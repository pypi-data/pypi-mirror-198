import terrascript.core as core


@core.schema
class ScalingConfig(core.Schema):

    desired_size: int | core.IntOut = core.attr(int, computed=True)

    max_size: int | core.IntOut = core.attr(int, computed=True)

    min_size: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        desired_size: int | core.IntOut,
        max_size: int | core.IntOut,
        min_size: int | core.IntOut,
    ):
        super().__init__(
            args=ScalingConfig.Args(
                desired_size=desired_size,
                max_size=max_size,
                min_size=min_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_size: int | core.IntOut = core.arg()

        max_size: int | core.IntOut = core.arg()

        min_size: int | core.IntOut = core.arg()


@core.schema
class Taints(core.Schema):

    effect: str | core.StringOut = core.attr(str, computed=True)

    key: str | core.StringOut = core.attr(str, computed=True)

    value: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        effect: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Taints.Args(
                effect=effect,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effect: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class RemoteAccess(core.Schema):

    ec2_ssh_key: str | core.StringOut = core.attr(str, computed=True)

    source_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ec2_ssh_key: str | core.StringOut,
        source_security_group_ids: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=RemoteAccess.Args(
                ec2_ssh_key=ec2_ssh_key,
                source_security_group_ids=source_security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_ssh_key: str | core.StringOut = core.arg()

        source_security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class AutoscalingGroups(core.Schema):

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=AutoscalingGroups.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()


@core.schema
class Resources(core.Schema):

    autoscaling_groups: list[AutoscalingGroups] | core.ArrayOut[AutoscalingGroups] = core.attr(
        AutoscalingGroups, computed=True, kind=core.Kind.array
    )

    remote_access_security_group_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        autoscaling_groups: list[AutoscalingGroups] | core.ArrayOut[AutoscalingGroups],
        remote_access_security_group_id: str | core.StringOut,
    ):
        super().__init__(
            args=Resources.Args(
                autoscaling_groups=autoscaling_groups,
                remote_access_security_group_id=remote_access_security_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling_groups: list[AutoscalingGroups] | core.ArrayOut[AutoscalingGroups] = core.arg()

        remote_access_security_group_id: str | core.StringOut = core.arg()


@core.data(type="aws_eks_node_group", namespace="aws_eks")
class DsNodeGroup(core.Data):

    ami_type: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    disk_size: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    labels: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    node_group_name: str | core.StringOut = core.attr(str)

    node_role_arn: str | core.StringOut = core.attr(str, computed=True)

    release_version: str | core.StringOut = core.attr(str, computed=True)

    remote_access: list[RemoteAccess] | core.ArrayOut[RemoteAccess] = core.attr(
        RemoteAccess, computed=True, kind=core.Kind.array
    )

    resources: list[Resources] | core.ArrayOut[Resources] = core.attr(
        Resources, computed=True, kind=core.Kind.array
    )

    scaling_config: list[ScalingConfig] | core.ArrayOut[ScalingConfig] = core.attr(
        ScalingConfig, computed=True, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    taints: list[Taints] | core.ArrayOut[Taints] = core.attr(
        Taints, computed=True, kind=core.Kind.array
    )

    version: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: str | core.StringOut,
        node_group_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsNodeGroup.Args(
                cluster_name=cluster_name,
                node_group_name=node_group_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: str | core.StringOut = core.arg()

        node_group_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
