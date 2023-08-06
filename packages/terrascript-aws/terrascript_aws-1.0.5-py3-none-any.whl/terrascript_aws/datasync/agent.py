import terrascript.core as core


@core.resource(type="aws_datasync_agent", namespace="datasync")
class Agent(core.Resource):
    """
    (Optional) DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If a
    n `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the reso
    urce creation.
    """

    activation_key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the DataSync Agent.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the DataSync Agent.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) DataSync Agent IP address to retrieve activation key during resource creation. Conflicts
    with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
    """
    ip_address: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) Name of the DataSync Agent.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The IP address of the VPC endpoint the agent should connect to when retrieving an activat
    ion key during resource creation. Conflicts with `activation_key`.
    """
    private_link_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ARNs of the security groups used to protect your data transfer task subnets.
    """
    security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The Amazon Resource Names (ARNs) of the subnets in which DataSync will create elastic net
    work interfaces for each data transfer task.
    """
    subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Key-value pairs of resource tags to assign to the DataSync Agent. If configured with a pr
    ovider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/la
    test/docs#default_tags-configuration-block) present, tags with matching keys will overwrite those de
    fined at the provider-level.
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
    (Optional) The ID of the VPC (virtual private cloud) endpoint that the agent has access to.
    """
    vpc_endpoint_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        activation_key: str | core.StringOut | None = None,
        ip_address: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        private_link_endpoint: str | core.StringOut | None = None,
        security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_endpoint_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Agent.Args(
                activation_key=activation_key,
                ip_address=ip_address,
                name=name,
                private_link_endpoint=private_link_endpoint,
                security_group_arns=security_group_arns,
                subnet_arns=subnet_arns,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_id=vpc_endpoint_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activation_key: str | core.StringOut | None = core.arg(default=None)

        ip_address: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        private_link_endpoint: str | core.StringOut | None = core.arg(default=None)

        security_group_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_endpoint_id: str | core.StringOut | None = core.arg(default=None)
