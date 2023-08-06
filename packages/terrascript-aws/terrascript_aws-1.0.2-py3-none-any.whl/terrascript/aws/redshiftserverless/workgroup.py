import terrascript.core as core


@core.schema
class ConfigParameter(core.Schema):

    parameter_key: str | core.StringOut = core.attr(str)

    parameter_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameter_key: str | core.StringOut,
        parameter_value: str | core.StringOut,
    ):
        super().__init__(
            args=ConfigParameter.Args(
                parameter_key=parameter_key,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_key: str | core.StringOut = core.arg()

        parameter_value: str | core.StringOut = core.arg()


@core.resource(type="aws_redshiftserverless_workgroup", namespace="aws_redshiftserverless")
class Workgroup(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    base_capacity: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = core.attr(
        ConfigParameter, default=None, computed=True, kind=core.Kind.array
    )

    enhanced_vpc_routing: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    namespace_name: str | core.StringOut = core.attr(str)

    publicly_accessible: bool | core.BoolOut | None = core.attr(bool, default=None)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    workgroup_id: str | core.StringOut = core.attr(str, computed=True)

    workgroup_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        namespace_name: str | core.StringOut,
        workgroup_name: str | core.StringOut,
        base_capacity: int | core.IntOut | None = None,
        config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = None,
        enhanced_vpc_routing: bool | core.BoolOut | None = None,
        publicly_accessible: bool | core.BoolOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workgroup.Args(
                namespace_name=namespace_name,
                workgroup_name=workgroup_name,
                base_capacity=base_capacity,
                config_parameter=config_parameter,
                enhanced_vpc_routing=enhanced_vpc_routing,
                publicly_accessible=publicly_accessible,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_capacity: int | core.IntOut | None = core.arg(default=None)

        config_parameter: list[ConfigParameter] | core.ArrayOut[ConfigParameter] | None = core.arg(
            default=None
        )

        enhanced_vpc_routing: bool | core.BoolOut | None = core.arg(default=None)

        namespace_name: str | core.StringOut = core.arg()

        publicly_accessible: bool | core.BoolOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        workgroup_name: str | core.StringOut = core.arg()
