import terrascript.core as core


@core.schema
class OptionSettings(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=OptionSettings.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Option(core.Schema):

    db_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    option_name: str | core.StringOut = core.attr(str)

    option_settings: list[OptionSettings] | core.ArrayOut[OptionSettings] | None = core.attr(
        OptionSettings, default=None, kind=core.Kind.array
    )

    port: int | core.IntOut | None = core.attr(int, default=None)

    version: str | core.StringOut | None = core.attr(str, default=None)

    vpc_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        option_name: str | core.StringOut,
        db_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = None,
        option_settings: list[OptionSettings] | core.ArrayOut[OptionSettings] | None = None,
        port: int | core.IntOut | None = None,
        version: str | core.StringOut | None = None,
        vpc_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Option.Args(
                option_name=option_name,
                db_security_group_memberships=db_security_group_memberships,
                option_settings=option_settings,
                port=port,
                version=version,
                vpc_security_group_memberships=vpc_security_group_memberships,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        option_name: str | core.StringOut = core.arg()

        option_settings: list[OptionSettings] | core.ArrayOut[OptionSettings] | None = core.arg(
            default=None
        )

        port: int | core.IntOut | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)

        vpc_security_group_memberships: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_db_option_group", namespace="rds")
class DbOptionGroup(core.Resource):
    """
    The ARN of the db option group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the name of the engine that this option group should be associated with.
    """
    engine_name: str | core.StringOut = core.attr(str)

    """
    The db option group name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the major version of the engine that this option group should be associated wit
    h.
    """
    major_engine_version: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The name of the option group. If omitted, Terraform will assign a ra
    ndom, unique name. Must be lowercase, to match as it is stored in AWS.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) Creates a unique name beginning with the specified prefix. Conflicts
    with `name`. Must be lowercase, to match as it is stored in AWS.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of Options to apply.
    """
    option: list[Option] | core.ArrayOut[Option] | None = core.attr(
        Option, default=None, kind=core.Kind.array
    )

    """
    (Optional) The description of the option group. Defaults to "Managed by Terraform".
    """
    option_group_description: str | core.StringOut | None = core.attr(str, default=None)

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
        engine_name: str | core.StringOut,
        major_engine_version: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        option: list[Option] | core.ArrayOut[Option] | None = None,
        option_group_description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbOptionGroup.Args(
                engine_name=engine_name,
                major_engine_version=major_engine_version,
                name=name,
                name_prefix=name_prefix,
                option=option,
                option_group_description=option_group_description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        engine_name: str | core.StringOut = core.arg()

        major_engine_version: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        option: list[Option] | core.ArrayOut[Option] | None = core.arg(default=None)

        option_group_description: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
