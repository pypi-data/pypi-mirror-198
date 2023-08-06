import attrs

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    "[{{#each list}}{{{render this}}}{{#unless @last}},{{/unless}}{{/each}}]"
)


@attrs.define
class AstArray(Element):
    elements: list[Element] = attrs.field(factory=list)

    def add(self, el: Element) -> None:
        self.elements.append(el)

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
