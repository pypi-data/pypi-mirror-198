import attrs

from .base import (
    Element,
    __compiler__,
    clear_literal,
    is_heredoc,
    is_literal,
    quote,
    strip_literal,
)

__t__ = __compiler__.compile("{{{value}}}")


@attrs.define
class AstNumber(Element):
    value: int | float

    def render(self) -> str:
        return __t__(self)


@attrs.define
class AstString(Element):
    value: str

    def render(self) -> str:
        s = self.value
        if is_heredoc(s):
            pass

        if is_literal(self.value):
            s = strip_literal(self.value)

        else:
            s = quote(clear_literal(self.value))

        self.value = s

        return __t__(self)
