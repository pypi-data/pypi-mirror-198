import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_redshift_parameter_group", namespace="redshift")
class ParameterGroup(core.Resource):
    """
    Amazon Resource Name (ARN) of parameter group
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the Redshift parameter group. Defaults to "Managed by Terraform".
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The family of the Redshift parameter group.
    """
    family: str | core.StringOut = core.attr(str)

    """
    The Redshift parameter group name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Redshift parameter group.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of Redshift parameters to apply.
    """
    parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        family: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ParameterGroup.Args(
                family=family,
                name=name,
                description=description,
                parameter=parameter,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        family: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
