import terrascript.core as core


@core.resource(type="aws_kms_alias", namespace="kms")
class Alias(core.Resource):
    """
    The Amazon Resource Name (ARN) of the key alias.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The display name of the alias. The name must start with the word "alias" followed by a fo
    rward slash (alias/)
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates an unique alias beginning with the specified prefix.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The Amazon Resource Name (ARN) of the target key identifier.
    """
    target_key_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Identifier for the key for which the alias is for, can be either an ARN or key_id.
    """
    target_key_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        target_key_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Alias.Args(
                target_key_id=target_key_id,
                name=name,
                name_prefix=name_prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        target_key_id: str | core.StringOut = core.arg()
