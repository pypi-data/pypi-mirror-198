import terrascript.core as core


@core.schema
class Notification(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    sns_topic: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut],
        sns_topic: str | core.StringOut,
    ):
        super().__init__(
            args=Notification.Args(
                events=events,
                sns_topic=sns_topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        sns_topic: str | core.StringOut = core.arg()


@core.resource(type="aws_glacier_vault", namespace="glacier")
class Vault(core.Resource):
    """
    (Optional) The policy document. This is a JSON formatted string.
    """

    access_policy: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ARN of the vault.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The URI of the vault that was created.
    """
    location: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Vault. Names can be between 1 and 255 characters long and the valid chara
    cters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The notifications for the Vault. Fields documented below.
    """
    notification: Notification | None = core.attr(Notification, default=None)

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
        name: str | core.StringOut,
        access_policy: str | core.StringOut | None = None,
        notification: Notification | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vault.Args(
                name=name,
                access_policy=access_policy,
                notification=notification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        notification: Notification | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
