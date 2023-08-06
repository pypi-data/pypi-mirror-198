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


@core.resource(type="aws_ce_anomaly_subscription", namespace="ce")
class AnomalySubscription(core.Resource):
    """
    (Optional) The unique identifier for the AWS account in which the anomaly subscription ought to be c
    reated.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    ARN of the anomaly subscription.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The frequency that anomaly reports are sent. Valid Values: `DAILY` | `IMMEDIATE` | `WEEKL
    Y`.
    """
    frequency: str | core.StringOut = core.attr(str)

    """
    Unique ID of the anomaly subscription. Same as `arn`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A list of cost anomaly monitors.
    """
    monitor_arn_list: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Required) The name for the subscription.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A subscriber configuration. Multiple subscribers can be defined.
    """
    subscriber: list[Subscriber] | core.ArrayOut[Subscriber] = core.attr(
        Subscriber, kind=core.Kind.array
    )

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

    """
    (Required) The dollar value that triggers a notification if the threshold is exceeded.
    """
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
