import terrascript.core as core


@core.resource(type="aws_ebs_default_kms_key", namespace="aws_ebs")
class DefaultKmsKey(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    key_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key_arn: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultKmsKey.Args(
                key_arn=key_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_arn: str | core.StringOut = core.arg()
