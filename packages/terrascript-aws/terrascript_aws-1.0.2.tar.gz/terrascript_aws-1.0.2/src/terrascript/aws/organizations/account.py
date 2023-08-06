import terrascript.core as core


@core.resource(type="aws_organizations_account", namespace="aws_organizations")
class Account(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    close_on_deletion: bool | core.BoolOut | None = core.attr(bool, default=None)

    create_govcloud: bool | core.BoolOut | None = core.attr(bool, default=None)

    email: str | core.StringOut = core.attr(str)

    govcloud_id: str | core.StringOut = core.attr(str, computed=True)

    iam_user_access_to_billing: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    joined_method: str | core.StringOut = core.attr(str, computed=True)

    joined_timestamp: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    parent_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role_name: str | core.StringOut | None = core.attr(str, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        email: str | core.StringOut,
        name: str | core.StringOut,
        close_on_deletion: bool | core.BoolOut | None = None,
        create_govcloud: bool | core.BoolOut | None = None,
        iam_user_access_to_billing: str | core.StringOut | None = None,
        parent_id: str | core.StringOut | None = None,
        role_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                email=email,
                name=name,
                close_on_deletion=close_on_deletion,
                create_govcloud=create_govcloud,
                iam_user_access_to_billing=iam_user_access_to_billing,
                parent_id=parent_id,
                role_name=role_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        close_on_deletion: bool | core.BoolOut | None = core.arg(default=None)

        create_govcloud: bool | core.BoolOut | None = core.arg(default=None)

        email: str | core.StringOut = core.arg()

        iam_user_access_to_billing: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        parent_id: str | core.StringOut | None = core.arg(default=None)

        role_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
