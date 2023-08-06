import terrascript.core as core


@core.resource(type="aws_ec2_capacity_reservation", namespace="aws_ec2")
class CapacityReservation(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str)

    ebs_optimized: bool | core.BoolOut | None = core.attr(bool, default=None)

    end_date: str | core.StringOut | None = core.attr(str, default=None)

    end_date_type: str | core.StringOut | None = core.attr(str, default=None)

    ephemeral_storage: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_count: int | core.IntOut = core.attr(int)

    instance_match_criteria: str | core.StringOut | None = core.attr(str, default=None)

    instance_platform: str | core.StringOut = core.attr(str)

    instance_type: str | core.StringOut = core.attr(str)

    outpost_arn: str | core.StringOut | None = core.attr(str, default=None)

    owner_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

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
