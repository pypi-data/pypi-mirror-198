import terrascript.core as core


@core.data(type="aws_ssm_parameter", namespace="ssm")
class DsParameter(core.Data):
    """
    The ARN of the parameter.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the parameter.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    The value of the parameter. This value is always marked as sensitive in the Terraform plan output, r
    egardless of `type`. In Terraform CLI version 0.15 and later, this may require additional configurat
    ion handling for certain scenarios. For more information, see the [Terraform v0.15 Upgrade Guide](ht
    tps://www.terraform.io/upgrade-guides/0-15.html#sensitive-output-values).
    """
    value: str | core.StringOut = core.attr(str, computed=True)

    """
    The version of the parameter.
    """
    version: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Whether to return decrypted `SecureString` value. Defaults to `true`.
    """
    with_decryption: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        with_decryption: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsParameter.Args(
                name=name,
                with_decryption=with_decryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        with_decryption: bool | core.BoolOut | None = core.arg(default=None)
