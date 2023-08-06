import terrascript.core as core


@core.schema
class UserConfig(core.Schema):

    contact_flow_id: str | core.StringOut = core.attr(str, computed=True)

    user_id: str | core.StringOut = core.attr(str, computed=True)

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

    phone_number: str | core.StringOut = core.attr(str, computed=True)

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

    contact_flow_id: str | core.StringOut = core.attr(str, computed=True)

    queue_id: str | core.StringOut = core.attr(str, computed=True)

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

    phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig] = core.attr(
        PhoneConfig, computed=True, kind=core.Kind.array
    )

    queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig] = core.attr(
        QueueConfig, computed=True, kind=core.Kind.array
    )

    quick_connect_type: str | core.StringOut = core.attr(str, computed=True)

    user_config: list[UserConfig] | core.ArrayOut[UserConfig] = core.attr(
        UserConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig],
        queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig],
        quick_connect_type: str | core.StringOut,
        user_config: list[UserConfig] | core.ArrayOut[UserConfig],
    ):
        super().__init__(
            args=QuickConnectConfig.Args(
                phone_config=phone_config,
                queue_config=queue_config,
                quick_connect_type=quick_connect_type,
                user_config=user_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_config: list[PhoneConfig] | core.ArrayOut[PhoneConfig] = core.arg()

        queue_config: list[QueueConfig] | core.ArrayOut[QueueConfig] = core.arg()

        quick_connect_type: str | core.StringOut = core.arg()

        user_config: list[UserConfig] | core.ArrayOut[UserConfig] = core.arg()


@core.data(type="aws_connect_quick_connect", namespace="connect")
class DsQuickConnect(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    quick_connect_config: list[QuickConnectConfig] | core.ArrayOut[QuickConnectConfig] = core.attr(
        QuickConnectConfig, computed=True, kind=core.Kind.array
    )

    quick_connect_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: str | core.StringOut,
        name: str | core.StringOut | None = None,
        quick_connect_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQuickConnect.Args(
                instance_id=instance_id,
                name=name,
                quick_connect_id=quick_connect_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        quick_connect_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
