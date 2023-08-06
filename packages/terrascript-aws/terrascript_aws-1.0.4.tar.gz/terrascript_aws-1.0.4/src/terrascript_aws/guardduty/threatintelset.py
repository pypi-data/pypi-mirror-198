import terrascript.core as core


@core.resource(type="aws_guardduty_threatintelset", namespace="guardduty")
class Threatintelset(core.Resource):
    """
    (Required) Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.
    """

    activate: bool | core.BoolOut = core.attr(bool)

    """
    Amazon Resource Name (ARN) of the GuardDuty ThreatIntelSet.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The detector ID of the GuardDuty.
    """
    detector_id: str | core.StringOut = core.attr(str)

    """
    (Required) The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `
    OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`
    """
    format: str | core.StringOut = core.attr(str)

    """
    The ID of the GuardDuty ThreatIntelSet and the detector ID. Format: `<DetectorID>:<ThreatIntelSetID>
    
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The URI of the file that contains the ThreatIntelSet.
    """
    location: str | core.StringOut = core.attr(str)

    """
    (Required) The friendly name to identify the ThreatIntelSet.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        activate: bool | core.BoolOut,
        detector_id: str | core.StringOut,
        format: str | core.StringOut,
        location: str | core.StringOut,
        name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Threatintelset.Args(
                activate=activate,
                detector_id=detector_id,
                format=format,
                location=location,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activate: bool | core.BoolOut = core.arg()

        detector_id: str | core.StringOut = core.arg()

        format: str | core.StringOut = core.arg()

        location: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
