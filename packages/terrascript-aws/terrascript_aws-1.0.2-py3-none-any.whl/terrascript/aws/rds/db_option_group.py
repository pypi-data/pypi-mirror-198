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


@core.resource(type="aws_db_option_group", namespace="aws_rds")
class DbOptionGroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    engine_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    major_engine_version: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    option: list[Option] | core.ArrayOut[Option] | None = core.attr(
        Option, default=None, kind=core.Kind.array
    )

    option_group_description: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
