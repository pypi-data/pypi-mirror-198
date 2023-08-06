import terrascript.core as core


@core.data(type="aws_iam_users", namespace="iam")
class DsUsers(core.Data):
    """
    Set of ARNs of the matched IAM users.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Regex string to apply to the IAM users list returned by AWS. This allows more advanced fi
    ltering not supported from the AWS API. This filtering is done locally on what AWS returns, and coul
    d have a performance impact if the result is large. Combine this with other options to narrow down t
    he list AWS returns.
    """
    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    """
    Set of Names of the matched IAM users.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The path prefix for filtering the results. For example, the prefix `/division_abc/subdivi
    sion_xyz/` gets all users whose path starts with `/division_abc/subdivision_xyz/`. If it is not incl
    uded, it defaults to a slash (`/`), listing all users. For more details, check out [list-users in th
    e AWS CLI reference][1].
    """
    path_prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: str | core.StringOut | None = None,
        path_prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsUsers.Args(
                name_regex=name_regex,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: str | core.StringOut | None = core.arg(default=None)

        path_prefix: str | core.StringOut | None = core.arg(default=None)
