import terrascript.core as core


@core.resource(type="aws_ec2_capacity_reservation", namespace="ec2")
class CapacityReservation(core.Resource):
    """
    The ARN of the Capacity Reservation.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The Availability Zone in which to create the Capacity Reservation.
    """
    availability_zone: str | core.StringOut = core.attr(str)

    """
    (Optional) Indicates whether the Capacity Reservation supports EBS-optimized instances.
    """
    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The date and time at which the Capacity Reservation expires. When a Capacity Reservation
    expires, the reserved capacity is released and you can no longer launch instances into it. Valid val
    ues: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`)
    """
    end_date: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `
    limited`.
    """
    end_date_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Indicates whether the Capacity Reservation supports instances with temporary, block-level
    storage.
    """
    ephemeral_storage: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The Capacity Reservation ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The number of instances for which to reserve capacity.
    """
    instance_count: int | core.IntOut = core.attr(int)

    """
    (Optional) Indicates the type of instance launches that the Capacity Reservation accepts. Specify ei
    ther `open` or `targeted`.
    """
    instance_match_criteria: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX
    , `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL
    Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.
    """
    instance_platform: str | core.StringOut = core.attr(str)

    """
    (Required) The instance type for which to reserve capacity.
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The Amazon Resource Name (ARN) of the Outpost on which to create the Capacity Reservation
    .
    """
    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the AWS account that owns the Capacity Reservation.
    """
    owner_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block)
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated
    .
    """
    tenancy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: str | core.StringOut,
        instance_count: int | core.IntOut,
        instance_platform: str | core.StringOut,
        instance_type: str | core.StringOut,
        ebs_optimized: bool | core.BoolOut | None = None,
        end_date: str | core.StringOut | None = None,
        end_date_type: str | core.StringOut | None = None,
        ephemeral_storage: bool | core.BoolOut | None = None,
        instance_match_criteria: str | core.StringOut | None = None,
        outpost_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tenancy: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=CapacityReservation.Args(
                availability_zone=availability_zone,
                instance_count=instance_count,
                instance_platform=instance_platform,
                instance_type=instance_type,
                ebs_optimized=ebs_optimized,
                end_date=end_date,
                end_date_type=end_date_type,
                ephemeral_storage=ephemeral_storage,
                instance_match_criteria=instance_match_criteria,
                outpost_arn=outpost_arn,
                tags=tags,
                tags_all=tags_all,
                tenancy=tenancy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: str | core.StringOut = core.arg()

        ebs_optimized: bool | core.BoolOut | None = core.arg(default=None)

        end_date: str | core.StringOut | None = core.arg(default=None)

        end_date_type: str | core.StringOut | None = core.arg(default=None)

        ephemeral_storage: bool | core.BoolOut | None = core.arg(default=None)

        instance_count: int | core.IntOut = core.arg()

        instance_match_criteria: str | core.StringOut | None = core.arg(default=None)

        instance_platform: str | core.StringOut = core.arg()

        instance_type: str | core.StringOut = core.arg()

        outpost_arn: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tenancy: str | core.StringOut | None = core.arg(default=None)
