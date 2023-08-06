from ...lang.decorators import arg, schema, schema_args
from ...lang.types import Schema, SchemaArgs


@schema
class Workspaces(Schema):
    def __init__(
        self,
        *,
        name: str | None = None,
        prefix: str | None = None,
    ):
        super().__init__(
            Workspaces.Args(
                name=name,
                prefix=prefix,
            )
        )

    @schema_args
    class Args(SchemaArgs):
        """
        The full name of one remote workspace. When configured, only the default workspace
        can be used.
        """

        name: str | None = arg(default=None)

        """
        A prefix used in the names of one or more remote workspaces, all of which can be
        used with this configuration. The full workspace names are used in Terraform Cloud,
        and the short names (minus the prefix) are used on the command line for Terraform CLI
        workspaces. If omitted, only the default workspace can be used
        """
        prefix: str | None = arg(default=None)


@schema
class Remote(Schema):
    def __init__(
        self,
        *,
        organization: str,
        workspaces: Workspaces,
        hostname: str | None = None,
        token: str | None = None,
    ):
        super().__init__(
            Remote.Args(
                organization=organization,
                workspaces=workspaces,
                hostname=hostname,
                token=token,
            )
        )

    @staticmethod
    def label_() -> str | None:
        return "remote"

    @schema_args
    class Args(SchemaArgs):
        """
        The remote backend hostname to connect to. Defaults to app.terraform.io.
        """

        hostname: str | None = arg(default=None)

        """
        The name of the organization containing the targeted workspace(s).
        """
        organization: str = arg()

        """
        The token used to authenticate with the remote backend. We recommend omitting
        the token from the configuration, and instead using terraform login or manually
        configuring credentials in the CLI config file.
        """
        token: str | None = arg(default=None)

        """
        A block specifying which remote workspace(s) to use
        """
        workspaces: Workspaces = arg()
