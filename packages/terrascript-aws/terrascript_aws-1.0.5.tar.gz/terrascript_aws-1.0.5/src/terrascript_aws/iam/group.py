import terrascript.core as core


@core.resource(type="aws_iam_group", namespace="iam")
class Group(core.Resource):
    """
    The ARN assigned by AWS for this group.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The group's ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The group's name. The name must consist of upper and lowercase alphanumeric characters wi
    th no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not d
    istinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional, default "/") Path in which to create the group.
    """
    path: str | core.StringOut | None = core.attr(str, default=None)

    """
    The [unique ID][1] assigned by AWS.
    """
    unique_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        path: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Group.Args(
                name=name,
                path=path,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut = core.arg()

        path: str | core.StringOut | None = core.arg(default=None)
