import terrascript.core as core


@core.data(type="aws_s3_account_public_access_block", namespace="s3")
class DsAccountPublicAccessBlock(core.Data):
    """
    (Optional) AWS account ID to configure. Defaults to automatically determined account ID of the Terra
    form AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Whether or not Amazon S3 should block public ACLs for buckets in this account is enabled. Returns as
    true` or `false`.
    """
    block_public_acls: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether or not Amazon S3 should block public bucket policies for buckets in this account is enabled.
    Returns as `true` or `false`.
    """
    block_public_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    AWS account ID
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether or not Amazon S3 should ignore public ACLs for buckets in this account is enabled. Returns a
    s `true` or `false`.
    """
    ignore_public_acls: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    Whether or not Amazon S3 should restrict public bucket policies for buckets in this account is enabl
    ed. Returns as `true` or `false`.
    """
    restrict_public_buckets: bool | core.BoolOut = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        account_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAccountPublicAccessBlock.Args(
                account_id=account_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut | None = core.arg(default=None)
