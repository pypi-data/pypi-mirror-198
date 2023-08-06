import attrs

from .attribute import AstAttribute
from .base import Element
from .object import AstObject


@attrs.define
class AstArgument(Element):
    key: str
    op: str | None = None
    label: str | None = None
    value: list[Element] | Element | None = None

    def render(self) -> str:
        ast: Element
        if isinstance(self.value, list):
            ast = AstObject(
                self.key, op=self.op if self.op else "", elements=self.value, label=self.label
            )
        else:
            ast = AstAttribute(self.key, op=self.op if self.op else "=", value=self.value)

        return ast.render()
