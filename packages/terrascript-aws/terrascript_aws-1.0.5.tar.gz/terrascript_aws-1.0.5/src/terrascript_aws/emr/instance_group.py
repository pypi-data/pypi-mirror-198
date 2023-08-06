import terrascript.core as core


@core.schema
class EbsConfig(core.Schema):

    iops: int | core.IntOut | None = core.attr(int, default=None)

    size: int | core.IntOut = core.attr(int)

    type: str | core.StringOut = core.attr(str)

    volumes_per_instance: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: int | core.IntOut,
        type: str | core.StringOut,
        iops: int | core.IntOut | None = None,
        volumes_per_instance: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=EbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: int | core.IntOut | None = core.arg(default=None)

        size: int | core.IntOut = core.arg()

        type: str | core.StringOut = core.arg()

        volumes_per_instance: int | core.IntOut | None = core.arg(default=None)


@core.resource(type="aws_emr_instance_group", namespace="emr")
class InstanceGroup(core.Resource):
    """
    (Optional) The autoscaling policy document. This is a JSON formatted string. See [EMR Auto Scaling](
    https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html)
    """

    autoscaling_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) If set, the bid price for each EC2 instance in the instance group, expressed in USD. By s
    etting this attribute, the instance group is being declared as a Spot Instance, and will implicitly
    create a Spot request. Leave this blank to use On-Demand Instances.
    """
    bid_price: str | core.StringOut | None = core.attr(str, default=None)

    cluster_id: str | core.StringOut = core.attr(str)

    """
    (Optional) A JSON string for supplying list of configurations specific to the EMR instance group. No
    te that this can only be changed when using EMR release 5.21 or later.
    """
    configurations_json: str | core.StringOut | None = core.attr(str, default=None)

    ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = core.attr(
        EbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The EMR Instance ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    instance_count: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    instance_type: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    running_instance_count: int | core.IntOut = core.attr(int, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: str | core.StringOut,
        instance_type: str | core.StringOut,
        autoscaling_policy: str | core.StringOut | None = None,
        bid_price: str | core.StringOut | None = None,
        configurations_json: str | core.StringOut | None = None,
        ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = None,
        ebs_optimized: bool | core.BoolOut | None = None,
        instance_count: int | core.IntOut | None = None,
        name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceGroup.Args(
                cluster_id=cluster_id,
                instance_type=instance_type,
                autoscaling_policy=autoscaling_policy,
                bid_price=bid_price,
                configurations_json=configurations_json,
                ebs_config=ebs_config,
                ebs_optimized=ebs_optimized,
                instance_count=instance_count,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_policy: str | core.StringOut | None = core.arg(default=None)

        bid_price: str | core.StringOut | None = core.arg(default=None)

        cluster_id: str | core.StringOut = core.arg()

        configurations_json: str | core.StringOut | None = core.arg(default=None)

        ebs_config: list[EbsConfig] | core.ArrayOut[EbsConfig] | None = core.arg(default=None)

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        instance_count: int | core.IntOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)
