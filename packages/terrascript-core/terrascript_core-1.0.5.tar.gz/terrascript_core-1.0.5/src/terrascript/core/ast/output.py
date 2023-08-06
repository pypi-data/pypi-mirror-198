import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    """output "{{{name}}}" {
    value = {{{render value}}}
    {{#if sensitive}}sensitive = yes{{/if}}
}
"""
)


@attrs.define
class AstOutput(Element):
    name: str
    value: Element | None = None
    description: str | None = None
    sensitive: bool | None = None

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
