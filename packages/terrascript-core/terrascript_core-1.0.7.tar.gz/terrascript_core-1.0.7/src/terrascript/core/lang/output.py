from typing import Any

import attrs
from pydash import is_list, starts_with

from ..ast import AstOutput
from ..context import register_block
from .attribute import Kind
from .block import Attribute, Block, ConfigurationBlock, Schema
from .types import parse_primitive


@attrs.define
class TerraformOutput:
    type: Any
    value: Any
    sensitive: bool


@attrs.define(init=False)
class Output(Block):
    name: str = attrs.field(kw_only=True)
    value: str | None = attrs.field(kw_only=True, default=None)
    sensitive: bool = attrs.field(kw_only=True, default=False)

    def __init__(
        self,
        *,
        name: str,
        value: str | None = None,
        sensitive: bool | None = False,
    ):
        super().__init__()

        args = dict(
            name=name,
            value=value,
            sensitive=sensitive,
        )

        self.__attrs_init__(**args)  # type: ignore

        register_block(self)

    @property
    def namespace_(self):
        return "outputs"

    def generate(self) -> str:
        ast = AstOutput(self.name, sensitive=self.sensitive)

        if self.value:
            el = parse_primitive(self.value)
            if el:
                ast.value = el

        return ast.render()


def process_outputs(blocks: list[Block], outputs: dict[str, TerraformOutput]):
    for block in blocks:
        if isinstance(block, ConfigurationBlock):
            for k, v in outputs.items():
                prefix = f"{block.type_}-{block.name_}-"
                if starts_with(k, prefix):
                    process_output(k.replace(prefix, ""), block, v)


def process_output(key: str, block: ConfigurationBlock, output: TerraformOutput):
    for attr in block.attrs_():
        if attr.name == key:
            process_attribute(block, attr, output.value)
            break


def process_attribute(block: Schema, attr: Attribute, value: Any):
    if attr.type == str or attr.type == float or attr.type == int or attr.type == bool:
        if attr.kind == Kind.array:
            item = [i for i in value]
        elif attr.kind == Kind.map:
            item = {k: v for k, v in value.items()}
        else:
            item = value

    else:
        if issubclass(attr.type, Schema):
            item = attr.type.new()
            if attr.kind == Kind.array:
                item = process_array(attr, value)
            elif attr.kind == Kind.map:
                item = process_map(attr, value)
            else:
                process_schema(item, value[0] if is_list(value) else value)

        else:
            item = value

    if item:
        setattr(block, attr.key, item)


def process_schema(schema: Schema, value: dict[str, Any]):
    for attr in schema.attrs_():
        if value and attr.name in value:
            process_attribute(schema, attr, value[attr.name])


def process_array(attr: Attribute, value: list[Any]):
    arr = []
    for item in value:
        if issubclass(attr.type, Schema):
            el = attr.type.new()
            process_schema(el, item)
            arr.append(el)
    return arr


def process_map(attr: Attribute, value: dict[str, Any]):
    m = dict()
    for k, v in value.items():
        if issubclass(attr.type, Schema):
            el = attr.type.new()
            process_schema(el, v)
            m[k] = el
    return m
