from enum import Enum
from functools import cached_property

import attrs


class Kind(str, Enum):
    object = "object"
    array = "array"
    map = "map"
    map_array = "map_array"


Type = type


@attrs.define
class Attribute:
    type: Type = attrs.field(kw_only=True)
    key: str = attrs.field(kw_only=True)
    kind: Kind = attrs.field(kw_only=True, default=Kind.object)
    computed: bool = attrs.field(kw_only=True, default=False)
    alias: str | None = attrs.field(kw_only=True, default=None)

    @property
    def name(self):
        return self.alias if self.alias else self.key

    @cached_property
    def is_optional(self) -> bool:
        from .types import is_optional

        return is_optional(self.type)

    @property
    def is_collection(self):
        return self.kind in (Kind.map, Kind.array)
