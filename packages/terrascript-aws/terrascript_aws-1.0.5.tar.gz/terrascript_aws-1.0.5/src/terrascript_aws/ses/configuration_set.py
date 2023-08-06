import terrascript.core as core


@core.schema
class TrackingOptions(core.Schema):

    custom_redirect_domain: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        custom_redirect_domain: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TrackingOptions.Args(
                custom_redirect_domain=custom_redirect_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_redirect_domain: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DeliveryOptions(core.Schema):

    tls_policy: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        tls_policy: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeliveryOptions.Args(
                tls_policy=tls_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tls_policy: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ses_configuration_set", namespace="ses")
class ConfigurationSet(core.Resource):
    """
    SES configuration set ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether messages that use the configuration set are required to use TLS. See below.
    """
    delivery_options: DeliveryOptions | None = core.attr(DeliveryOptions, default=None)

    """
    SES configuration set name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Date and time at which the reputation metrics for the configuration set were last reset. Resetting t
    hese metrics is known as a fresh start.
    """
    last_fresh_start: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of the configuration set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Whether or not Amazon SES publishes reputation metrics for the configuration set, such as
    bounce and complaint rates, to Amazon CloudWatch. The default value is `false`.
    """
    reputation_metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether email sending is enabled or disabled for the configuration set. The default value
    is `true`.
    """
    sending_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Domain that is used to redirect email recipients to an Amazon SES-operated domain. See be
    low. **NOTE:** This functionality is best effort.
    """
    tracking_options: TrackingOptions | None = core.attr(TrackingOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        delivery_options: DeliveryOptions | None = None,
        reputation_metrics_enabled: bool | core.BoolOut | None = None,
        sending_enabled: bool | core.BoolOut | None = None,
        tracking_options: TrackingOptions | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationSet.Args(
                name=name,
                delivery_options=delivery_options,
                reputation_metrics_enabled=reputation_metrics_enabled,
                sending_enabled=sending_enabled,
                tracking_options=tracking_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delivery_options: DeliveryOptions | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        reputation_metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        sending_enabled: bool | core.BoolOut | None = core.arg(default=None)

        tracking_options: TrackingOptions | None = core.arg(default=None)
