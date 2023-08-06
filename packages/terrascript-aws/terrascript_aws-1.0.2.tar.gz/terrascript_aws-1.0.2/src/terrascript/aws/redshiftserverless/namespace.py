import terrascript.core as core


@core.resource(type="aws_redshiftserverless_namespace", namespace="aws_redshiftserverless")
class Namespace(core.Resource):

    admin_user_password: str | core.StringOut | None = core.attr(str, default=None)

    admin_username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    db_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    log_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    namespace_id: str | core.StringOut = core.attr(str, computed=True)

    namespace_name: str | core.StringOut = core.attr(str)

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
        namespace_name: str | core.StringOut,
        admin_user_password: str | core.StringOut | None = None,
        admin_username: str | core.StringOut | None = None,
        db_name: str | core.StringOut | None = None,
        default_iam_role_arn: str | core.StringOut | None = None,
        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = None,
        kms_key_id: str | core.StringOut | None = None,
        log_exports: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Namespace.Args(
                namespace_name=namespace_name,
                admin_user_password=admin_user_password,
                admin_username=admin_username,
                db_name=db_name,
                default_iam_role_arn=default_iam_role_arn,
                iam_roles=iam_roles,
                kms_key_id=kms_key_id,
                log_exports=log_exports,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_user_password: str | core.StringOut | None = core.arg(default=None)

        admin_username: str | core.StringOut | None = core.arg(default=None)

        db_name: str | core.StringOut | None = core.arg(default=None)

        default_iam_role_arn: str | core.StringOut | None = core.arg(default=None)

        iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        log_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        namespace_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
