import terrascript.core as core


@core.resource(type="aws_elasticache_user", namespace="elasticache")
class User(core.Resource):
    """
    (Required) Access permissions string used for this user. See [Specifying Permissions Using an Access
    String](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html#Access-strin
    g) for more details.
    """

    access_string: str | core.StringOut = core.attr(str)

    """
    The ARN of the created ElastiCache User.
    """
    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The current supported value is `REDIS`.
    """
    engine: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Indicates a password is not required for this user.
    """
    no_password_required: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Passwords used for this user. You can create up to two passwords for each user.
    """
    passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) A list of tags to be added to this resource. A tag is a key-value pair.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The ID of the user.
    """
    user_id: str | core.StringOut = core.attr(str)

    """
    (Required) The username of the user.
    """
    user_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_string: str | core.StringOut,
        engine: str | core.StringOut,
        user_id: str | core.StringOut,
        user_name: str | core.StringOut,
        arn: str | core.StringOut | None = None,
        no_password_required: bool | core.BoolOut | None = None,
        passwords: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                access_string=access_string,
                engine=engine,
                user_id=user_id,
                user_name=user_name,
                arn=arn,
                no_password_required=no_password_required,
                passwords=passwords,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_string: str | core.StringOut = core.arg()

        arn: str | core.StringOut | None = core.arg(default=None)

        engine: str | core.StringOut = core.arg()

        no_password_required: bool | core.BoolOut | None = core.arg(default=None)

        passwords: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        user_id: str | core.StringOut = core.arg()

        user_name: str | core.StringOut = core.arg()
