import terrascript.core as core


@core.resource(type="aws_route53_key_signing_key", namespace="route53")
class KeySigningKey(core.Resource):
    """
    A string used to represent the delegation signer digest algorithm. This value must follow the guidel
    ines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3).
    """

    digest_algorithm_mnemonic: str | core.StringOut = core.attr(str, computed=True)

    """
    An integer used to represent the delegation signer digest algorithm. This value must follow the guid
    elines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3).
    """
    digest_algorithm_type: int | core.IntOut = core.attr(int, computed=True)

    """
    A cryptographic digest of a DNSKEY resource record (RR). DNSKEY records are used to publish the publ
    ic key that resolvers can use to verify DNSSEC signatures that are used to secure certain kinds of i
    nformation provided by the DNS system.
    """
    digest_value: str | core.StringOut = core.attr(str, computed=True)

    """
    A string that represents a DNSKEY record.
    """
    dnskey_record: str | core.StringOut = core.attr(str, computed=True)

    """
    A string that represents a delegation signer (DS) record.
    """
    ds_record: str | core.StringOut = core.attr(str, computed=True)

    """
    An integer that specifies how the key is used. For key-signing key (KSK), this value is always 257.
    """
    flag: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Identifier of the Route 53 Hosted Zone.
    """
    hosted_zone_id: str | core.StringOut = core.attr(str)

    """
    Route 53 Hosted Zone identifier and KMS Key identifier, separated by a comma (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the Key Management Service (KMS) Key. This must be unique f
    or each key-signing key (KSK) in a single hosted zone. This key must be in the `us-east-1` Region an
    d meet certain requirements, which are described in the [Route 53 Developer Guide](https://docs.aws.
    amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-cmk-requirements.html) and [Route 53
    API Reference](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateKeySigningKey.html
    ).
    """
    key_management_service_arn: str | core.StringOut = core.attr(str)

    """
    An integer used to identify the DNSSEC record for the domain name. The process used to calculate the
    value is described in [RFC-4034 Appendix B](https://tools.ietf.org/rfc/rfc4034.txt).
    """
    key_tag: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Name of the key-signing key (KSK). Must be unique for each key-singing key in the same ho
    sted zone.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The public key, represented as a Base64 encoding, as required by [RFC-4034 Page 5](https://tools.iet
    f.org/rfc/rfc4034.txt).
    """
    public_key: str | core.StringOut = core.attr(str, computed=True)

    """
    A string used to represent the signing algorithm. This value must follow the guidelines provided by
    [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1).
    """
    signing_algorithm_mnemonic: str | core.StringOut = core.attr(str, computed=True)

    """
    An integer used to represent the signing algorithm. This value must follow the guidelines provided b
    y [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1).
    """
    signing_algorithm_type: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Status of the key-signing key (KSK). Valid values: `ACTIVE`, `INACTIVE`. Defaults to `ACT
    IVE`.
    """
    status: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: str | core.StringOut,
        key_management_service_arn: str | core.StringOut,
        name: str | core.StringOut,
        status: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeySigningKey.Args(
                hosted_zone_id=hosted_zone_id,
                key_management_service_arn=key_management_service_arn,
                name=name,
                status=status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: str | core.StringOut = core.arg()

        key_management_service_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        status: str | core.StringOut | None = core.arg(default=None)
