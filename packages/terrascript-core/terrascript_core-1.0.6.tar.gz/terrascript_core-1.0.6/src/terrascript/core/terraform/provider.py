from ..lang.decorators import arg, schema, schema_args
from ..lang.provider import Provider as Base
from ..lang.types import SchemaArgs


@schema
class Provider(Base):
    ...

    @schema_args
    class Args(SchemaArgs):
        """
        Provider alias
        """

        alias: str | None = arg(default=None)

        """
        Provider version
        """
        version: str | None = arg(default=None)
