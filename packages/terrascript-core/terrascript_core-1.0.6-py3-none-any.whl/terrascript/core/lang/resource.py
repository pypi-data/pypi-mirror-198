from ..ast.resource import AstResource
from .attribute import Kind
from .block import ConfigurationBlock
from .decorators import arg, attr, schema, schema_args
from .types import ArrayOut, BoolOut, Schema, SchemaArgs, StringOut


@schema
class Lifecycle(Schema):
    """
    By default, when Terraform must make a change to a resource argument that cannot
    be updated in-place due to remote API limitations, Terraform will instead destroy
    the existing object and then create a new replacement object with the new configured
    arguments.
    """

    create_before_destroy: bool | BoolOut | None = attr(bool, default=None)

    """
    This meta-argument, when set to true, will cause Terraform to reject with an error any
    plan that would destroy the infrastructure object associated with the resource, as long
    as the argument remains present in the configuration.
    """
    prevent_destroy: bool | BoolOut | None = attr(bool, default=None)

    """
    By default, Terraform detects any difference in the current settings of a real
    infrastructure object and plans to update the remote object to match configuration.
    """
    ignore_changed: list[str] | ArrayOut[StringOut] | None = attr(
        str, kind=Kind.array, default=None
    )

    def __init__(
        self,
        *,
        create_before_destroy: bool | BoolOut | None = None,
        prevent_destroy: bool | BoolOut | None = None,
        ignore_changed: list[str] | ArrayOut[StringOut] | None = None,
    ):
        super().__init__(
            Lifecycle.Args(
                create_before_destroy=create_before_destroy,
                prevent_destroy=prevent_destroy,
                ignore_changed=ignore_changed,
            )
        )

    @schema_args
    class Args(SchemaArgs):
        create_before_destroy: bool | BoolOut | None = arg(default=None)

        prevent_destroy: bool | BoolOut | None = arg(default=None)

        ignore_changed: list[str] | ArrayOut[StringOut] | None = arg(default=None)


@schema
class Resource(ConfigurationBlock):
    """
    Explicitly specifying a dependency is only necessary when a resource relies
    on some other resource's behavior but doesn't access any of that resource's
    data in its arguments.
    """

    depends_on: list[str] | ArrayOut[StringOut] | None = attr(str, kind=Kind.array, default=None)

    """
    The provider meta-argument specifies which provider configuration to use, overriding
    Terraform's default behavior of selecting one based on the resource type name.
    """
    provider: str | StringOut | None = attr(str, default=None)

    """
    Customize the behaviour of the resources
    """
    lifecycle: Lifecycle | None = attr(Lifecycle, default=None)

    def generate(self) -> str:
        self.parse()

        ast = AstResource(self.name_, self.type_, self.ast_())
        return ast.render()

    @schema_args
    class Args(SchemaArgs):
        depends_on: list[str] | ArrayOut[StringOut] | None = arg(default=None)

        provider: str | StringOut | None = arg(default=None)

        lifecycle: Lifecycle | None = arg(default=None)
