import terrascript.core as core


@core.schema
class Subscriber(core.Schema):

    address: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        address: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=Subscriber.Args(
                address=address,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_ce_anomaly_subscription", namespace="aws_ce")
class AnomalySubscription(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    frequency: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    monitor_arn_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    subscriber: list[Subscriber] | core.ArrayOut[Subscriber] = core.attr(
        Subscriber, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    threshold: float | core.FloatOut = core.attr(float)

    def __init__(
        self,
        resource_name: str,
        *,
        frequency: str | core.StringOut,
        monitor_arn_list: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut,
        subscriber: list[Subscriber] | core.ArrayOut[Subscriber],
        threshold: float | core.FloatOut,
        account_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AnomalySubscription.Args(
                frequency=frequency,
                monitor_arn_list=monitor_arn_list,
                name=name,
                subscriber=subscriber,
                threshold=threshold,
                account_id=account_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        frequency: str | core.StringOut = core.arg()

        monitor_arn_list: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        name: str | core.StringOut = core.arg()

        subscriber: list[Subscriber] | core.ArrayOut[Subscriber] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        threshold: float | core.FloatOut = core.arg()
