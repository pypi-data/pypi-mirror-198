import terrascript.core as core


@core.schema
class ComputeCapacity(core.Schema):

    available: int | core.IntOut = core.attr(int, computed=True)

    desired_instances: int | core.IntOut = core.attr(int)

    in_use: int | core.IntOut = core.attr(int, computed=True)

    running: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        available: int | core.IntOut,
        desired_instances: int | core.IntOut,
        in_use: int | core.IntOut,
        running: int | core.IntOut,
    ):
        super().__init__(
            args=ComputeCapacity.Args(
                available=available,
                desired_instances=desired_instances,
                in_use=in_use,
                running=running,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        available: int | core.IntOut = core.arg()

        desired_instances: int | core.IntOut = core.arg()

        in_use: int | core.IntOut = core.arg()

        running: int | core.IntOut = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class DomainJoinInfo(core.Schema):

    directory_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    organizational_unit_distinguished_name: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        directory_name: str | core.StringOut | None = None,
        organizational_unit_distinguished_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DomainJoinInfo.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_name: str | core.StringOut | None = core.arg(default=None)

        organizational_unit_distinguished_name: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_appstream_fleet", namespace="appstream")
class Fleet(core.Resource):
    """
    ARN of the appstream fleet.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block for the desired capacity of the fleet. See below.
    """
    compute_capacity: ComputeCapacity = core.attr(ComputeCapacity)

    """
    Date and time, in UTC and extended RFC 3339 format, when the fleet was created.
    """
    created_time: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description to display.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Amount of time that a streaming session remains active after users disconnect.
    """
    disconnect_timeout_in_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) Human-readable friendly name for the AppStream fleet.
    """
    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block for the name of the directory and organizational unit (OU) to use to
    join the fleet to a Microsoft Active Directory domain. See below.
    """
    domain_join_info: DomainJoinInfo | None = core.attr(DomainJoinInfo, default=None, computed=True)

    """
    (Optional) Enables or disables default internet access for the fleet.
    """
    enable_default_internet_access: bool | core.BoolOut | None = core.attr(
        bool, default=None, computed=True
    )

    """
    (Optional) Fleet type. Valid values are: `ON_DEMAND`, `ALWAYS_ON`
    """
    fleet_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) ARN of the IAM role to apply to the fleet.
    """
    iam_role_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Unique identifier (ID) of the appstream fleet.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amount of time that users can be idle (inactive) before they are disconnected from their
    streaming session and the `disconnect_timeout_in_seconds` time interval begins.
    """
    idle_disconnect_timeout_in_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) ARN of the public, private, or shared image to use.
    """
    image_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Name of the image used to create the fleet.
    """
    image_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Instance type to use when launching fleet instances.
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    (Optional) Maximum amount of time that a streaming session can remain active, in seconds.
    """
    max_user_duration_in_seconds: int | core.IntOut | None = core.attr(
        int, default=None, computed=True
    )

    """
    (Required) Unique name for the fleet.
    """
    name: str | core.StringOut = core.attr(str)

    """
    State of the fleet. Can be `STARTING`, `RUNNING`, `STOPPING` or `STOPPED`
    """
    state: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) AppStream 2.0 view that is displayed to your users when they stream from the fleet. When
    APP` is specified, only the windows of applications opened by users display. When `DESKTOP` is spec
    ified, the standard desktop that is provided by the operating system displays. If not specified, def
    aults to `APP`.
    """
    stream_view: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Map of tags to attach to AppStream instances.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Configuration block for the VPC configuration for the image builder. See below.
    """
    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        compute_capacity: ComputeCapacity,
        instance_type: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        disconnect_timeout_in_seconds: int | core.IntOut | None = None,
        display_name: str | core.StringOut | None = None,
        domain_join_info: DomainJoinInfo | None = None,
        enable_default_internet_access: bool | core.BoolOut | None = None,
        fleet_type: str | core.StringOut | None = None,
        iam_role_arn: str | core.StringOut | None = None,
        idle_disconnect_timeout_in_seconds: int | core.IntOut | None = None,
        image_arn: str | core.StringOut | None = None,
        image_name: str | core.StringOut | None = None,
        max_user_duration_in_seconds: int | core.IntOut | None = None,
        stream_view: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                compute_capacity=compute_capacity,
                instance_type=instance_type,
                name=name,
                description=description,
                disconnect_timeout_in_seconds=disconnect_timeout_in_seconds,
                display_name=display_name,
                domain_join_info=domain_join_info,
                enable_default_internet_access=enable_default_internet_access,
                fleet_type=fleet_type,
                iam_role_arn=iam_role_arn,
                idle_disconnect_timeout_in_seconds=idle_disconnect_timeout_in_seconds,
                image_arn=image_arn,
                image_name=image_name,
                max_user_duration_in_seconds=max_user_duration_in_seconds,
                stream_view=stream_view,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_capacity: ComputeCapacity = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        disconnect_timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)

        display_name: str | core.StringOut | None = core.arg(default=None)

        domain_join_info: DomainJoinInfo | None = core.arg(default=None)

        enable_default_internet_access: bool | core.BoolOut | None = core.arg(default=None)

        fleet_type: str | core.StringOut | None = core.arg(default=None)

        iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        idle_disconnect_timeout_in_seconds: int | core.IntOut | None = core.arg(default=None)

        image_arn: str | core.StringOut | None = core.arg(default=None)

        image_name: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        max_user_duration_in_seconds: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        stream_view: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
