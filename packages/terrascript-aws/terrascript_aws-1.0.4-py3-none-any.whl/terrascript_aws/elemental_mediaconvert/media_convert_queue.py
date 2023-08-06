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


@core.resource(type="aws_media_convert_queue", namespace="elemental_mediaconvert")
class MediaConvertQueue(core.Resource):
    """
    The Arn of the queue
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A description of the queue
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The same as `name`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A unique identifier describing the queue
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Specifies whether the pricing plan for the queue is on-demand or reserved. Valid values a
    re `ON_DEMAND` or `RESERVED`. Default to `ON_DEMAND`.
    """
    pricing_plan: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A detail pricing plan of the  reserved queue. See below.
    """
    reservation_plan_settings: ReservationPlanSettings | None = core.attr(
        ReservationPlanSettings, default=None, computed=True
    )

    """
    (Optional) A status of the queue. Valid values are `ACTIVE` or `RESERVED`. Default to `PAUSED`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

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
    configuration-block).
    """
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
