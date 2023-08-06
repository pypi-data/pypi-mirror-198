from __future__ import annotations

import json
import os
from functools import cached_property
from typing import TYPE_CHECKING, Callable, cast

if TYPE_CHECKING:
    from terrascript.core.lang.types import Out, Schema
    from terrascript.core.lang.block import Block

import cattrs
from pydash import pull

from .cmd import Terraform
from .generate import Generator


class Runner:
    def __init__(self, ctx: Context):
        self.ctx = ctx
        self._generator = Generator(self.ctx.path, blocks=self.ctx.blocks)
        self._tf = Terraform(path=self.ctx.path)
        self._workspace: str | None = None

    def prepare(self):
        self.ctx.register_exports()
        self._generator.generate()

        self._tf.format()
        self._tf.init()
        if self._workspace:
            self._tf.workspace(self._workspace)

    def apply(self):
        from terrascript.core.lang.output import TerraformOutput, process_outputs

        self.prepare()
        self._tf.apply()

        rc, out = self._tf.output()
        if rc == 0 and out:
            process_outputs(
                self.ctx.export_blocks,
                cattrs.structure(json.loads(out), dict[str, TerraformOutput]),
            )

    def plan(self):
        self.prepare()
        self._tf.plan()

    def destroy(self):
        self.prepare()
        self._tf.destroy()

    def workspace(self, name: str):
        self._workspace = name

    def stdout(self, cb: Callable[[str], None | int]):
        self._tf.stdout(cb)


class Context:
    def __init__(self, *, path: str | None = None):
        self._path = path
        self._blocks = []
        self._exports = []
        self._exportBlocks = []
        self._runner = Runner(self)

    @cached_property
    def path(self):
        return self._path if self._path else os.path.join(os.getcwd(), ".terrascript")

    @property
    def blocks(self):
        return self._blocks

    @property
    def export_blocks(self):
        return self._exportBlocks

    @property
    def exports(self):
        return self._exports

    def register(self, block: Block):
        self._blocks.append(block)

    def unregister(self, block: Block):
        pull(self._blocks, block)

    def apply(self):
        self._runner.apply()

    def plan(self):
        self._runner.plan()

    def destroy(self):
        self._runner.destroy()

    def workspace(self, name) -> Context:
        self._runner.workspace(name)
        return self

    def export(self, exp: Out):
        out = self._traverse(exp)
        if out:
            self._exports.append(out)
            self._exportBlocks.append(out.parent)

    def stdout(self, cb: Callable[[str], None | int]):
        self._runner.stdout(cb)

    @classmethod
    def _traverse(cls, exp: Out) -> Out | None:
        from terrascript.core.lang.block import is_configuration
        from terrascript.core.lang.types import (
            Collection,
            Out,
            is_collection,
            is_out,
            is_schema,
        )

        out = None
        if is_schema(exp):
            out = cast(Schema, exp).out_()
        elif is_collection(exp):
            out = cast(Collection, exp).item
        elif is_out(exp):
            out = cast(Out, exp)

        if out and out.parent:
            if is_configuration(out.parent):
                return out
            else:
                parent = out.parent.out_()
                if parent:
                    cls._traverse(parent)

        return None

    def register_exports(self):
        from terrascript.core.lang.output import Output
        from terrascript.core.lang.types import is_schema

        for exp in self._exports:
            if is_schema(exp):
                exp = exp.out_()

            Output(
                name=f"{exp.parent.type_}-{exp.parent.name_}-{exp.attr.name}",
                value=f"${{{exp.expr_()}}}",
            )


ctx = Context()


def register_block(block: Block):
    ctx.register(block)


def unregister_block(block: Block):
    ctx.unregister(block)


def apply():
    ctx.apply()


def plan():
    ctx.plan()


def destroy():
    ctx.destroy()


def workspace(name: str) -> Context:
    ctx.workspace(name)
    return ctx


def export(out: Out):
    ctx.export(out)


def stdout(cb: Callable[[str], None | int]) -> Context:
    ctx.stdout(cb)
    return ctx
