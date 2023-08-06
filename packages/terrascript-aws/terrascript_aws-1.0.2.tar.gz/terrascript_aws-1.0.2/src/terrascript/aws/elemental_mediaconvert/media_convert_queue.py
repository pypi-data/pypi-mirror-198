import terrascript.core as core


@core.schema
class ReservationPlanSettings(core.Schema):

    commitment: str | core.StringOut = core.attr(str)

    renewal_type: str | core.StringOut = core.attr(str)

    reserved_slots: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        commitment: str | core.StringOut,
        renewal_type: str | core.StringOut,
        reserved_slots: int | core.IntOut,
    ):
        super().__init__(
            args=ReservationPlanSettings.Args(
                commitment=commitment,
                renewal_type=renewal_type,
                reserved_slots=reserved_slots,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        commitment: str | core.StringOut = core.arg()

        renewal_type: str | core.StringOut = core.arg()

        reserved_slots: int | core.IntOut = core.arg()


@core.resource(type="aws_media_convert_queue", namespace="aws_elemental_mediaconvert")
class MediaConvertQueue(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    pricing_plan: str | core.StringOut | None = core.attr(str, default=None)

    reservation_plan_settings: ReservationPlanSettings | None = core.attr(
        ReservationPlanSettings, default=None, computed=True
    )

    status: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        pricing_plan: str | core.StringOut | None = None,
        reservation_plan_settings: ReservationPlanSettings | None = None,
        status: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaConvertQueue.Args(
                name=name,
                description=description,
                pricing_plan=pricing_plan,
                reservation_plan_settings=reservation_plan_settings,
                status=status,
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

        name: str | core.StringOut = core.arg()

        pricing_plan: str | core.StringOut | None = core.arg(default=None)

        reservation_plan_settings: ReservationPlanSettings | None = core.arg(default=None)

        status: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
