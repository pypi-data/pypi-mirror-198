import terrascript.core as core


@core.resource(type="aws_iam_virtual_mfa_device", namespace="iam")
class VirtualMfaDevice(core.Resource):
    """
    The Amazon Resource Name (ARN) specifying the virtual mfa device.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `bas
    e_32_string_seed` is base64-encoded.
    """
    base_32_string_seed: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut | None = core.attr(str, default=None)

    """
    A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32S
    tring` where `$virtualMFADeviceName` is one of the create call arguments. AccountName is the user na
    me if set (otherwise, the account ID otherwise), and Base32String is the seed in base32 format.
    """
    qr_code_png: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Map of resource tags for the virtual mfa device. If configured with a provider [`default_
    tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default
    _tags-configuration-block) present, tags with matching keys will overwrite those defined at the prov
    ider-level.
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
    (Required) The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA devi
    ce.
    """
    virtual_mfa_device_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        virtual_mfa_device_name: str | core.StringOut,
        path: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualMfaDevice.Args(
                virtual_mfa_device_name=virtual_mfa_device_name,
                path=path,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        path: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        virtual_mfa_device_name: str | core.StringOut = core.arg()
