import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    apply_method: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
        apply_method: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
                apply_method=apply_method,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_method: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_db_parameter_group", namespace="rds")
class DbParameterGroup(core.Resource):
    """
    The ARN of the db parameter group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The description of the DB parameter group. Defaults to "Managed by T
    erraform".
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, Forces new resource) The family of the DB parameter group.
    """
    family: str | core.StringOut = core.attr(str)

    """
    The db parameter group name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The name of the DB parameter group. If omitted, Terraform will assig
    n a random, unique name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of DB parameters to apply. Note that parameters may differ from a family to an oth
    er. Full list of all parameters can be discovered via [`aws rds describe-db-parameters`](https://doc
    s.aws.amazon.com/cli/latest/reference/rds/describe-db-parameters.html) after initial creation of the
    group.
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
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbParameterGroup.Args(
                family=family,
                description=description,
                name=name,
                name_prefix=name_prefix,
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

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        parameter: list[Parameter] | core.ArrayOut[Parameter] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
