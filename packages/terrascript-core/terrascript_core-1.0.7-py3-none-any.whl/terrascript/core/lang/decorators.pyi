from typing import Any, Callable, TypeVar

from attr import attrib
from attrs import NOTHING, field

from .attribute import Kind

_T = TypeVar("_T")

def __dataclass_transform__(
    *,
    eq_default: bool = True,
    order_default: bool = False,
    kw_only_default: bool = False,
    field_descriptors: tuple[type | Callable[..., Any], ...] = (()),
) -> Callable[[_T], _T]: ...
def schema(cls): ...
@__dataclass_transform__(field_descriptors=(attrib, field))
def schema_args(cls): ...
@__dataclass_transform__(field_descriptors=(attrib, field))
def attr(
    type: type,
    *,
    alias: str | None = None,
    kind: Kind = Kind.object,
    computed: bool = False,
    default: Any = NOTHING,
): ...
@__dataclass_transform__(field_descriptors=(attrib, field))
def arg(*, default: Any = NOTHING): ...
@__dataclass_transform__(field_descriptors=(attrib, field))
def configuration(
    maybe_cls=None,
    type: str = "",
    namespace: str = "",
): ...
@__dataclass_transform__(field_descriptors=(attrib, field))
def provider(
    maybe_cls=None,
    name: str = "",
): ...

data = configuration
resource = configuration
