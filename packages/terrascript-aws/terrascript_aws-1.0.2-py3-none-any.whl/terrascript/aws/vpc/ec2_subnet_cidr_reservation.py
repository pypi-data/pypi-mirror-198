import terrascript.core as core


@core.resource(type="aws_ec2_subnet_cidr_reservation", namespace="aws_vpc")
class Ec2SubnetCidrReservation(core.Resource):

    cidr_block: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    reservation_type: str | core.StringOut = core.attr(str)

    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cidr_block: str | core.StringOut,
        reservation_type: str | core.StringOut,
        subnet_id: str | core.StringOut,
        description: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2SubnetCidrReservation.Args(
                cidr_block=cidr_block,
                reservation_type=reservation_type,
                subnet_id=subnet_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_block: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        reservation_type: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()
