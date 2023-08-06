import terrascript.core as core


@core.data(type="aws_iam_role", namespace="iam")
class DsRole(core.Data):
    """
    The Amazon Resource Name (ARN) specifying the role.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The policy document associated with the role.
    """
    assume_role_policy: str | core.StringOut = core.attr(str, computed=True)

    """
    Creation date of the role in RFC 3339 format.
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    """
    Description for the role.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    The friendly IAM role name to match.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Maximum session duration.
    """
    max_session_duration: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The friendly IAM role name to match.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The path to the role.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    The ARN of the policy that is used to set the permissions boundary for the role.
    """
    permissions_boundary: str | core.StringOut = core.attr(str, computed=True)

    """
    The tags attached to the role.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    The stable and unique string identifying the role.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRole.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
