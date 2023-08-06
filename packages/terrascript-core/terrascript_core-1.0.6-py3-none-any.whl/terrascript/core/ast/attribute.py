import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile("{{{key}}}{{#if op}} {{{op}}} {{/if}}{{{render value}}}")


@attrs.define
class AstAttribute(Element):
    key: str
    op: str = "="
    value: list[Element] | Element | None = None

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
