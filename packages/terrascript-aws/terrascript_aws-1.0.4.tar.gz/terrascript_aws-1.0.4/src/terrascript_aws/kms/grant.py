import terrascript.core as core


@core.schema
class Constraints(core.Schema):

    encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Constraints.Args(
                encryption_context_equals=encryption_context_equals,
                encryption_context_subset=encryption_context_subset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_context_equals: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )

        encryption_context_subset: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.resource(type="aws_kms_grant", namespace="kms")
class Grant(core.Resource):
    """
    (Optional, Forces new resources) A structure that you can use to allow certain operations in the gra
    nt only when the desired encryption context is present. For more information about encryption contex
    t, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.
    html).
    """

    constraints: list[Constraints] | core.ArrayOut[Constraints] | None = core.attr(
        Constraints, default=None, kind=core.Kind.array
    )

    """
    (Optional, Forces new resources) A list of grant tokens to be used when creating the grant. See [Gra
    nt Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more
    information about grant tokens.
    """
    grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The unique identifier for the grant.
    """
    grant_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amaz
    on.com/kms/latest/developerguide/concepts.html#grant_token).
    """
    grant_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resources) The principal that is given permission to perform the operations th
    at the grant permits in ARN format. Note that due to eventual consistency issues around IAM principa
    ls, terraform's state may not always be refreshed to reflect what is true in AWS.
    """
    grantee_principal: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resources) The unique identifier for the customer master key (CMK) that the gr
    ant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in
    a different AWS account, you must use the key ARN.
    """
    key_id: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resources) A friendly name for identifying the grant.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, Forces new resources) A list of operations that the grant permits. The permitted values a
    re: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `Re
    EncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `Generate
    DataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
    """
    operations: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    retire_on_delete: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Forces new resources) The principal that is given permission to retire the grant by using
    RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM princi
    pals, terraform's state may not always be refreshed to reflect what is true in AWS.
    """
    retiring_principal: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        grantee_principal: str | core.StringOut,
        key_id: str | core.StringOut,
        operations: list[str] | core.ArrayOut[core.StringOut],
        constraints: list[Constraints] | core.ArrayOut[Constraints] | None = None,
        grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = None,
        name: str | core.StringOut | None = None,
        retire_on_delete: bool | core.BoolOut | None = None,
        retiring_principal: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Grant.Args(
                grantee_principal=grantee_principal,
                key_id=key_id,
                operations=operations,
                constraints=constraints,
                grant_creation_tokens=grant_creation_tokens,
                name=name,
                retire_on_delete=retire_on_delete,
                retiring_principal=retiring_principal,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        constraints: list[Constraints] | core.ArrayOut[Constraints] | None = core.arg(default=None)

        grant_creation_tokens: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        grantee_principal: str | core.StringOut = core.arg()

        key_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        operations: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        retire_on_delete: bool | core.BoolOut | None = core.arg(default=None)

        retiring_principal: str | core.StringOut | None = core.arg(default=None)
