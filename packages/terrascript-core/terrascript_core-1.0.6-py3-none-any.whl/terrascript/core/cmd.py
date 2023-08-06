import shutil
from functools import cached_property
from typing import Callable

from command_runner import command_runner


class CmdError(Exception):
    ...


def _run(
    cmd: list[str],
    *,
    cwd: str | None = None,
    stdout: Callable[[str], None] | None = None,
    raise_on_error: bool = True,
) -> tuple[int, str | bytes | None]:
    rc, output = command_runner(cmd, method="poller", stdout=stdout, stderr=stdout, cwd=cwd)
    if raise_on_error and rc != 0:
        raise CmdError(f"Problem running command {' '.join(cmd)}")
    return rc, output


class Terraform:
    def __init__(
        self,
        *,
        path: str | None = None,
        cb: Callable[[str], None | int] | None = None,
    ):
        self.path = path
        self._cb = cb

        exe = shutil.which("terraform")
        if not exe:
            raise CmdError("Missing terraform installation")

        self._exe: str = exe

    def stdout(self, cb: Callable[[str], None | int]):
        self._cb = cb

    @cached_property
    def args(self):
        args = dict()
        if self.path:
            args["cwd"] = self.path
        return args

    def on_stdout(self, line: str):
        if self._cb:
            self._cb(line)

    def init(self):
        return _run([self._exe, "init"], stdout=self.on_stdout, **self.args)

    def workspace(self, name: str):
        _run(
            [self._exe, "workspace", "new", name],
            stdout=self.on_stdout,
            raise_on_error=False,
            **self.args,
        )

        return _run([self._exe, "workspace", "select", name], stdout=self.on_stdout, **self.args)

    def plan(self):
        return _run([self._exe, "plan"], stdout=self.on_stdout, **self.args)

    def apply(self):
        return _run([self._exe, "apply", "-auto-approve"], stdout=self.on_stdout, **self.args)

    def destroy(self):
        return _run(
            [self._exe, "apply", "-auto-approve", "-destroy"], stdout=self.on_stdout, **self.args
        )

    def format(self):
        return _run([self._exe, "fmt", "-recursive"], stdout=self.on_stdout, **self.args)

    def output(self) -> tuple[int, str | bytes | None]:
        return _run([self._exe, "output", "-json"], stdout=self.on_stdout, **self.args)
