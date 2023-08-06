import terrascript.core as core


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        name: str | core.StringOut,
        version: str | core.StringOut,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        version: str | core.StringOut = core.arg()


@core.data(type="aws_autoscaling_group", namespace="aws_autoscaling")
class DsGroup(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    default_cooldown: int | core.IntOut = core.attr(int, computed=True)

    desired_capacity: int | core.IntOut = core.attr(int, computed=True)

    enabled_metrics: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    health_check_grace_period: int | core.IntOut = core.attr(int, computed=True)

    health_check_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    launch_configuration: str | core.StringOut = core.attr(str, computed=True)

    launch_template: list[LaunchTemplate] | core.ArrayOut[LaunchTemplate] = core.attr(
        LaunchTemplate, computed=True, kind=core.Kind.array
    )

    load_balancers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_size: int | core.IntOut = core.attr(int, computed=True)

    min_size: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

    new_instances_protected_from_scale_in: bool | core.BoolOut = core.attr(bool, computed=True)

    placement_group: str | core.StringOut = core.attr(str, computed=True)

    service_linked_role_arn: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    target_group_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    termination_policies: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_zone_identifier: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
