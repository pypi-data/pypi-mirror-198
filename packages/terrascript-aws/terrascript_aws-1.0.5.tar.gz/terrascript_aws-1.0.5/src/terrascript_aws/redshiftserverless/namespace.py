import terrascript.core as core


@core.resource(type="aws_redshiftserverless_namespace", namespace="redshiftserverless")
class Namespace(core.Resource):
    """
    (Optional) The password of the administrator for the first database created in the namespace.
    """

    admin_user_password: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The username of the administrator for the first database created in the namespace.
    """
    admin_username: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the Redshift Serverless Namespace.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the first database created in the namespace.
    """
    db_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
    """
    default_iam_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A list of IAM roles to associate with the namespace.
    """
    iam_roles: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    The Redshift Namespace Name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN of the Amazon Web Services Key Management Service key used to encrypt your data.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The types of logs the namespace can export. Available export types are `userlog`, `connec
    tionlog`, and `useractivitylog`.
    """
    log_exports: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The Redshift Namespace ID.
    """
    namespace_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the namespace.
    """
    namespace_name: str | core.StringOut = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
