import terrascript.core as core


@core.data(type="aws_caller_identity", namespace="sts")
class DsCallerIdentity(core.Data):
    """
    AWS Account ID number of the account that owns or contains the calling entity.
    """

    account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    ARN associated with the calling entity.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Account ID number of the account that owns or contains the calling entity.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Unique identifier of the calling entity.
    """
    user_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsCallerIdentity.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
