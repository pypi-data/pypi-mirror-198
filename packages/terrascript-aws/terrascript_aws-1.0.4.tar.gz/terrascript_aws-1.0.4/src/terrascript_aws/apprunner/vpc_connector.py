import terrascript.core as core


@core.resource(type="aws_apprunner_vpc_connector", namespace="apprunner")
class VpcConnector(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    A list of IDs of security groups that App Runner should use for access to AWS resources under the sp
    ecified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The
    default security group allows all outbound traffic.
    """
    security_groups: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    The current state of the VPC connector. If the status of a connector revision is INACTIVE, it was de
    leted and can't be used. Inactive connector revisions are permanently removed some time after they a
    re deleted.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) A name for the VPC connector.
    """
    vpc_connector_name: str | core.StringOut = core.attr(str)

    """
    The revision of VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that
    share the same Name.
    """
    vpc_connector_revision: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        security_groups: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
        vpc_connector_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcConnector.Args(
                security_groups=security_groups,
                subnets=subnets,
                vpc_connector_name=vpc_connector_name,
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        security_groups: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_connector_name: str | core.StringOut = core.arg()
