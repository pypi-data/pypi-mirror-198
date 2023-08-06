import terrascript.core as core


@core.schema
class UpdateConfig(core.Schema):

    max_unavailable: int | core.IntOut | None = core.attr(int, default=None)

    max_unavailable_percentage: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_unavailable: int | core.IntOut | None = None,
        max_unavailable_percentage: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=UpdateConfig.Args(
                max_unavailable=max_unavailable,
                max_unavailable_percentage=max_unavailable_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_unavailable: int | core.IntOut | None = core.arg(default=None)

        max_unavailable_percentage: int | core.IntOut | None = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        version: str | core.StringOut,
        id: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                version=version,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()


@core.schema
class ScalingConfig(core.Schema):

    desired_size: int | core.IntOut = core.attr(int)

    max_size: int | core.IntOut = core.attr(int)

    min_size: int | core.IntOut = core.attr(int)

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
class RemoteAccess(core.Schema):

    ec2_ssh_key: str | core.StringOut | None = core.attr(str, default=None)

    source_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ec2_ssh_key: str | core.StringOut | None = None,
        source_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RemoteAccess.Args(
                ec2_ssh_key=ec2_ssh_key,
                source_security_group_ids=source_security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_ssh_key: str | core.StringOut | None = core.arg(default=None)

        source_security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


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
class Taint(core.Schema):

    effect: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        effect: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Taint.Args(
                effect=effect,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effect: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_eks_node_group", namespace="eks")
class NodeGroup(core.Resource):
    """
    (Optional) Type of Amazon Machine Image (AMI) associated with the EKS Node Group. See the [AWS docum
    entation](https://docs.aws.amazon.com/eks/latest/APIReference/API_Nodegroup.html#AmazonEKS-Type-Node
    group-amiType) for valid values. Terraform will only perform drift detection if a configuration valu
    e is provided.
    """

    ami_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the EKS Node Group.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Type of capacity associated with the EKS Node Group. Valid values: `ON_DEMAND`, `SPOT`. T
    erraform will only perform drift detection if a configuration value is provided.
    """
    capacity_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Disk size in GiB for worker nodes. Defaults to `20`. Terraform will only perform drift de
    tection if a configuration value is provided.
    """
    disk_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) Force version update if existing pods are unable to be drained due to a pod disruption bu
    dget issue.
    """
    force_update_version: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Identifier of the EC2 Launch Template. Conflicts with `name`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) List of instance types associated with the EKS Node Group. Defaults to `["t3.medium"]`. T
    erraform will only perform drift detection if a configuration value is provided.
    """
    instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are man
    aged by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
    """
    labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) Configuration block with Launch Template settings. Detailed below.
    """
    launch_template: LaunchTemplate | None = core.attr(LaunchTemplate, default=None)

    node_group_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    node_group_name_prefix: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    node_role_arn: str | core.StringOut = core.attr(str)

    release_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block with remote access settings. Detailed below.
    """
    remote_access: RemoteAccess | None = core.attr(RemoteAccess, default=None)

    """
    List of objects containing information about underlying resources.
    """
    resources: list[Resources] | core.ArrayOut[Resources] = core.attr(
        Resources, computed=True, kind=core.Kind.array
    )

    """
    (Required) Configuration block with scaling settings. Detailed below.
    """
    scaling_config: ScalingConfig = core.attr(ScalingConfig)

    """
    Status of the EKS Node Group.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) The Kubernetes taints to be applied to the nodes in the node group. Maximum of 50 taints
    per node group. Detailed below.
    """
    taint: list[Taint] | core.ArrayOut[Taint] | None = core.attr(
        Taint, default=None, kind=core.Kind.array
    )

    update_config: UpdateConfig | None = core.attr(UpdateConfig, default=None, computed=True)

    """
    (Required) EC2 Launch Template version number. While the API accepts values like `$Default` and `$La
    test`, the API will convert the value to the associated version number (e.g., `1`) on read and Terra
    form will show a difference on next plan. Using the `default_version` or `latest_version` attribute
    of the `aws_launch_template` resource or data source is recommended for this argument.
    """
    version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: str | core.StringOut,
        node_role_arn: str | core.StringOut,
        scaling_config: ScalingConfig,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        ami_type: str | core.StringOut | None = None,
        capacity_type: str | core.StringOut | None = None,
        disk_size: int | core.IntOut | None = None,
        force_update_version: bool | core.BoolOut | None = None,
        instance_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        labels: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        launch_template: LaunchTemplate | None = None,
        node_group_name: str | core.StringOut | None = None,
        node_group_name_prefix: str | core.StringOut | None = None,
        release_version: str | core.StringOut | None = None,
        remote_access: RemoteAccess | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        taint: list[Taint] | core.ArrayOut[Taint] | None = None,
        update_config: UpdateConfig | None = None,
        version: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=NodeGroup.Args(
                cluster_name=cluster_name,
                node_role_arn=node_role_arn,
                scaling_config=scaling_config,
                subnet_ids=subnet_ids,
                ami_type=ami_type,
                capacity_type=capacity_type,
                disk_size=disk_size,
                force_update_version=force_update_version,
                instance_types=instance_types,
                labels=labels,
                launch_template=launch_template,
                node_group_name=node_group_name,
                node_group_name_prefix=node_group_name_prefix,
                release_version=release_version,
                remote_access=remote_access,
                tags=tags,
                tags_all=tags_all,
                taint=taint,
                update_config=update_config,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ami_type: str | core.StringOut | None = core.arg(default=None)

        capacity_type: str | core.StringOut | None = core.arg(default=None)

        cluster_name: str | core.StringOut = core.arg()

        disk_size: int | core.IntOut | None = core.arg(default=None)

        force_update_version: bool | core.BoolOut | None = core.arg(default=None)

        instance_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        launch_template: LaunchTemplate | None = core.arg(default=None)

        node_group_name: str | core.StringOut | None = core.arg(default=None)

        node_group_name_prefix: str | core.StringOut | None = core.arg(default=None)

        node_role_arn: str | core.StringOut = core.arg()

        release_version: str | core.StringOut | None = core.arg(default=None)

        remote_access: RemoteAccess | None = core.arg(default=None)

        scaling_config: ScalingConfig = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        taint: list[Taint] | core.ArrayOut[Taint] | None = core.arg(default=None)

        update_config: UpdateConfig | None = core.arg(default=None)

        version: str | core.StringOut | None = core.arg(default=None)
