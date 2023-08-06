import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    """{{{key}}}{{#if label}} "{{{label}}}"{{/if}} {{{op}}} {
{{#each elements}}
    {{{render this}}}
{{/each}}
}"""
)


@attrs.define
class AstObject(Element):
    key: str
    op: str = ""
    label: str | None = None
    elements: list[Element] = attrs.field(factory=list)

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
