import terrascript.core as core


@core.data(type="aws_rds_certificate", namespace="rds")
class DsCertificate(core.Data):
    """
    Amazon Resource Name (ARN) of the certificate.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Type of certificate. For example, `CA`.
    """
    certificate_type: str | core.StringOut = core.attr(str, computed=True)

    """
    Boolean whether there is an override for the default certificate identifier.
    """
    customer_override: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    If there is an override for the default certificate identifier, when the override expires.
    """
    customer_override_valid_till: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Certificate identifier. For example, `rds-ca-2019`.
    """
    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) When enabled, returns the certificate with the latest `ValidTill`.
    """
    latest_valid_till: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Thumbprint of the certificate.
    """
    thumbprint: str | core.StringOut = core.attr(str, computed=True)

    """
    [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of certificate starting validity d
    ate.
    """
    valid_from: str | core.StringOut = core.attr(str, computed=True)

    """
    [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) of certificate ending validity dat
    e.
    """
    valid_till: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: str | core.StringOut | None = None,
        latest_valid_till: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                id=id,
                latest_valid_till=latest_valid_till,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut | None = core.arg(default=None)

        latest_valid_till: bool | core.BoolOut | None = core.arg(default=None)
