import terrascript.core as core


@core.resource(type="aws_xray_encryption_config", namespace="x_ray")
class XrayEncryptionConfig(core.Resource):
    """
    Region name.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An AWS KMS customer master key (CMK) ARN.
    """
    key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` fo
    r default encryption.
    """
    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: str | core.StringOut,
        key_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=XrayEncryptionConfig.Args(
                type=type,
                key_id=key_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_id: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()
