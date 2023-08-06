import terrascript.core as core


@core.data(type="aws_acm_certificate", namespace="acm")
class DsCertificate(core.Data):
    """
    Amazon Resource Name (ARN) of the found certificate, suitable for referencing in other resources tha
    t support ACM certificates.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The ACM-issued certificate.
    """
    certificate: str | core.StringOut = core.attr(str, computed=True)

    """
    Certificates forming the requested ACM-issued certificate's chain of trust. The chain consists of th
    e certificate of the issuing CA and the intermediate certificates of any other subordinate CAs.
    """
    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The domain of the certificate to look up. If no certificate is found with this name, an e
    rror will be returned.
    """
    domain: str | core.StringOut = core.attr(str)

    """
    Amazon Resource Name (ARN) of the found certificate, suitable for referencing in other resources tha
    t support ACM certificates.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of key algorithms to filter certificates. By default, ACM does not return all cert
    ificate types when searching. See the [ACM API Reference](https://docs.aws.amazon.com/acm/latest/API
    Reference/API_CertificateDetail.html#ACM-Type-CertificateDetail-KeyAlgorithm) for supported key algo
    rithms.
    """
    key_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) If set to true, it sorts the certificates matched by previous criteria by the NotBefore f
    ield, returning only the most recent one. If set to false, it returns an error if more than one cert
    ificate is found. Defaults to false.
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    Status of the found certificate.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A list of statuses on which to filter the returned list. Valid values are `PENDING_VALIDA
    TION`, `ISSUED`,
    """
    statuses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    A mapping of tags for the resource.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) A list of types on which to filter the returned list. Valid values are `AMAZON_ISSUED` an
    d `IMPORTED`.
    """
    types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain: str | core.StringOut,
        key_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        statuses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                domain=domain,
                key_types=key_types,
                most_recent=most_recent,
                statuses=statuses,
                tags=tags,
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()

        key_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        statuses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
