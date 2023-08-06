import terrascript.core as core


@core.schema
class OutputConfig(core.Schema):

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    s3_output_location: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        s3_output_location: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OutputConfig.Args(
                s3_output_location=s3_output_location,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        s3_output_location: str | core.StringOut = core.arg()


@core.resource(type="aws_sagemaker_device_fleet", namespace="aws_sagemaker")
class DeviceFleet(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    device_fleet_name: str | core.StringOut = core.attr(str)

    enable_iot_role_alias: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    iot_role_alias: str | core.StringOut = core.attr(str, computed=True)

    output_config: OutputConfig = core.attr(OutputConfig)

    role_arn: str | core.StringOut = core.attr(str)

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
        device_fleet_name: str | core.StringOut,
        output_config: OutputConfig,
        role_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        enable_iot_role_alias: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeviceFleet.Args(
                device_fleet_name=device_fleet_name,
                output_config=output_config,
                role_arn=role_arn,
                description=description,
                enable_iot_role_alias=enable_iot_role_alias,
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

        device_fleet_name: str | core.StringOut = core.arg()

        enable_iot_role_alias: bool | core.BoolOut | None = core.arg(default=None)

        output_config: OutputConfig = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
