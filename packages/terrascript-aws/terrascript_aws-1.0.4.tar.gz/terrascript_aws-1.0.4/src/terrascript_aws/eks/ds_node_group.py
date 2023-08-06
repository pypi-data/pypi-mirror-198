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


@core.data(type="aws_eks_node_group", namespace="eks")
class DsNodeGroup(core.Data):
    """
    Type of Amazon Machine Image (AMI) associated with the EKS Node Group.
    """

    ami_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the EKS Node Group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the cluster.
    """
    cluster_name: str | core.StringOut = core.attr(str)

    """
    Disk size in GiB for worker nodes.
    """
    disk_size: int | core.IntOut = core.attr(int, computed=True)

    """
    EKS Cluster name and EKS Node Group name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of instance types associated with the EKS Node Group.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by thi
    s argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
    """
    labels: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    (Required) The name of the node group.
    """
    node_group_name: str | core.StringOut = core.attr(str)

    node_role_arn: str | core.StringOut = core.attr(str, computed=True)

    release_version: str | core.StringOut = core.attr(str, computed=True)

    """
    Configuration block with remote access settings.
    """
    remote_access: list[RemoteAccess] | core.ArrayOut[RemoteAccess] = core.attr(
        RemoteAccess, computed=True, kind=core.Kind.array
    )

    """
    List of objects containing information about underlying resources.
    """
    resources: list[Resources] | core.ArrayOut[Resources] = core.attr(
        Resources, computed=True, kind=core.Kind.array
    )

    """
    Configuration block with scaling settings.
    """
    scaling_config: list[ScalingConfig] | core.ArrayOut[ScalingConfig] = core.attr(
        ScalingConfig, computed=True, kind=core.Kind.array
    )

    """
    Status of the EKS Node Group.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Key-value map of resource tags.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    List of objects containing information about taints applied to the nodes in the EKS Node Group.
    """
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
