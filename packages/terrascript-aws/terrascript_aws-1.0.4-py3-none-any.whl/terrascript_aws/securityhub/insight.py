import terrascript.core as core


@core.schema
class MalwareName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MalwareName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessPath(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ProcessPath.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Title(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Title.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class DateRange(core.Schema):

    unit: str | core.StringOut = core.attr(str)

    value: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        unit: str | core.StringOut,
        value: int | core.IntOut,
    ):
        super().__init__(
            args=DateRange.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: str | core.StringOut = core.arg()

        value: int | core.IntOut = core.arg()


@core.schema
class UpdatedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=UpdatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CreatedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CreatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NetworkDirection(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkDirection.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkDestinationDomain(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkDestinationDomain.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Criticality(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Criticality.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Confidence(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Confidence.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class FirstObservedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FirstObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RecordState(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=RecordState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ThreatIntelIndicatorValue(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ThreatIntelIndicatorValue.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ComplianceStatus(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ComplianceStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProductFields(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ProductFields.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessLaunchedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProcessLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceAwsEc2InstanceIpv6Addresses(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIpv6Addresses.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class MalwareState(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MalwareState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsCriticality(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FindingProviderFieldsCriticality.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Type(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Type.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Id(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Id.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceContainerImageName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceContainerImageName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsTypes(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=FindingProviderFieldsTypes.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NoteText(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NoteText.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Description(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Description.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceContainerName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceContainerName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class SourceUrl(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=SourceUrl.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class LastObservedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=LastObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceRegion(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceRegion.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProductArn(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkSourcePort(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NetworkSourcePort.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceAwsEc2InstanceType(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class RelatedFindingsId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=RelatedFindingsId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class WorkflowStatus(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=WorkflowStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class RelatedFindingsProductArn(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=RelatedFindingsProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkSourceMac(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkSourceMac.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessParentPid(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProcessParentPid.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceVpcId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceVpcId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessTerminatedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProcessTerminatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class NoteUpdatedBy(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NoteUpdatedBy.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceLaunchedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ThreatIntelIndicatorType(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ThreatIntelIndicatorType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProductName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ProductName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceIamInstanceProfileArn(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIamInstanceProfileArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class VerificationState(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=VerificationState.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceContainerLaunchedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ResourceContainerLaunchedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourceAwsEc2InstanceIpv4Addresses(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceIpv4Addresses.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsRelatedFindingsId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=FindingProviderFieldsRelatedFindingsId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class AwsAccountId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=AwsAccountId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkDestinationIpv6(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkDestinationIpv6.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class NetworkProtocol(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkProtocol.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsSeverityOriginal(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=FindingProviderFieldsSeverityOriginal.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkSourceIpv6(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkSourceIpv6.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsRelatedFindingsProductArn(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=FindingProviderFieldsRelatedFindingsProductArn.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceSubnetId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceSubnetId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceContainerImageId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceContainerImageId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkDestinationPort(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NetworkDestinationPort.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ResourcePartition(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourcePartition.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceKeyName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceKeyName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class FindingProviderFieldsSeverityLabel(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=FindingProviderFieldsSeverityLabel.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkSourceIpv4(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkSourceIpv4.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class ThreatIntelIndicatorCategory(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ThreatIntelIndicatorCategory.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceType(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessPid(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ProcessPid.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class RecommendationText(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=RecommendationText.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ThreatIntelIndicatorSource(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ThreatIntelIndicatorSource.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsIamAccessKeyStatus(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyStatus.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsS3BucketOwnerName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsS3BucketOwnerName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsIamAccessKeyUserName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyUserName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class Keyword(core.Schema):

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Keyword.Args(
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: str | core.StringOut = core.arg()


@core.schema
class CompanyName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=CompanyName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ProcessName(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ProcessName.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NoteUpdatedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NoteUpdatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class FindingProviderFieldsConfidence(core.Schema):

    eq: str | core.StringOut | None = core.attr(str, default=None)

    gte: str | core.StringOut | None = core.attr(str, default=None)

    lte: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        eq: str | core.StringOut | None = None,
        gte: str | core.StringOut | None = None,
        lte: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FindingProviderFieldsConfidence.Args(
                eq=eq,
                gte=gte,
                lte=lte,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: str | core.StringOut | None = core.arg(default=None)

        gte: str | core.StringOut | None = core.arg(default=None)

        lte: str | core.StringOut | None = core.arg(default=None)


@core.schema
class UserDefinedValues(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=UserDefinedValues.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsEc2InstanceImageId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsEc2InstanceImageId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsIamAccessKeyCreatedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ResourceAwsIamAccessKeyCreatedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class SeverityLabel(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=SeverityLabel.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class GeneratorId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=GeneratorId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkDestinationIpv4(core.Schema):

    cidr: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cidr: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkDestinationIpv4.Args(
                cidr=cidr,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: str | core.StringOut = core.arg()


@core.schema
class ThreatIntelIndicatorSourceUrl(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ThreatIntelIndicatorSourceUrl.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class MalwareType(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MalwareType.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceDetailsOther(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceDetailsOther.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceAwsS3BucketOwnerId(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceAwsS3BucketOwnerId.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class MalwarePath(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=MalwarePath.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ResourceTags(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=ResourceTags.Args(
                comparison=comparison,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class NetworkSourceDomain(core.Schema):

    comparison: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        comparison: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=NetworkSourceDomain.Args(
                comparison=comparison,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class ThreatIntelIndicatorLastObservedAt(core.Schema):

    date_range: DateRange | None = core.attr(DateRange, default=None)

    end: str | core.StringOut | None = core.attr(str, default=None)

    start: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        date_range: DateRange | None = None,
        end: str | core.StringOut | None = None,
        start: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ThreatIntelIndicatorLastObservedAt.Args(
                date_range=date_range,
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date_range: DateRange | None = core.arg(default=None)

        end: str | core.StringOut | None = core.arg(default=None)

        start: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Filters(core.Schema):

    aws_account_id: list[AwsAccountId] | core.ArrayOut[AwsAccountId] | None = core.attr(
        AwsAccountId, default=None, kind=core.Kind.array
    )

    company_name: list[CompanyName] | core.ArrayOut[CompanyName] | None = core.attr(
        CompanyName, default=None, kind=core.Kind.array
    )

    compliance_status: list[ComplianceStatus] | core.ArrayOut[ComplianceStatus] | None = core.attr(
        ComplianceStatus, default=None, kind=core.Kind.array
    )

    confidence: list[Confidence] | core.ArrayOut[Confidence] | None = core.attr(
        Confidence, default=None, kind=core.Kind.array
    )

    created_at: list[CreatedAt] | core.ArrayOut[CreatedAt] | None = core.attr(
        CreatedAt, default=None, kind=core.Kind.array
    )

    criticality: list[Criticality] | core.ArrayOut[Criticality] | None = core.attr(
        Criticality, default=None, kind=core.Kind.array
    )

    description: list[Description] | core.ArrayOut[Description] | None = core.attr(
        Description, default=None, kind=core.Kind.array
    )

    finding_provider_fields_confidence: list[FindingProviderFieldsConfidence] | core.ArrayOut[
        FindingProviderFieldsConfidence
    ] | None = core.attr(FindingProviderFieldsConfidence, default=None, kind=core.Kind.array)

    finding_provider_fields_criticality: list[FindingProviderFieldsCriticality] | core.ArrayOut[
        FindingProviderFieldsCriticality
    ] | None = core.attr(FindingProviderFieldsCriticality, default=None, kind=core.Kind.array)

    finding_provider_fields_related_findings_id: list[
        FindingProviderFieldsRelatedFindingsId
    ] | core.ArrayOut[FindingProviderFieldsRelatedFindingsId] | None = core.attr(
        FindingProviderFieldsRelatedFindingsId, default=None, kind=core.Kind.array
    )

    finding_provider_fields_related_findings_product_arn: list[
        FindingProviderFieldsRelatedFindingsProductArn
    ] | core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn] | None = core.attr(
        FindingProviderFieldsRelatedFindingsProductArn, default=None, kind=core.Kind.array
    )

    finding_provider_fields_severity_label: list[
        FindingProviderFieldsSeverityLabel
    ] | core.ArrayOut[FindingProviderFieldsSeverityLabel] | None = core.attr(
        FindingProviderFieldsSeverityLabel, default=None, kind=core.Kind.array
    )

    finding_provider_fields_severity_original: list[
        FindingProviderFieldsSeverityOriginal
    ] | core.ArrayOut[FindingProviderFieldsSeverityOriginal] | None = core.attr(
        FindingProviderFieldsSeverityOriginal, default=None, kind=core.Kind.array
    )

    finding_provider_fields_types: list[FindingProviderFieldsTypes] | core.ArrayOut[
        FindingProviderFieldsTypes
    ] | None = core.attr(FindingProviderFieldsTypes, default=None, kind=core.Kind.array)

    first_observed_at: list[FirstObservedAt] | core.ArrayOut[FirstObservedAt] | None = core.attr(
        FirstObservedAt, default=None, kind=core.Kind.array
    )

    generator_id: list[GeneratorId] | core.ArrayOut[GeneratorId] | None = core.attr(
        GeneratorId, default=None, kind=core.Kind.array
    )

    id: list[Id] | core.ArrayOut[Id] | None = core.attr(Id, default=None, kind=core.Kind.array)

    keyword: list[Keyword] | core.ArrayOut[Keyword] | None = core.attr(
        Keyword, default=None, kind=core.Kind.array
    )

    last_observed_at: list[LastObservedAt] | core.ArrayOut[LastObservedAt] | None = core.attr(
        LastObservedAt, default=None, kind=core.Kind.array
    )

    malware_name: list[MalwareName] | core.ArrayOut[MalwareName] | None = core.attr(
        MalwareName, default=None, kind=core.Kind.array
    )

    malware_path: list[MalwarePath] | core.ArrayOut[MalwarePath] | None = core.attr(
        MalwarePath, default=None, kind=core.Kind.array
    )

    malware_state: list[MalwareState] | core.ArrayOut[MalwareState] | None = core.attr(
        MalwareState, default=None, kind=core.Kind.array
    )

    malware_type: list[MalwareType] | core.ArrayOut[MalwareType] | None = core.attr(
        MalwareType, default=None, kind=core.Kind.array
    )

    network_destination_domain: list[NetworkDestinationDomain] | core.ArrayOut[
        NetworkDestinationDomain
    ] | None = core.attr(NetworkDestinationDomain, default=None, kind=core.Kind.array)

    network_destination_ipv4: list[NetworkDestinationIpv4] | core.ArrayOut[
        NetworkDestinationIpv4
    ] | None = core.attr(NetworkDestinationIpv4, default=None, kind=core.Kind.array)

    network_destination_ipv6: list[NetworkDestinationIpv6] | core.ArrayOut[
        NetworkDestinationIpv6
    ] | None = core.attr(NetworkDestinationIpv6, default=None, kind=core.Kind.array)

    network_destination_port: list[NetworkDestinationPort] | core.ArrayOut[
        NetworkDestinationPort
    ] | None = core.attr(NetworkDestinationPort, default=None, kind=core.Kind.array)

    network_direction: list[NetworkDirection] | core.ArrayOut[NetworkDirection] | None = core.attr(
        NetworkDirection, default=None, kind=core.Kind.array
    )

    network_protocol: list[NetworkProtocol] | core.ArrayOut[NetworkProtocol] | None = core.attr(
        NetworkProtocol, default=None, kind=core.Kind.array
    )

    network_source_domain: list[NetworkSourceDomain] | core.ArrayOut[
        NetworkSourceDomain
    ] | None = core.attr(NetworkSourceDomain, default=None, kind=core.Kind.array)

    network_source_ipv4: list[NetworkSourceIpv4] | core.ArrayOut[
        NetworkSourceIpv4
    ] | None = core.attr(NetworkSourceIpv4, default=None, kind=core.Kind.array)

    network_source_ipv6: list[NetworkSourceIpv6] | core.ArrayOut[
        NetworkSourceIpv6
    ] | None = core.attr(NetworkSourceIpv6, default=None, kind=core.Kind.array)

    network_source_mac: list[NetworkSourceMac] | core.ArrayOut[NetworkSourceMac] | None = core.attr(
        NetworkSourceMac, default=None, kind=core.Kind.array
    )

    network_source_port: list[NetworkSourcePort] | core.ArrayOut[
        NetworkSourcePort
    ] | None = core.attr(NetworkSourcePort, default=None, kind=core.Kind.array)

    note_text: list[NoteText] | core.ArrayOut[NoteText] | None = core.attr(
        NoteText, default=None, kind=core.Kind.array
    )

    note_updated_at: list[NoteUpdatedAt] | core.ArrayOut[NoteUpdatedAt] | None = core.attr(
        NoteUpdatedAt, default=None, kind=core.Kind.array
    )

    note_updated_by: list[NoteUpdatedBy] | core.ArrayOut[NoteUpdatedBy] | None = core.attr(
        NoteUpdatedBy, default=None, kind=core.Kind.array
    )

    process_launched_at: list[ProcessLaunchedAt] | core.ArrayOut[
        ProcessLaunchedAt
    ] | None = core.attr(ProcessLaunchedAt, default=None, kind=core.Kind.array)

    process_name: list[ProcessName] | core.ArrayOut[ProcessName] | None = core.attr(
        ProcessName, default=None, kind=core.Kind.array
    )

    process_parent_pid: list[ProcessParentPid] | core.ArrayOut[ProcessParentPid] | None = core.attr(
        ProcessParentPid, default=None, kind=core.Kind.array
    )

    process_path: list[ProcessPath] | core.ArrayOut[ProcessPath] | None = core.attr(
        ProcessPath, default=None, kind=core.Kind.array
    )

    process_pid: list[ProcessPid] | core.ArrayOut[ProcessPid] | None = core.attr(
        ProcessPid, default=None, kind=core.Kind.array
    )

    process_terminated_at: list[ProcessTerminatedAt] | core.ArrayOut[
        ProcessTerminatedAt
    ] | None = core.attr(ProcessTerminatedAt, default=None, kind=core.Kind.array)

    product_arn: list[ProductArn] | core.ArrayOut[ProductArn] | None = core.attr(
        ProductArn, default=None, kind=core.Kind.array
    )

    product_fields: list[ProductFields] | core.ArrayOut[ProductFields] | None = core.attr(
        ProductFields, default=None, kind=core.Kind.array
    )

    product_name: list[ProductName] | core.ArrayOut[ProductName] | None = core.attr(
        ProductName, default=None, kind=core.Kind.array
    )

    recommendation_text: list[RecommendationText] | core.ArrayOut[
        RecommendationText
    ] | None = core.attr(RecommendationText, default=None, kind=core.Kind.array)

    record_state: list[RecordState] | core.ArrayOut[RecordState] | None = core.attr(
        RecordState, default=None, kind=core.Kind.array
    )

    related_findings_id: list[RelatedFindingsId] | core.ArrayOut[
        RelatedFindingsId
    ] | None = core.attr(RelatedFindingsId, default=None, kind=core.Kind.array)

    related_findings_product_arn: list[RelatedFindingsProductArn] | core.ArrayOut[
        RelatedFindingsProductArn
    ] | None = core.attr(RelatedFindingsProductArn, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_iam_instance_profile_arn: list[
        ResourceAwsEc2InstanceIamInstanceProfileArn
    ] | core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn] | None = core.attr(
        ResourceAwsEc2InstanceIamInstanceProfileArn, default=None, kind=core.Kind.array
    )

    resource_aws_ec2_instance_image_id: list[ResourceAwsEc2InstanceImageId] | core.ArrayOut[
        ResourceAwsEc2InstanceImageId
    ] | None = core.attr(ResourceAwsEc2InstanceImageId, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_ipv4_addresses: list[
        ResourceAwsEc2InstanceIpv4Addresses
    ] | core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses] | None = core.attr(
        ResourceAwsEc2InstanceIpv4Addresses, default=None, kind=core.Kind.array
    )

    resource_aws_ec2_instance_ipv6_addresses: list[
        ResourceAwsEc2InstanceIpv6Addresses
    ] | core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses] | None = core.attr(
        ResourceAwsEc2InstanceIpv6Addresses, default=None, kind=core.Kind.array
    )

    resource_aws_ec2_instance_key_name: list[ResourceAwsEc2InstanceKeyName] | core.ArrayOut[
        ResourceAwsEc2InstanceKeyName
    ] | None = core.attr(ResourceAwsEc2InstanceKeyName, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_launched_at: list[ResourceAwsEc2InstanceLaunchedAt] | core.ArrayOut[
        ResourceAwsEc2InstanceLaunchedAt
    ] | None = core.attr(ResourceAwsEc2InstanceLaunchedAt, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_subnet_id: list[ResourceAwsEc2InstanceSubnetId] | core.ArrayOut[
        ResourceAwsEc2InstanceSubnetId
    ] | None = core.attr(ResourceAwsEc2InstanceSubnetId, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_type: list[ResourceAwsEc2InstanceType] | core.ArrayOut[
        ResourceAwsEc2InstanceType
    ] | None = core.attr(ResourceAwsEc2InstanceType, default=None, kind=core.Kind.array)

    resource_aws_ec2_instance_vpc_id: list[ResourceAwsEc2InstanceVpcId] | core.ArrayOut[
        ResourceAwsEc2InstanceVpcId
    ] | None = core.attr(ResourceAwsEc2InstanceVpcId, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_created_at: list[ResourceAwsIamAccessKeyCreatedAt] | core.ArrayOut[
        ResourceAwsIamAccessKeyCreatedAt
    ] | None = core.attr(ResourceAwsIamAccessKeyCreatedAt, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_status: list[ResourceAwsIamAccessKeyStatus] | core.ArrayOut[
        ResourceAwsIamAccessKeyStatus
    ] | None = core.attr(ResourceAwsIamAccessKeyStatus, default=None, kind=core.Kind.array)

    resource_aws_iam_access_key_user_name: list[ResourceAwsIamAccessKeyUserName] | core.ArrayOut[
        ResourceAwsIamAccessKeyUserName
    ] | None = core.attr(ResourceAwsIamAccessKeyUserName, default=None, kind=core.Kind.array)

    resource_aws_s3_bucket_owner_id: list[ResourceAwsS3BucketOwnerId] | core.ArrayOut[
        ResourceAwsS3BucketOwnerId
    ] | None = core.attr(ResourceAwsS3BucketOwnerId, default=None, kind=core.Kind.array)

    resource_aws_s3_bucket_owner_name: list[ResourceAwsS3BucketOwnerName] | core.ArrayOut[
        ResourceAwsS3BucketOwnerName
    ] | None = core.attr(ResourceAwsS3BucketOwnerName, default=None, kind=core.Kind.array)

    resource_container_image_id: list[ResourceContainerImageId] | core.ArrayOut[
        ResourceContainerImageId
    ] | None = core.attr(ResourceContainerImageId, default=None, kind=core.Kind.array)

    resource_container_image_name: list[ResourceContainerImageName] | core.ArrayOut[
        ResourceContainerImageName
    ] | None = core.attr(ResourceContainerImageName, default=None, kind=core.Kind.array)

    resource_container_launched_at: list[ResourceContainerLaunchedAt] | core.ArrayOut[
        ResourceContainerLaunchedAt
    ] | None = core.attr(ResourceContainerLaunchedAt, default=None, kind=core.Kind.array)

    resource_container_name: list[ResourceContainerName] | core.ArrayOut[
        ResourceContainerName
    ] | None = core.attr(ResourceContainerName, default=None, kind=core.Kind.array)

    resource_details_other: list[ResourceDetailsOther] | core.ArrayOut[
        ResourceDetailsOther
    ] | None = core.attr(ResourceDetailsOther, default=None, kind=core.Kind.array)

    resource_id: list[ResourceId] | core.ArrayOut[ResourceId] | None = core.attr(
        ResourceId, default=None, kind=core.Kind.array
    )

    resource_partition: list[ResourcePartition] | core.ArrayOut[
        ResourcePartition
    ] | None = core.attr(ResourcePartition, default=None, kind=core.Kind.array)

    resource_region: list[ResourceRegion] | core.ArrayOut[ResourceRegion] | None = core.attr(
        ResourceRegion, default=None, kind=core.Kind.array
    )

    resource_tags: list[ResourceTags] | core.ArrayOut[ResourceTags] | None = core.attr(
        ResourceTags, default=None, kind=core.Kind.array
    )

    resource_type: list[ResourceType] | core.ArrayOut[ResourceType] | None = core.attr(
        ResourceType, default=None, kind=core.Kind.array
    )

    severity_label: list[SeverityLabel] | core.ArrayOut[SeverityLabel] | None = core.attr(
        SeverityLabel, default=None, kind=core.Kind.array
    )

    source_url: list[SourceUrl] | core.ArrayOut[SourceUrl] | None = core.attr(
        SourceUrl, default=None, kind=core.Kind.array
    )

    threat_intel_indicator_category: list[ThreatIntelIndicatorCategory] | core.ArrayOut[
        ThreatIntelIndicatorCategory
    ] | None = core.attr(ThreatIntelIndicatorCategory, default=None, kind=core.Kind.array)

    threat_intel_indicator_last_observed_at: list[
        ThreatIntelIndicatorLastObservedAt
    ] | core.ArrayOut[ThreatIntelIndicatorLastObservedAt] | None = core.attr(
        ThreatIntelIndicatorLastObservedAt, default=None, kind=core.Kind.array
    )

    threat_intel_indicator_source: list[ThreatIntelIndicatorSource] | core.ArrayOut[
        ThreatIntelIndicatorSource
    ] | None = core.attr(ThreatIntelIndicatorSource, default=None, kind=core.Kind.array)

    threat_intel_indicator_source_url: list[ThreatIntelIndicatorSourceUrl] | core.ArrayOut[
        ThreatIntelIndicatorSourceUrl
    ] | None = core.attr(ThreatIntelIndicatorSourceUrl, default=None, kind=core.Kind.array)

    threat_intel_indicator_type: list[ThreatIntelIndicatorType] | core.ArrayOut[
        ThreatIntelIndicatorType
    ] | None = core.attr(ThreatIntelIndicatorType, default=None, kind=core.Kind.array)

    threat_intel_indicator_value: list[ThreatIntelIndicatorValue] | core.ArrayOut[
        ThreatIntelIndicatorValue
    ] | None = core.attr(ThreatIntelIndicatorValue, default=None, kind=core.Kind.array)

    title: list[Title] | core.ArrayOut[Title] | None = core.attr(
        Title, default=None, kind=core.Kind.array
    )

    type: list[Type] | core.ArrayOut[Type] | None = core.attr(
        Type, default=None, kind=core.Kind.array
    )

    updated_at: list[UpdatedAt] | core.ArrayOut[UpdatedAt] | None = core.attr(
        UpdatedAt, default=None, kind=core.Kind.array
    )

    user_defined_values: list[UserDefinedValues] | core.ArrayOut[
        UserDefinedValues
    ] | None = core.attr(UserDefinedValues, default=None, kind=core.Kind.array)

    verification_state: list[VerificationState] | core.ArrayOut[
        VerificationState
    ] | None = core.attr(VerificationState, default=None, kind=core.Kind.array)

    workflow_status: list[WorkflowStatus] | core.ArrayOut[WorkflowStatus] | None = core.attr(
        WorkflowStatus, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        aws_account_id: list[AwsAccountId] | core.ArrayOut[AwsAccountId] | None = None,
        company_name: list[CompanyName] | core.ArrayOut[CompanyName] | None = None,
        compliance_status: list[ComplianceStatus] | core.ArrayOut[ComplianceStatus] | None = None,
        confidence: list[Confidence] | core.ArrayOut[Confidence] | None = None,
        created_at: list[CreatedAt] | core.ArrayOut[CreatedAt] | None = None,
        criticality: list[Criticality] | core.ArrayOut[Criticality] | None = None,
        description: list[Description] | core.ArrayOut[Description] | None = None,
        finding_provider_fields_confidence: list[FindingProviderFieldsConfidence]
        | core.ArrayOut[FindingProviderFieldsConfidence]
        | None = None,
        finding_provider_fields_criticality: list[FindingProviderFieldsCriticality]
        | core.ArrayOut[FindingProviderFieldsCriticality]
        | None = None,
        finding_provider_fields_related_findings_id: list[FindingProviderFieldsRelatedFindingsId]
        | core.ArrayOut[FindingProviderFieldsRelatedFindingsId]
        | None = None,
        finding_provider_fields_related_findings_product_arn: list[
            FindingProviderFieldsRelatedFindingsProductArn
        ]
        | core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn]
        | None = None,
        finding_provider_fields_severity_label: list[FindingProviderFieldsSeverityLabel]
        | core.ArrayOut[FindingProviderFieldsSeverityLabel]
        | None = None,
        finding_provider_fields_severity_original: list[FindingProviderFieldsSeverityOriginal]
        | core.ArrayOut[FindingProviderFieldsSeverityOriginal]
        | None = None,
        finding_provider_fields_types: list[FindingProviderFieldsTypes]
        | core.ArrayOut[FindingProviderFieldsTypes]
        | None = None,
        first_observed_at: list[FirstObservedAt] | core.ArrayOut[FirstObservedAt] | None = None,
        generator_id: list[GeneratorId] | core.ArrayOut[GeneratorId] | None = None,
        id: list[Id] | core.ArrayOut[Id] | None = None,
        keyword: list[Keyword] | core.ArrayOut[Keyword] | None = None,
        last_observed_at: list[LastObservedAt] | core.ArrayOut[LastObservedAt] | None = None,
        malware_name: list[MalwareName] | core.ArrayOut[MalwareName] | None = None,
        malware_path: list[MalwarePath] | core.ArrayOut[MalwarePath] | None = None,
        malware_state: list[MalwareState] | core.ArrayOut[MalwareState] | None = None,
        malware_type: list[MalwareType] | core.ArrayOut[MalwareType] | None = None,
        network_destination_domain: list[NetworkDestinationDomain]
        | core.ArrayOut[NetworkDestinationDomain]
        | None = None,
        network_destination_ipv4: list[NetworkDestinationIpv4]
        | core.ArrayOut[NetworkDestinationIpv4]
        | None = None,
        network_destination_ipv6: list[NetworkDestinationIpv6]
        | core.ArrayOut[NetworkDestinationIpv6]
        | None = None,
        network_destination_port: list[NetworkDestinationPort]
        | core.ArrayOut[NetworkDestinationPort]
        | None = None,
        network_direction: list[NetworkDirection] | core.ArrayOut[NetworkDirection] | None = None,
        network_protocol: list[NetworkProtocol] | core.ArrayOut[NetworkProtocol] | None = None,
        network_source_domain: list[NetworkSourceDomain]
        | core.ArrayOut[NetworkSourceDomain]
        | None = None,
        network_source_ipv4: list[NetworkSourceIpv4]
        | core.ArrayOut[NetworkSourceIpv4]
        | None = None,
        network_source_ipv6: list[NetworkSourceIpv6]
        | core.ArrayOut[NetworkSourceIpv6]
        | None = None,
        network_source_mac: list[NetworkSourceMac] | core.ArrayOut[NetworkSourceMac] | None = None,
        network_source_port: list[NetworkSourcePort]
        | core.ArrayOut[NetworkSourcePort]
        | None = None,
        note_text: list[NoteText] | core.ArrayOut[NoteText] | None = None,
        note_updated_at: list[NoteUpdatedAt] | core.ArrayOut[NoteUpdatedAt] | None = None,
        note_updated_by: list[NoteUpdatedBy] | core.ArrayOut[NoteUpdatedBy] | None = None,
        process_launched_at: list[ProcessLaunchedAt]
        | core.ArrayOut[ProcessLaunchedAt]
        | None = None,
        process_name: list[ProcessName] | core.ArrayOut[ProcessName] | None = None,
        process_parent_pid: list[ProcessParentPid] | core.ArrayOut[ProcessParentPid] | None = None,
        process_path: list[ProcessPath] | core.ArrayOut[ProcessPath] | None = None,
        process_pid: list[ProcessPid] | core.ArrayOut[ProcessPid] | None = None,
        process_terminated_at: list[ProcessTerminatedAt]
        | core.ArrayOut[ProcessTerminatedAt]
        | None = None,
        product_arn: list[ProductArn] | core.ArrayOut[ProductArn] | None = None,
        product_fields: list[ProductFields] | core.ArrayOut[ProductFields] | None = None,
        product_name: list[ProductName] | core.ArrayOut[ProductName] | None = None,
        recommendation_text: list[RecommendationText]
        | core.ArrayOut[RecommendationText]
        | None = None,
        record_state: list[RecordState] | core.ArrayOut[RecordState] | None = None,
        related_findings_id: list[RelatedFindingsId]
        | core.ArrayOut[RelatedFindingsId]
        | None = None,
        related_findings_product_arn: list[RelatedFindingsProductArn]
        | core.ArrayOut[RelatedFindingsProductArn]
        | None = None,
        resource_aws_ec2_instance_iam_instance_profile_arn: list[
            ResourceAwsEc2InstanceIamInstanceProfileArn
        ]
        | core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn]
        | None = None,
        resource_aws_ec2_instance_image_id: list[ResourceAwsEc2InstanceImageId]
        | core.ArrayOut[ResourceAwsEc2InstanceImageId]
        | None = None,
        resource_aws_ec2_instance_ipv4_addresses: list[ResourceAwsEc2InstanceIpv4Addresses]
        | core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses]
        | None = None,
        resource_aws_ec2_instance_ipv6_addresses: list[ResourceAwsEc2InstanceIpv6Addresses]
        | core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses]
        | None = None,
        resource_aws_ec2_instance_key_name: list[ResourceAwsEc2InstanceKeyName]
        | core.ArrayOut[ResourceAwsEc2InstanceKeyName]
        | None = None,
        resource_aws_ec2_instance_launched_at: list[ResourceAwsEc2InstanceLaunchedAt]
        | core.ArrayOut[ResourceAwsEc2InstanceLaunchedAt]
        | None = None,
        resource_aws_ec2_instance_subnet_id: list[ResourceAwsEc2InstanceSubnetId]
        | core.ArrayOut[ResourceAwsEc2InstanceSubnetId]
        | None = None,
        resource_aws_ec2_instance_type: list[ResourceAwsEc2InstanceType]
        | core.ArrayOut[ResourceAwsEc2InstanceType]
        | None = None,
        resource_aws_ec2_instance_vpc_id: list[ResourceAwsEc2InstanceVpcId]
        | core.ArrayOut[ResourceAwsEc2InstanceVpcId]
        | None = None,
        resource_aws_iam_access_key_created_at: list[ResourceAwsIamAccessKeyCreatedAt]
        | core.ArrayOut[ResourceAwsIamAccessKeyCreatedAt]
        | None = None,
        resource_aws_iam_access_key_status: list[ResourceAwsIamAccessKeyStatus]
        | core.ArrayOut[ResourceAwsIamAccessKeyStatus]
        | None = None,
        resource_aws_iam_access_key_user_name: list[ResourceAwsIamAccessKeyUserName]
        | core.ArrayOut[ResourceAwsIamAccessKeyUserName]
        | None = None,
        resource_aws_s3_bucket_owner_id: list[ResourceAwsS3BucketOwnerId]
        | core.ArrayOut[ResourceAwsS3BucketOwnerId]
        | None = None,
        resource_aws_s3_bucket_owner_name: list[ResourceAwsS3BucketOwnerName]
        | core.ArrayOut[ResourceAwsS3BucketOwnerName]
        | None = None,
        resource_container_image_id: list[ResourceContainerImageId]
        | core.ArrayOut[ResourceContainerImageId]
        | None = None,
        resource_container_image_name: list[ResourceContainerImageName]
        | core.ArrayOut[ResourceContainerImageName]
        | None = None,
        resource_container_launched_at: list[ResourceContainerLaunchedAt]
        | core.ArrayOut[ResourceContainerLaunchedAt]
        | None = None,
        resource_container_name: list[ResourceContainerName]
        | core.ArrayOut[ResourceContainerName]
        | None = None,
        resource_details_other: list[ResourceDetailsOther]
        | core.ArrayOut[ResourceDetailsOther]
        | None = None,
        resource_id: list[ResourceId] | core.ArrayOut[ResourceId] | None = None,
        resource_partition: list[ResourcePartition]
        | core.ArrayOut[ResourcePartition]
        | None = None,
        resource_region: list[ResourceRegion] | core.ArrayOut[ResourceRegion] | None = None,
        resource_tags: list[ResourceTags] | core.ArrayOut[ResourceTags] | None = None,
        resource_type: list[ResourceType] | core.ArrayOut[ResourceType] | None = None,
        severity_label: list[SeverityLabel] | core.ArrayOut[SeverityLabel] | None = None,
        source_url: list[SourceUrl] | core.ArrayOut[SourceUrl] | None = None,
        threat_intel_indicator_category: list[ThreatIntelIndicatorCategory]
        | core.ArrayOut[ThreatIntelIndicatorCategory]
        | None = None,
        threat_intel_indicator_last_observed_at: list[ThreatIntelIndicatorLastObservedAt]
        | core.ArrayOut[ThreatIntelIndicatorLastObservedAt]
        | None = None,
        threat_intel_indicator_source: list[ThreatIntelIndicatorSource]
        | core.ArrayOut[ThreatIntelIndicatorSource]
        | None = None,
        threat_intel_indicator_source_url: list[ThreatIntelIndicatorSourceUrl]
        | core.ArrayOut[ThreatIntelIndicatorSourceUrl]
        | None = None,
        threat_intel_indicator_type: list[ThreatIntelIndicatorType]
        | core.ArrayOut[ThreatIntelIndicatorType]
        | None = None,
        threat_intel_indicator_value: list[ThreatIntelIndicatorValue]
        | core.ArrayOut[ThreatIntelIndicatorValue]
        | None = None,
        title: list[Title] | core.ArrayOut[Title] | None = None,
        type: list[Type] | core.ArrayOut[Type] | None = None,
        updated_at: list[UpdatedAt] | core.ArrayOut[UpdatedAt] | None = None,
        user_defined_values: list[UserDefinedValues]
        | core.ArrayOut[UserDefinedValues]
        | None = None,
        verification_state: list[VerificationState]
        | core.ArrayOut[VerificationState]
        | None = None,
        workflow_status: list[WorkflowStatus] | core.ArrayOut[WorkflowStatus] | None = None,
    ):
        super().__init__(
            args=Filters.Args(
                aws_account_id=aws_account_id,
                company_name=company_name,
                compliance_status=compliance_status,
                confidence=confidence,
                created_at=created_at,
                criticality=criticality,
                description=description,
                finding_provider_fields_confidence=finding_provider_fields_confidence,
                finding_provider_fields_criticality=finding_provider_fields_criticality,
                finding_provider_fields_related_findings_id=finding_provider_fields_related_findings_id,
                finding_provider_fields_related_findings_product_arn=finding_provider_fields_related_findings_product_arn,
                finding_provider_fields_severity_label=finding_provider_fields_severity_label,
                finding_provider_fields_severity_original=finding_provider_fields_severity_original,
                finding_provider_fields_types=finding_provider_fields_types,
                first_observed_at=first_observed_at,
                generator_id=generator_id,
                id=id,
                keyword=keyword,
                last_observed_at=last_observed_at,
                malware_name=malware_name,
                malware_path=malware_path,
                malware_state=malware_state,
                malware_type=malware_type,
                network_destination_domain=network_destination_domain,
                network_destination_ipv4=network_destination_ipv4,
                network_destination_ipv6=network_destination_ipv6,
                network_destination_port=network_destination_port,
                network_direction=network_direction,
                network_protocol=network_protocol,
                network_source_domain=network_source_domain,
                network_source_ipv4=network_source_ipv4,
                network_source_ipv6=network_source_ipv6,
                network_source_mac=network_source_mac,
                network_source_port=network_source_port,
                note_text=note_text,
                note_updated_at=note_updated_at,
                note_updated_by=note_updated_by,
                process_launched_at=process_launched_at,
                process_name=process_name,
                process_parent_pid=process_parent_pid,
                process_path=process_path,
                process_pid=process_pid,
                process_terminated_at=process_terminated_at,
                product_arn=product_arn,
                product_fields=product_fields,
                product_name=product_name,
                recommendation_text=recommendation_text,
                record_state=record_state,
                related_findings_id=related_findings_id,
                related_findings_product_arn=related_findings_product_arn,
                resource_aws_ec2_instance_iam_instance_profile_arn=resource_aws_ec2_instance_iam_instance_profile_arn,
                resource_aws_ec2_instance_image_id=resource_aws_ec2_instance_image_id,
                resource_aws_ec2_instance_ipv4_addresses=resource_aws_ec2_instance_ipv4_addresses,
                resource_aws_ec2_instance_ipv6_addresses=resource_aws_ec2_instance_ipv6_addresses,
                resource_aws_ec2_instance_key_name=resource_aws_ec2_instance_key_name,
                resource_aws_ec2_instance_launched_at=resource_aws_ec2_instance_launched_at,
                resource_aws_ec2_instance_subnet_id=resource_aws_ec2_instance_subnet_id,
                resource_aws_ec2_instance_type=resource_aws_ec2_instance_type,
                resource_aws_ec2_instance_vpc_id=resource_aws_ec2_instance_vpc_id,
                resource_aws_iam_access_key_created_at=resource_aws_iam_access_key_created_at,
                resource_aws_iam_access_key_status=resource_aws_iam_access_key_status,
                resource_aws_iam_access_key_user_name=resource_aws_iam_access_key_user_name,
                resource_aws_s3_bucket_owner_id=resource_aws_s3_bucket_owner_id,
                resource_aws_s3_bucket_owner_name=resource_aws_s3_bucket_owner_name,
                resource_container_image_id=resource_container_image_id,
                resource_container_image_name=resource_container_image_name,
                resource_container_launched_at=resource_container_launched_at,
                resource_container_name=resource_container_name,
                resource_details_other=resource_details_other,
                resource_id=resource_id,
                resource_partition=resource_partition,
                resource_region=resource_region,
                resource_tags=resource_tags,
                resource_type=resource_type,
                severity_label=severity_label,
                source_url=source_url,
                threat_intel_indicator_category=threat_intel_indicator_category,
                threat_intel_indicator_last_observed_at=threat_intel_indicator_last_observed_at,
                threat_intel_indicator_source=threat_intel_indicator_source,
                threat_intel_indicator_source_url=threat_intel_indicator_source_url,
                threat_intel_indicator_type=threat_intel_indicator_type,
                threat_intel_indicator_value=threat_intel_indicator_value,
                title=title,
                type=type,
                updated_at=updated_at,
                user_defined_values=user_defined_values,
                verification_state=verification_state,
                workflow_status=workflow_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_account_id: list[AwsAccountId] | core.ArrayOut[AwsAccountId] | None = core.arg(
            default=None
        )

        company_name: list[CompanyName] | core.ArrayOut[CompanyName] | None = core.arg(default=None)

        compliance_status: list[ComplianceStatus] | core.ArrayOut[
            ComplianceStatus
        ] | None = core.arg(default=None)

        confidence: list[Confidence] | core.ArrayOut[Confidence] | None = core.arg(default=None)

        created_at: list[CreatedAt] | core.ArrayOut[CreatedAt] | None = core.arg(default=None)

        criticality: list[Criticality] | core.ArrayOut[Criticality] | None = core.arg(default=None)

        description: list[Description] | core.ArrayOut[Description] | None = core.arg(default=None)

        finding_provider_fields_confidence: list[FindingProviderFieldsConfidence] | core.ArrayOut[
            FindingProviderFieldsConfidence
        ] | None = core.arg(default=None)

        finding_provider_fields_criticality: list[FindingProviderFieldsCriticality] | core.ArrayOut[
            FindingProviderFieldsCriticality
        ] | None = core.arg(default=None)

        finding_provider_fields_related_findings_id: list[
            FindingProviderFieldsRelatedFindingsId
        ] | core.ArrayOut[FindingProviderFieldsRelatedFindingsId] | None = core.arg(default=None)

        finding_provider_fields_related_findings_product_arn: list[
            FindingProviderFieldsRelatedFindingsProductArn
        ] | core.ArrayOut[FindingProviderFieldsRelatedFindingsProductArn] | None = core.arg(
            default=None
        )

        finding_provider_fields_severity_label: list[
            FindingProviderFieldsSeverityLabel
        ] | core.ArrayOut[FindingProviderFieldsSeverityLabel] | None = core.arg(default=None)

        finding_provider_fields_severity_original: list[
            FindingProviderFieldsSeverityOriginal
        ] | core.ArrayOut[FindingProviderFieldsSeverityOriginal] | None = core.arg(default=None)

        finding_provider_fields_types: list[FindingProviderFieldsTypes] | core.ArrayOut[
            FindingProviderFieldsTypes
        ] | None = core.arg(default=None)

        first_observed_at: list[FirstObservedAt] | core.ArrayOut[FirstObservedAt] | None = core.arg(
            default=None
        )

        generator_id: list[GeneratorId] | core.ArrayOut[GeneratorId] | None = core.arg(default=None)

        id: list[Id] | core.ArrayOut[Id] | None = core.arg(default=None)

        keyword: list[Keyword] | core.ArrayOut[Keyword] | None = core.arg(default=None)

        last_observed_at: list[LastObservedAt] | core.ArrayOut[LastObservedAt] | None = core.arg(
            default=None
        )

        malware_name: list[MalwareName] | core.ArrayOut[MalwareName] | None = core.arg(default=None)

        malware_path: list[MalwarePath] | core.ArrayOut[MalwarePath] | None = core.arg(default=None)

        malware_state: list[MalwareState] | core.ArrayOut[MalwareState] | None = core.arg(
            default=None
        )

        malware_type: list[MalwareType] | core.ArrayOut[MalwareType] | None = core.arg(default=None)

        network_destination_domain: list[NetworkDestinationDomain] | core.ArrayOut[
            NetworkDestinationDomain
        ] | None = core.arg(default=None)

        network_destination_ipv4: list[NetworkDestinationIpv4] | core.ArrayOut[
            NetworkDestinationIpv4
        ] | None = core.arg(default=None)

        network_destination_ipv6: list[NetworkDestinationIpv6] | core.ArrayOut[
            NetworkDestinationIpv6
        ] | None = core.arg(default=None)

        network_destination_port: list[NetworkDestinationPort] | core.ArrayOut[
            NetworkDestinationPort
        ] | None = core.arg(default=None)

        network_direction: list[NetworkDirection] | core.ArrayOut[
            NetworkDirection
        ] | None = core.arg(default=None)

        network_protocol: list[NetworkProtocol] | core.ArrayOut[NetworkProtocol] | None = core.arg(
            default=None
        )

        network_source_domain: list[NetworkSourceDomain] | core.ArrayOut[
            NetworkSourceDomain
        ] | None = core.arg(default=None)

        network_source_ipv4: list[NetworkSourceIpv4] | core.ArrayOut[
            NetworkSourceIpv4
        ] | None = core.arg(default=None)

        network_source_ipv6: list[NetworkSourceIpv6] | core.ArrayOut[
            NetworkSourceIpv6
        ] | None = core.arg(default=None)

        network_source_mac: list[NetworkSourceMac] | core.ArrayOut[
            NetworkSourceMac
        ] | None = core.arg(default=None)

        network_source_port: list[NetworkSourcePort] | core.ArrayOut[
            NetworkSourcePort
        ] | None = core.arg(default=None)

        note_text: list[NoteText] | core.ArrayOut[NoteText] | None = core.arg(default=None)

        note_updated_at: list[NoteUpdatedAt] | core.ArrayOut[NoteUpdatedAt] | None = core.arg(
            default=None
        )

        note_updated_by: list[NoteUpdatedBy] | core.ArrayOut[NoteUpdatedBy] | None = core.arg(
            default=None
        )

        process_launched_at: list[ProcessLaunchedAt] | core.ArrayOut[
            ProcessLaunchedAt
        ] | None = core.arg(default=None)

        process_name: list[ProcessName] | core.ArrayOut[ProcessName] | None = core.arg(default=None)

        process_parent_pid: list[ProcessParentPid] | core.ArrayOut[
            ProcessParentPid
        ] | None = core.arg(default=None)

        process_path: list[ProcessPath] | core.ArrayOut[ProcessPath] | None = core.arg(default=None)

        process_pid: list[ProcessPid] | core.ArrayOut[ProcessPid] | None = core.arg(default=None)

        process_terminated_at: list[ProcessTerminatedAt] | core.ArrayOut[
            ProcessTerminatedAt
        ] | None = core.arg(default=None)

        product_arn: list[ProductArn] | core.ArrayOut[ProductArn] | None = core.arg(default=None)

        product_fields: list[ProductFields] | core.ArrayOut[ProductFields] | None = core.arg(
            default=None
        )

        product_name: list[ProductName] | core.ArrayOut[ProductName] | None = core.arg(default=None)

        recommendation_text: list[RecommendationText] | core.ArrayOut[
            RecommendationText
        ] | None = core.arg(default=None)

        record_state: list[RecordState] | core.ArrayOut[RecordState] | None = core.arg(default=None)

        related_findings_id: list[RelatedFindingsId] | core.ArrayOut[
            RelatedFindingsId
        ] | None = core.arg(default=None)

        related_findings_product_arn: list[RelatedFindingsProductArn] | core.ArrayOut[
            RelatedFindingsProductArn
        ] | None = core.arg(default=None)

        resource_aws_ec2_instance_iam_instance_profile_arn: list[
            ResourceAwsEc2InstanceIamInstanceProfileArn
        ] | core.ArrayOut[ResourceAwsEc2InstanceIamInstanceProfileArn] | None = core.arg(
            default=None
        )

        resource_aws_ec2_instance_image_id: list[ResourceAwsEc2InstanceImageId] | core.ArrayOut[
            ResourceAwsEc2InstanceImageId
        ] | None = core.arg(default=None)

        resource_aws_ec2_instance_ipv4_addresses: list[
            ResourceAwsEc2InstanceIpv4Addresses
        ] | core.ArrayOut[ResourceAwsEc2InstanceIpv4Addresses] | None = core.arg(default=None)

        resource_aws_ec2_instance_ipv6_addresses: list[
            ResourceAwsEc2InstanceIpv6Addresses
        ] | core.ArrayOut[ResourceAwsEc2InstanceIpv6Addresses] | None = core.arg(default=None)

        resource_aws_ec2_instance_key_name: list[ResourceAwsEc2InstanceKeyName] | core.ArrayOut[
            ResourceAwsEc2InstanceKeyName
        ] | None = core.arg(default=None)

        resource_aws_ec2_instance_launched_at: list[
            ResourceAwsEc2InstanceLaunchedAt
        ] | core.ArrayOut[ResourceAwsEc2InstanceLaunchedAt] | None = core.arg(default=None)

        resource_aws_ec2_instance_subnet_id: list[ResourceAwsEc2InstanceSubnetId] | core.ArrayOut[
            ResourceAwsEc2InstanceSubnetId
        ] | None = core.arg(default=None)

        resource_aws_ec2_instance_type: list[ResourceAwsEc2InstanceType] | core.ArrayOut[
            ResourceAwsEc2InstanceType
        ] | None = core.arg(default=None)

        resource_aws_ec2_instance_vpc_id: list[ResourceAwsEc2InstanceVpcId] | core.ArrayOut[
            ResourceAwsEc2InstanceVpcId
        ] | None = core.arg(default=None)

        resource_aws_iam_access_key_created_at: list[
            ResourceAwsIamAccessKeyCreatedAt
        ] | core.ArrayOut[ResourceAwsIamAccessKeyCreatedAt] | None = core.arg(default=None)

        resource_aws_iam_access_key_status: list[ResourceAwsIamAccessKeyStatus] | core.ArrayOut[
            ResourceAwsIamAccessKeyStatus
        ] | None = core.arg(default=None)

        resource_aws_iam_access_key_user_name: list[
            ResourceAwsIamAccessKeyUserName
        ] | core.ArrayOut[ResourceAwsIamAccessKeyUserName] | None = core.arg(default=None)

        resource_aws_s3_bucket_owner_id: list[ResourceAwsS3BucketOwnerId] | core.ArrayOut[
            ResourceAwsS3BucketOwnerId
        ] | None = core.arg(default=None)

        resource_aws_s3_bucket_owner_name: list[ResourceAwsS3BucketOwnerName] | core.ArrayOut[
            ResourceAwsS3BucketOwnerName
        ] | None = core.arg(default=None)

        resource_container_image_id: list[ResourceContainerImageId] | core.ArrayOut[
            ResourceContainerImageId
        ] | None = core.arg(default=None)

        resource_container_image_name: list[ResourceContainerImageName] | core.ArrayOut[
            ResourceContainerImageName
        ] | None = core.arg(default=None)

        resource_container_launched_at: list[ResourceContainerLaunchedAt] | core.ArrayOut[
            ResourceContainerLaunchedAt
        ] | None = core.arg(default=None)

        resource_container_name: list[ResourceContainerName] | core.ArrayOut[
            ResourceContainerName
        ] | None = core.arg(default=None)

        resource_details_other: list[ResourceDetailsOther] | core.ArrayOut[
            ResourceDetailsOther
        ] | None = core.arg(default=None)

        resource_id: list[ResourceId] | core.ArrayOut[ResourceId] | None = core.arg(default=None)

        resource_partition: list[ResourcePartition] | core.ArrayOut[
            ResourcePartition
        ] | None = core.arg(default=None)

        resource_region: list[ResourceRegion] | core.ArrayOut[ResourceRegion] | None = core.arg(
            default=None
        )

        resource_tags: list[ResourceTags] | core.ArrayOut[ResourceTags] | None = core.arg(
            default=None
        )

        resource_type: list[ResourceType] | core.ArrayOut[ResourceType] | None = core.arg(
            default=None
        )

        severity_label: list[SeverityLabel] | core.ArrayOut[SeverityLabel] | None = core.arg(
            default=None
        )

        source_url: list[SourceUrl] | core.ArrayOut[SourceUrl] | None = core.arg(default=None)

        threat_intel_indicator_category: list[ThreatIntelIndicatorCategory] | core.ArrayOut[
            ThreatIntelIndicatorCategory
        ] | None = core.arg(default=None)

        threat_intel_indicator_last_observed_at: list[
            ThreatIntelIndicatorLastObservedAt
        ] | core.ArrayOut[ThreatIntelIndicatorLastObservedAt] | None = core.arg(default=None)

        threat_intel_indicator_source: list[ThreatIntelIndicatorSource] | core.ArrayOut[
            ThreatIntelIndicatorSource
        ] | None = core.arg(default=None)

        threat_intel_indicator_source_url: list[ThreatIntelIndicatorSourceUrl] | core.ArrayOut[
            ThreatIntelIndicatorSourceUrl
        ] | None = core.arg(default=None)

        threat_intel_indicator_type: list[ThreatIntelIndicatorType] | core.ArrayOut[
            ThreatIntelIndicatorType
        ] | None = core.arg(default=None)

        threat_intel_indicator_value: list[ThreatIntelIndicatorValue] | core.ArrayOut[
            ThreatIntelIndicatorValue
        ] | None = core.arg(default=None)

        title: list[Title] | core.ArrayOut[Title] | None = core.arg(default=None)

        type: list[Type] | core.ArrayOut[Type] | None = core.arg(default=None)

        updated_at: list[UpdatedAt] | core.ArrayOut[UpdatedAt] | None = core.arg(default=None)

        user_defined_values: list[UserDefinedValues] | core.ArrayOut[
            UserDefinedValues
        ] | None = core.arg(default=None)

        verification_state: list[VerificationState] | core.ArrayOut[
            VerificationState
        ] | None = core.arg(default=None)

        workflow_status: list[WorkflowStatus] | core.ArrayOut[WorkflowStatus] | None = core.arg(
            default=None
        )


@core.resource(type="aws_securityhub_insight", namespace="securityhub")
class Insight(core.Resource):
    """
    ARN of the insight.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A configuration block including one or more (up to 10 distinct) attributes used to filter
    the findings included in the insight. The insight only includes findings that match criteria define
    d in the filters. See [filters](#filters) below for more details.
    """
    filters: Filters = core.attr(Filters)

    """
    (Required) The attribute used to group the findings for the insight e.g., if an insight is grouped b
    y `ResourceId`, then the insight produces a list of resource identifiers.
    """
    group_by_attribute: str | core.StringOut = core.attr(str)

    """
    (Optional) The security findings provider-specific identifier for a finding. See [String Filter](#st
    ring-filter-argument-reference) below for more details.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the custom insight.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        filters: Filters,
        group_by_attribute: str | core.StringOut,
        name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Insight.Args(
                filters=filters,
                group_by_attribute=group_by_attribute,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filters: Filters = core.arg()

        group_by_attribute: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()
