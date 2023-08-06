import terrascript.core as core


@core.schema
class SecurityServicePolicyData(core.Schema):

    managed_service_data: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        managed_service_data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SecurityServicePolicyData.Args(
                type=type,
                managed_service_data=managed_service_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        managed_service_data: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class ExcludeMap(core.Schema):

    account: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: list[str] | core.ArrayOut[core.StringOut] | None = None,
        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ExcludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class IncludeMap(core.Schema):

    account: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: list[str] | core.ArrayOut[core.StringOut] | None = None,
        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=IncludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_fms_policy", namespace="aws_fms")
class Policy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    delete_all_policy_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    delete_unused_fm_managed_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    exclude_map: ExcludeMap | None = core.attr(ExcludeMap, default=None)

    exclude_resource_tags: bool | core.BoolOut = core.attr(bool)

    id: str | core.StringOut = core.attr(str, computed=True)

    include_map: IncludeMap | None = core.attr(IncludeMap, default=None)

    name: str | core.StringOut = core.attr(str)

    policy_update_token: str | core.StringOut = core.attr(str, computed=True)

    remediation_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    resource_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_service_policy_data: SecurityServicePolicyData = core.attr(SecurityServicePolicyData)

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
        exclude_resource_tags: bool | core.BoolOut,
        name: str | core.StringOut,
        security_service_policy_data: SecurityServicePolicyData,
        delete_all_policy_resources: bool | core.BoolOut | None = None,
        delete_unused_fm_managed_resources: bool | core.BoolOut | None = None,
        exclude_map: ExcludeMap | None = None,
        include_map: IncludeMap | None = None,
        remediation_enabled: bool | core.BoolOut | None = None,
        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        resource_type: str | core.StringOut | None = None,
        resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                exclude_resource_tags=exclude_resource_tags,
                name=name,
                security_service_policy_data=security_service_policy_data,
                delete_all_policy_resources=delete_all_policy_resources,
                delete_unused_fm_managed_resources=delete_unused_fm_managed_resources,
                exclude_map=exclude_map,
                include_map=include_map,
                remediation_enabled=remediation_enabled,
                resource_tags=resource_tags,
                resource_type=resource_type,
                resource_type_list=resource_type_list,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_all_policy_resources: bool | core.BoolOut | None = core.arg(default=None)

        delete_unused_fm_managed_resources: bool | core.BoolOut | None = core.arg(default=None)

        exclude_map: ExcludeMap | None = core.arg(default=None)

        exclude_resource_tags: bool | core.BoolOut = core.arg()

        include_map: IncludeMap | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        remediation_enabled: bool | core.BoolOut | None = core.arg(default=None)

        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        resource_type: str | core.StringOut | None = core.arg(default=None)

        resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_service_policy_data: SecurityServicePolicyData = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
