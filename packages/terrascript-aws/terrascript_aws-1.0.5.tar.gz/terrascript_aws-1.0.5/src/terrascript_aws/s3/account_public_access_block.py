import terrascript.core as core


@core.resource(type="aws_s3_account_public_access_block", namespace="s3")
class AccountPublicAccessBlock(core.Resource):
    """
    (Optional) AWS account ID to configure. Defaults to automatically determined account ID of the Terra
    form AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `fals
    e`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the f
    ollowing behavior:
    """
    block_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether Amazon S3 should block public bucket policies for buckets in this account. Defaul
    ts to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` ca
    uses Amazon S3 to:
    """
    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    AWS account ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `fal
    se`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent
    new public ACLs from being set. When set to `true` causes Amazon S3 to:
    """
    ignore_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Whether Amazon S3 should restrict public bucket policies for buckets in this account. Def
    aults to `false`. Enabling this setting does not affect previously stored bucket policies, except th
    at public and cross-account access within any public bucket policy, including non-public delegation
    to specific accounts, is blocked. When set to `true`:
    """
    restrict_public_buckets: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: str | core.StringOut | None = None,
        block_public_acls: bool | core.BoolOut | None = None,
        block_public_policy: bool | core.BoolOut | None = None,
        ignore_public_acls: bool | core.BoolOut | None = None,
        restrict_public_buckets: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccountPublicAccessBlock.Args(
                account_id=account_id,
                block_public_acls=block_public_acls,
                block_public_policy=block_public_policy,
                ignore_public_acls=ignore_public_acls,
                restrict_public_buckets=restrict_public_buckets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        block_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        block_public_policy: bool | core.BoolOut | None = core.arg(default=None)

        ignore_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        restrict_public_buckets: bool | core.BoolOut | None = core.arg(default=None)
