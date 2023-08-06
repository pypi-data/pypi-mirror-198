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

    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint_id: str | core.StringOut,
        status: str | core.StringOut,
        subnet_id: str | core.StringOut,
    ):
        super().__init__(
            args=Attachment.Args(
                endpoint_id=endpoint_id,
                status=status,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_id: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

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
class IpSetReferences(core.Schema):

    resolved_cidr_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        resolved_cidr_count: int | core.IntOut,
    ):
        super().__init__(
            args=IpSetReferences.Args(
                resolved_cidr_count=resolved_cidr_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resolved_cidr_count: int | core.IntOut = core.arg()


@core.schema
class Cidrs(core.Schema):

    available_cidr_count: int | core.IntOut = core.attr(int, computed=True)

    ip_set_references: list[IpSetReferences] | core.ArrayOut[IpSetReferences] = core.attr(
        IpSetReferences, computed=True, kind=core.Kind.array
    )

    utilized_cidr_count: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        available_cidr_count: int | core.IntOut,
        ip_set_references: list[IpSetReferences] | core.ArrayOut[IpSetReferences],
        utilized_cidr_count: int | core.IntOut,
    ):
        super().__init__(
            args=Cidrs.Args(
                available_cidr_count=available_cidr_count,
                ip_set_references=ip_set_references,
                utilized_cidr_count=utilized_cidr_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        available_cidr_count: int | core.IntOut = core.arg()

        ip_set_references: list[IpSetReferences] | core.ArrayOut[IpSetReferences] = core.arg()

        utilized_cidr_count: int | core.IntOut = core.arg()


@core.schema
class CapacityUsageSummary(core.Schema):

    cidrs: list[Cidrs] | core.ArrayOut[Cidrs] = core.attr(
        Cidrs, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cidrs: list[Cidrs] | core.ArrayOut[Cidrs],
    ):
        super().__init__(
            args=CapacityUsageSummary.Args(
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: list[Cidrs] | core.ArrayOut[Cidrs] = core.arg()


@core.schema
class FirewallStatus(core.Schema):

    capacity_usage_summary: list[CapacityUsageSummary] | core.ArrayOut[
        CapacityUsageSummary
    ] = core.attr(CapacityUsageSummary, computed=True, kind=core.Kind.array)

    configuration_sync_state_summary: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    sync_states: list[SyncStates] | core.ArrayOut[SyncStates] = core.attr(
        SyncStates, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        capacity_usage_summary: list[CapacityUsageSummary] | core.ArrayOut[CapacityUsageSummary],
        configuration_sync_state_summary: str | core.StringOut,
        status: str | core.StringOut,
        sync_states: list[SyncStates] | core.ArrayOut[SyncStates],
    ):
        super().__init__(
            args=FirewallStatus.Args(
                capacity_usage_summary=capacity_usage_summary,
                configuration_sync_state_summary=configuration_sync_state_summary,
                status=status,
                sync_states=sync_states,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_usage_summary: list[CapacityUsageSummary] | core.ArrayOut[
            CapacityUsageSummary
        ] = core.arg()

        configuration_sync_state_summary: str | core.StringOut = core.arg()

        status: str | core.StringOut = core.arg()

        sync_states: list[SyncStates] | core.ArrayOut[SyncStates] = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    key_id: str | core.StringOut = core.attr(str, computed=True)

    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        key_id: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                key_id=key_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_id: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.data(type="aws_networkfirewall_firewall", namespace="aws_networkfirewall")
class DsFirewall(core.Data):

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    delete_protection: bool | core.BoolOut = core.attr(bool, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    encryption_configuration: list[EncryptionConfiguration] | core.ArrayOut[
        EncryptionConfiguration
    ] = core.attr(EncryptionConfiguration, computed=True, kind=core.Kind.array)

    firewall_policy_arn: str | core.StringOut = core.attr(str, computed=True)

    firewall_policy_change_protection: bool | core.BoolOut = core.attr(bool, computed=True)

    firewall_status: list[FirewallStatus] | core.ArrayOut[FirewallStatus] = core.attr(
        FirewallStatus, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    subnet_change_protection: bool | core.BoolOut = core.attr(bool, computed=True)

    subnet_mapping: list[SubnetMapping] | core.ArrayOut[SubnetMapping] = core.attr(
        SubnetMapping, computed=True, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    update_token: str | core.StringOut = core.attr(str, computed=True)

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFirewall.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
