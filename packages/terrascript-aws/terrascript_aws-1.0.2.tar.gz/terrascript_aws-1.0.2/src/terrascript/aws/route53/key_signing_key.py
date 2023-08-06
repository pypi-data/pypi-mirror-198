import terrascript.core as core


@core.resource(type="aws_route53_key_signing_key", namespace="aws_route53")
class KeySigningKey(core.Resource):

    digest_algorithm_mnemonic: str | core.StringOut = core.attr(str, computed=True)

    digest_algorithm_type: int | core.IntOut = core.attr(int, computed=True)

    digest_value: str | core.StringOut = core.attr(str, computed=True)

    dnskey_record: str | core.StringOut = core.attr(str, computed=True)

    ds_record: str | core.StringOut = core.attr(str, computed=True)

    flag: int | core.IntOut = core.attr(int, computed=True)

    hosted_zone_id: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_management_service_arn: str | core.StringOut = core.attr(str)

    key_tag: int | core.IntOut = core.attr(int, computed=True)

    name: str | core.StringOut = core.attr(str)

    public_key: str | core.StringOut = core.attr(str, computed=True)

    signing_algorithm_mnemonic: str | core.StringOut = core.attr(str, computed=True)

    signing_algorithm_type: int | core.IntOut = core.attr(int, computed=True)

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
