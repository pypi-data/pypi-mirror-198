import terrascript.core as core


@core.schema
class Conditions(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None)

    operator: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        key: str | core.StringOut | None = None,
        operator: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Conditions.Args(
                type=type,
                key=key,
                operator=operator,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        operator: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Action(core.Schema):

    association_method: str | core.StringOut = core.attr(str)

    require_acceptance: bool | core.BoolOut | None = core.attr(bool, default=None)

    segment: str | core.StringOut | None = core.attr(str, default=None)

    tag_value_of_key: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        association_method: str | core.StringOut,
        require_acceptance: bool | core.BoolOut | None = None,
        segment: str | core.StringOut | None = None,
        tag_value_of_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Action.Args(
                association_method=association_method,
                require_acceptance=require_acceptance,
                segment=segment,
                tag_value_of_key=tag_value_of_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        association_method: str | core.StringOut = core.arg()

        require_acceptance: bool | core.BoolOut | None = core.arg(default=None)

        segment: str | core.StringOut | None = core.arg(default=None)

        tag_value_of_key: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AttachmentPolicies(core.Schema):

    action: Action = core.attr(Action)

    condition_logic: str | core.StringOut | None = core.attr(str, default=None)

    conditions: list[Conditions] | core.ArrayOut[Conditions] = core.attr(
        Conditions, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    rule_number: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        action: Action,
        conditions: list[Conditions] | core.ArrayOut[Conditions],
        rule_number: int | core.IntOut,
        condition_logic: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AttachmentPolicies.Args(
                action=action,
                conditions=conditions,
                rule_number=rule_number,
                condition_logic=condition_logic,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        condition_logic: str | core.StringOut | None = core.arg(default=None)

        conditions: list[Conditions] | core.ArrayOut[Conditions] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        rule_number: int | core.IntOut = core.arg()


@core.schema
class EdgeLocations(core.Schema):

    asn: int | core.IntOut | None = core.attr(int, default=None)

    inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    location: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        location: str | core.StringOut,
        asn: int | core.IntOut | None = None,
        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=EdgeLocations.Args(
                location=location,
                asn=asn,
                inside_cidr_blocks=inside_cidr_blocks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        asn: int | core.IntOut | None = core.arg(default=None)

        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        location: str | core.StringOut = core.arg()


@core.schema
class CoreNetworkConfiguration(core.Schema):

    asn_ranges: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    edge_locations: list[EdgeLocations] | core.ArrayOut[EdgeLocations] = core.attr(
        EdgeLocations, kind=core.Kind.array
    )

    inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpn_ecmp_support: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        asn_ranges: list[str] | core.ArrayOut[core.StringOut],
        edge_locations: list[EdgeLocations] | core.ArrayOut[EdgeLocations],
        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpn_ecmp_support: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=CoreNetworkConfiguration.Args(
                asn_ranges=asn_ranges,
                edge_locations=edge_locations,
                inside_cidr_blocks=inside_cidr_blocks,
                vpn_ecmp_support=vpn_ecmp_support,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        asn_ranges: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        edge_locations: list[EdgeLocations] | core.ArrayOut[EdgeLocations] = core.arg()

        inside_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpn_ecmp_support: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class Segments(core.Schema):

    allow_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    deny_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: str | core.StringOut | None = core.attr(str, default=None)

    edge_locations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    isolate_attachments: bool | core.BoolOut | None = core.attr(bool, default=None)

    name: str | core.StringOut = core.attr(str)

    require_attachment_acceptance: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        allow_filter: list[str] | core.ArrayOut[core.StringOut] | None = None,
        deny_filter: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        edge_locations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        isolate_attachments: bool | core.BoolOut | None = None,
        require_attachment_acceptance: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Segments.Args(
                name=name,
                allow_filter=allow_filter,
                deny_filter=deny_filter,
                description=description,
                edge_locations=edge_locations,
                isolate_attachments=isolate_attachments,
                require_attachment_acceptance=require_attachment_acceptance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        deny_filter: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        edge_locations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        isolate_attachments: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        require_attachment_acceptance: bool | core.BoolOut | None = core.arg(default=None)


@core.schema
class SegmentActions(core.Schema):

    action: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    destination_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    mode: str | core.StringOut | None = core.attr(str, default=None)

    segment: str | core.StringOut = core.attr(str)

    share_with: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    share_with_except: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        action: str | core.StringOut,
        segment: str | core.StringOut,
        description: str | core.StringOut | None = None,
        destination_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = None,
        destinations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        mode: str | core.StringOut | None = None,
        share_with: list[str] | core.ArrayOut[core.StringOut] | None = None,
        share_with_except: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=SegmentActions.Args(
                action=action,
                segment=segment,
                description=description,
                destination_cidr_blocks=destination_cidr_blocks,
                destinations=destinations,
                mode=mode,
                share_with=share_with,
                share_with_except=share_with_except,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        destination_cidr_blocks: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)

        segment: str | core.StringOut = core.arg()

        share_with: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        share_with_except: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.data(type="aws_networkmanager_core_network_policy_document", namespace="networkmanager")
class DsCoreNetworkPolicyDocument(core.Data):

    attachment_policies: list[AttachmentPolicies] | core.ArrayOut[
        AttachmentPolicies
    ] | None = core.attr(AttachmentPolicies, default=None, kind=core.Kind.array)

    core_network_configuration: list[CoreNetworkConfiguration] | core.ArrayOut[
        CoreNetworkConfiguration
    ] = core.attr(CoreNetworkConfiguration, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Standard JSON policy document rendered based on the arguments above.
    """
    json: str | core.StringOut = core.attr(str, computed=True)

    segment_actions: list[SegmentActions] | core.ArrayOut[SegmentActions] | None = core.attr(
        SegmentActions, default=None, kind=core.Kind.array
    )

    segments: list[Segments] | core.ArrayOut[Segments] = core.attr(Segments, kind=core.Kind.array)

    version: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        core_network_configuration: list[CoreNetworkConfiguration]
        | core.ArrayOut[CoreNetworkConfiguration],
        segments: list[Segments] | core.ArrayOut[Segments],
        attachment_policies: list[AttachmentPolicies]
        | core.ArrayOut[AttachmentPolicies]
        | None = None,
        segment_actions: list[SegmentActions] | core.ArrayOut[SegmentActions] | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCoreNetworkPolicyDocument.Args(
                core_network_configuration=core_network_configuration,
                segments=segments,
                attachment_policies=attachment_policies,
                segment_actions=segment_actions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_policies: list[AttachmentPolicies] | core.ArrayOut[
            AttachmentPolicies
        ] | None = core.arg(default=None)

        core_network_configuration: list[CoreNetworkConfiguration] | core.ArrayOut[
            CoreNetworkConfiguration
        ] = core.arg()

        segment_actions: list[SegmentActions] | core.ArrayOut[SegmentActions] | None = core.arg(
            default=None
        )

        segments: list[Segments] | core.ArrayOut[Segments] = core.arg()

        version: str | core.StringOut | None = core.arg(default=None)
