import attrs


@attrs.define
class Argument:
    key: str
    alias: str | None = attrs.field(default=None, kw_only=True)

    @property
    def name(self):
        return self.alias if self.alias else self.key
