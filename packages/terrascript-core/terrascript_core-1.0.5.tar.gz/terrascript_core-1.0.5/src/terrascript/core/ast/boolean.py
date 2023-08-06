import attrs

from .base import Element, __compiler__

__t__ = __compiler__.compile("{{#if value}}true{{else}}false{{/if}}")


@attrs.define
class AstBoolean(Element):
    value: bool

    def render(self) -> str:
        return __t__(self)
