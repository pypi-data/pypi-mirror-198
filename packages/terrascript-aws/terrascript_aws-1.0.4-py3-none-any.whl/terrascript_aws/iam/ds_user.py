import terrascript.core as core


@core.data(type="aws_iam_user", namespace="iam")
class DsUser(core.Data):
    """
    The Amazon Resource Name (ARN) assigned by AWS for this user.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Path in which this user was created.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the policy that is used to set the permissions boundary for the user.
    """
    permissions_boundary: str | core.StringOut = core.attr(str, computed=True)

    """
    Map of key-value pairs associated with the user.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The unique ID assigned by AWS for this user.
    """
    user_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly IAM user name to match.
    """
    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        user_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUser.Args(
                user_name=user_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_name: str | core.StringOut = core.arg()
