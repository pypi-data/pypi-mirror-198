import terrascript.core as core


@core.data(type="aws_iam_roles", namespace="iam")
class DsRoles(core.Data):
    """
    Set of ARNs of the matched IAM roles.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A regex string to apply to the IAM roles list returned by AWS. This allows more advanced
    filtering not supported from the AWS API. This filtering is done locally on what AWS returns, and co
    uld have a performance impact if the result is large. Combine this with other options to narrow down
    the list AWS returns.
    """
    name_regex: str | core.StringOut | None = core.attr(str, default=None)

    """
    Set of Names of the matched IAM roles.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) The path prefix for filtering the results. For example, the prefix `/application_abc/comp
    onent_xyz/` gets all roles whose path starts with `/application_abc/component_xyz/`. If it is not in
    cluded, it defaults to a slash (`/`), listing all roles. For more details, check out [list-roles in
    the AWS CLI reference][1].
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
            args=DsRoles.Args(
                name_regex=name_regex,
                path_prefix=path_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_regex: str | core.StringOut | None = core.arg(default=None)

        path_prefix: str | core.StringOut | None = core.arg(default=None)
