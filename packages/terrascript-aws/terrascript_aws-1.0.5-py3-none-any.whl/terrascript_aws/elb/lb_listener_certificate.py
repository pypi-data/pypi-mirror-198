import terrascript.core as core


@core.resource(type="aws_lb_listener_certificate", namespace="elb")
class LbListenerCertificate(core.Resource):
    """
    (Required, Forces New Resource) The ARN of the certificate to attach to the listener.
    """

    certificate_arn: str | core.StringOut = core.attr(str)

    """
    The `listener_arn` and `certificate_arn` separated by a `_`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces New Resource) The ARN of the listener to which to attach the certificate.
    """
    listener_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_arn: str | core.StringOut,
        listener_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbListenerCertificate.Args(
                certificate_arn=certificate_arn,
                listener_arn=listener_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: str | core.StringOut = core.arg()

        listener_arn: str | core.StringOut = core.arg()
