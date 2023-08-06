from ...lang.decorators import arg, schema, schema_args
from ...lang.types import Schema, SchemaArgs


@schema
class Local(Schema):
    def __init__(
        self,
        *,
        path: str | None = None,
        workspace_dir: str | None = None,
    ):
        super().__init__(
            Local.Args(
                path=path,
                workspace_dir=workspace_dir,
            )
        )

    @staticmethod
    def label_() -> str | None:
        return "local"

    @schema_args
    class Args(SchemaArgs):
        """
        The path to the tfstate file. This defaults to "terraform.tfstate" relative to
        the root module by default.
        """

        path: str | None = arg(default=None)

        """
        The path to the tfstate file. This defaults to "terraform.tfstate" relative to
        the root module by default.
        """
        workspace_dir: str | None = arg(default=None)
