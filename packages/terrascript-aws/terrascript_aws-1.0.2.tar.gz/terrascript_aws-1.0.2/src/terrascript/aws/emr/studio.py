import terrascript.core as core


@core.resource(type="aws_emr_studio", namespace="aws_emr")
class Studio(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    auth_mode: str | core.StringOut = core.attr(str)

    default_s3_location: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    engine_security_group_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    idp_auth_url: str | core.StringOut | None = core.attr(str, default=None)

    idp_relay_state_parameter_name: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    service_role: str | core.StringOut = core.attr(str)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: str | core.StringOut = core.attr(str, computed=True)

    user_role: str | core.StringOut | None = core.attr(str, default=None)

    vpc_id: str | core.StringOut = core.attr(str)

    workspace_security_group_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        auth_mode: str | core.StringOut,
        default_s3_location: str | core.StringOut,
        engine_security_group_id: str | core.StringOut,
        name: str | core.StringOut,
        service_role: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        workspace_security_group_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        idp_auth_url: str | core.StringOut | None = None,
        idp_relay_state_parameter_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        user_role: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Studio.Args(
                auth_mode=auth_mode,
                default_s3_location=default_s3_location,
                engine_security_group_id=engine_security_group_id,
                name=name,
                service_role=service_role,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                workspace_security_group_id=workspace_security_group_id,
                description=description,
                idp_auth_url=idp_auth_url,
                idp_relay_state_parameter_name=idp_relay_state_parameter_name,
                tags=tags,
                tags_all=tags_all,
                user_role=user_role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auth_mode: str | core.StringOut = core.arg()

        default_s3_location: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        engine_security_group_id: str | core.StringOut = core.arg()

        idp_auth_url: str | core.StringOut | None = core.arg(default=None)

        idp_relay_state_parameter_name: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        service_role: str | core.StringOut = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_role: str | core.StringOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()

        workspace_security_group_id: str | core.StringOut = core.arg()
