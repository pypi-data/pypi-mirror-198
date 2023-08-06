import terrascript.core as core


@core.schema
class UserConfig(core.Schema):

    contact_flow_id: str | core.StringOut = core.attr(str)

    user_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        contact_flow_id: str | core.StringOut,
        user_id: str | core.StringOut,
    ):
        super().__init__(
            args=UserConfig.Args(
                contact_flow_id=contact_flow_id,
                user_id=user_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_id: str | core.StringOut = core.arg()

        user_id: str | core.StringOut = core.arg()


@core.schema
class PhoneConfig(core.Schema):

    phone_number: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        phone_number: str | core.StringOut,
    ):
        super().__init__(
            args=PhoneConfig.Args(
                phone_number=phone_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_number: str | core.StringOut = core.arg()


@core.schema
class QueueConfig(core.Schema):

    contact_flow_id: str | core.StringOut = core.attr(str)

    queue_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        contact_flow_id: str | core.StringOut,
        queue_id: str | core.StringOut,
    ):
        super().__init__(
            args=QueueConfig.Args(
                contact_flow_id=contact_flow_id,
                queue_id=queue_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_id: str | core.StringOut = core.arg()

        queue_id: str | core.StringOut = core.arg()


@core.schema
class QuickConnectConfig(core.Schema):

    phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig] | None = core.attr(
        PhoneConfig, default=None, kind=core.Kind.array
    )

    queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig] | None = core.attr(
        QueueConfig, default=None, kind=core.Kind.array
    )

    quick_connect_type: str | core.StringOut = core.attr(str)

    user_config: list[UserConfig] | core.ArrayOut[UserConfig] | None = core.attr(
        UserConfig, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        quick_connect_type: str | core.StringOut,
        phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig] | None = None,
        queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig] | None = None,
        user_config: list[UserConfig] | core.ArrayOut[UserConfig] | None = None,
    ):
        super().__init__(
            args=QuickConnectConfig.Args(
                quick_connect_type=quick_connect_type,
                phone_config=phone_config,
                queue_config=queue_config,
                user_config=user_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig] | None = core.arg(default=None)

        queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig] | None = core.arg(default=None)

        quick_connect_type: str | core.StringOut = core.arg()

        user_config: list[UserConfig] | core.ArrayOut[UserConfig] | None = core.arg(default=None)


@core.resource(type="aws_connect_quick_connect", namespace="connect")
class QuickConnect(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Quick Connect.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the description of the Quick Connect.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Quick Connect separated
    by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies the identifier of the hosting Amazon Connect Instance.
    """
    instance_id: str | core.StringOut = core.attr(str)

    """
    (Required) Specifies the name of the Quick Connect.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) A block that defines the configuration information for the Quick Connect: `quick_connect_
    type` and one of `phone_config`, `queue_config`, `user_config` . The Quick Connect Config block is d
    ocumented below.
    """
    quick_connect_config: QuickConnectConfig = core.attr(QuickConnectConfig)

    """
    The identifier for the Quick Connect.
    """
    quick_connect_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Tags to apply to the Quick Connect. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        instance_id: str | core.StringOut,
        name: str | core.StringOut,
        quick_connect_config: QuickConnectConfig,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=QuickConnect.Args(
                instance_id=instance_id,
                name=name,
                quick_connect_config=quick_connect_config,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        quick_connect_config: QuickConnectConfig = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
