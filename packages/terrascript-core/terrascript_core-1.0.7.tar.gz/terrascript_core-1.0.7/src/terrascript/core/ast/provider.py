import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    """provider "{{{name}}}" {
    {{#each elements}}
        {{{render this}}}
    {{/each}}
}
"""
)


@attrs.define
class AstProvider(Element):
    name: str
    elements: list[Element] = attrs.field(factory=list)

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
