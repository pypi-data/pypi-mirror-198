import terrascript.core as core


@core.resource(type="aws_ec2_availability_zone_group", namespace="ec2")
class AvailabilityZoneGroup(core.Resource):
    """
    (Required) Name of the Availability Zone Group.
    """

    group_name: str | core.StringOut = core.attr(str)

    """
    Name of the Availability Zone Group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Indicates whether to enable or disable Availability Zone Group. Valid values: `opted-in`
    or `not-opted-in`.
    """
    opt_in_status: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: str | core.StringOut,
        opt_in_status: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AvailabilityZoneGroup.Args(
                group_name=group_name,
                opt_in_status=opt_in_status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_name: str | core.StringOut = core.arg()

        opt_in_status: str | core.StringOut = core.arg()
