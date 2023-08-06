import terrascript.core as core


@core.data(type="aws_rds_certificate", namespace="aws_rds")
class DsCertificate(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate_type: str | core.StringOut = core.attr(str, computed=True)

    customer_override: bool | core.BoolOut = core.attr(bool, computed=True)

    customer_override_valid_till: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    latest_valid_till: bool | core.BoolOut | None = core.attr(bool, default=None)

    thumbprint: str | core.StringOut = core.attr(str, computed=True)

    valid_from: str | core.StringOut = core.attr(str, computed=True)

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
