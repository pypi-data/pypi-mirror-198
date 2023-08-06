import terrascript.core as core


@core.resource(type="aws_route53_vpc_association_authorization", namespace="route53")
class VpcAssociationAuthorization(core.Resource):
    """
    The calculated unique identifier for the association.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The VPC to authorize for association with the private hosted zone.
    """
    vpc_id: str | core.StringOut = core.attr(str)

    """
    (Optional) The VPC's region. Defaults to the region of the AWS provider.
    """
    vpc_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The ID of the private hosted zone that you want to authorize associating a VPC with.
    """
    zone_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: str | core.StringOut,
        zone_id: str | core.StringOut,
        vpc_region: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VpcAssociationAuthorization.Args(
                vpc_id=vpc_id,
                zone_id=zone_id,
                vpc_region=vpc_region,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_id: str | core.StringOut = core.arg()

        vpc_region: str | core.StringOut | None = core.arg(default=None)

        zone_id: str | core.StringOut = core.arg()
