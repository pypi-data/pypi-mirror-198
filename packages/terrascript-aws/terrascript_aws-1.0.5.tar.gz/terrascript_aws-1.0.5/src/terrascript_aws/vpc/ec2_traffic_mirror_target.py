import terrascript.core as core


@core.resource(type="aws_ec2_traffic_mirror_target", namespace="vpc")
class Ec2TrafficMirrorTarget(core.Resource):
    """
    The ARN of the traffic mirror target.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new) A description of the traffic mirror session.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the Traffic Mirror target.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new) The network interface ID that is associated with the target.
    """
    network_interface_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new) The Amazon Resource Name (ARN) of the Network Load Balancer that is associate
    d with the target.
    """
    network_load_balancer_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the AWS account that owns the traffic mirror target.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

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

    def __init__(
        self,
        resource_name: str,
        *,
        description: str | core.StringOut | None = None,
        network_interface_id: str | core.StringOut | None = None,
        network_load_balancer_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorTarget.Args(
                description=description,
                network_interface_id=network_interface_id,
                network_load_balancer_arn=network_load_balancer_arn,
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

        network_interface_id: str | core.StringOut | None = core.arg(default=None)

        network_load_balancer_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
