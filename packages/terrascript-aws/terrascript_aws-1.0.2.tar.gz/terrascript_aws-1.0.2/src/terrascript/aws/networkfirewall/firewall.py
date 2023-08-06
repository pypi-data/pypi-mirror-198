import terrascript.core as core


@core.schema
class SubnetMapping(core.Schema):

    subnet_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=SubnetMapping.Args(
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_id: str | core.StringOut = core.arg()


@core.schema
class Attachment(core.Schema):

    endpoint_id: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint_id: str | core.StringOut,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=Attachment.Args(
                endpoint_id=endpoint_id,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_id: str | core.StringOut = core.arg()

        subnet_id: str | core.StringOut = core.arg()


@core.schema
class SyncStates(core.Schema):

    attachment: list[Attachment] | core.ArrayOut[Attachment] = core.attr(
        Attachment, computed=True, kind=core.Kind.array
    )

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment: list[Attachment] | core.ArrayOut[Attachment],
        availability_zone: str | core.StringOut,
    ):
        super().__init__(
            args=SyncStates.Args(
                attachment=attachment,
                availability_zone=availability_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment: list[Attachment] | core.ArrayOut[Attachment] = core.arg()

        availability_zone: str | core.StringOut = core.arg()


@core.schema
class FirewallStatus(core.Schema):

    sync_states: list[SyncStates] | core.ArrayOut[SyncStates] = core.attr(
        SyncStates, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        sync_states: list[SyncStates] | core.ArrayOut[SyncStates],
    ):
        super().__init__(
            args=FirewallStatus.Args(
                sync_states=sync_states,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sync_states: list[SyncStates] | core.ArrayOut[SyncStates] = core.arg()


@core.resource(type="aws_networkfirewall_firewall", namespace="aws_networkfirewall")
class Firewall(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    delete_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    firewall_policy_arn: str | core.StringOut = core.attr(str)

    firewall_policy_change_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    firewall_status: list[FirewallStatus] | core.ArrayOut[FirewallStatus] = core.attr(
        FirewallStatus, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    subnet_change_protection: bool | core.BoolOut | None = core.attr(bool, default=None)

    subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] = core.attr(
        SubnetMapping, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_token: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_policy_arn: str | core.StringOut,
        name: str | core.StringOut,
        subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping],
        vpc_id: str | core.StringOut,
        delete_protection: bool | core.BoolOut | None = None,
        description: str | core.StringOut | None = None,
        firewall_policy_change_protection: bool | core.BoolOut | None = None,
        subnet_change_protection: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Firewall.Args(
                firewall_policy_arn=firewall_policy_arn,
                name=name,
                subnet_mapping=subnet_mapping,
                vpc_id=vpc_id,
                delete_protection=delete_protection,
                description=description,
                firewall_policy_change_protection=firewall_policy_change_protection,
                subnet_change_protection=subnet_change_protection,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_protection: bool | core.BoolOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        firewall_policy_arn: str | core.StringOut = core.arg()

        firewall_policy_change_protection: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        subnet_change_protection: bool | core.BoolOut | None = core.arg(default=None)

        subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_id: str | core.StringOut = core.arg()
