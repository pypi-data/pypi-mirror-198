import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    """terraform {
    {{#each elements}}
        {{{render this}}}
    {{/each}}
}
"""
)


@attrs.define
class AstTerraform(Element):
    elements: list[Element] = attrs.field(factory=list)

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
