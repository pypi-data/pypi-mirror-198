import terrascript.core as core


@core.schema
class AuditLogs(core.Schema):

    enable: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enable: bool | core.BoolOut,
    ):
        super().__init__(
            args=AuditLogs.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: bool | core.BoolOut = core.arg()


@core.schema
class Kubernetes(core.Schema):

    audit_logs: AuditLogs = core.attr(AuditLogs)

    def __init__(
        self,
        *,
        audit_logs: AuditLogs,
    ):
        super().__init__(
            args=Kubernetes.Args(
                audit_logs=audit_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit_logs: AuditLogs = core.arg()


@core.schema
class EbsVolumes(core.Schema):

    enable: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enable: bool | core.BoolOut,
    ):
        super().__init__(
            args=EbsVolumes.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: bool | core.BoolOut = core.arg()


@core.schema
class ScanEc2InstanceWithFindings(core.Schema):

    ebs_volumes: EbsVolumes = core.attr(EbsVolumes)

    def __init__(
        self,
        *,
        ebs_volumes: EbsVolumes,
    ):
        super().__init__(
            args=ScanEc2InstanceWithFindings.Args(
                ebs_volumes=ebs_volumes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_volumes: EbsVolumes = core.arg()


@core.schema
class MalwareProtection(core.Schema):

    scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings = core.attr(
        ScanEc2InstanceWithFindings
    )

    def __init__(
        self,
        *,
        scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings,
    ):
        super().__init__(
            args=MalwareProtection.Args(
                scan_ec2_instance_with_findings=scan_ec2_instance_with_findings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scan_ec2_instance_with_findings: ScanEc2InstanceWithFindings = core.arg()


@core.schema
class S3Logs(core.Schema):

    enable: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enable: bool | core.BoolOut,
    ):
        super().__init__(
            args=S3Logs.Args(
                enable=enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: bool | core.BoolOut = core.arg()


@core.schema
class Datasources(core.Schema):

    kubernetes: Kubernetes | None = core.attr(Kubernetes, default=None, computed=True)

    malware_protection: MalwareProtection | None = core.attr(
        MalwareProtection, default=None, computed=True
    )

    s3_logs: S3Logs | None = core.attr(S3Logs, default=None, computed=True)

    def __init__(
        self,
        *,
        kubernetes: Kubernetes | None = None,
        malware_protection: MalwareProtection | None = None,
        s3_logs: S3Logs | None = None,
    ):
        super().__init__(
            args=Datasources.Args(
                kubernetes=kubernetes,
                malware_protection=malware_protection,
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kubernetes: Kubernetes | None = core.arg(default=None)

        malware_protection: MalwareProtection | None = core.arg(default=None)

        s3_logs: S3Logs | None = core.arg(default=None)


@core.resource(type="aws_guardduty_detector", namespace="guardduty")
class Detector(core.Resource):
    """
    The AWS account ID of the GuardDuty detector
    """

    account_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the GuardDuty detector
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Describes which data sources will be enabled for the detector. See [Data Sources](#data-s
    ources) below for more details.
    """
    datasources: Datasources | None = core.attr(Datasources, default=None, computed=True)

    """
    (Optional) Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending
    " GuardDuty. Defaults to `true`.
    """
    enable: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies the frequency of notifications sent for subsequent finding occurrences. If the
    detector is a GuardDuty member account, the value is determined by the GuardDuty primary account and
    cannot be modified, otherwise defaults to `SIX_HOURS`. For standalone and GuardDuty primary account
    s, it must be configured in Terraform to enable drift detection. Valid values for standalone and pri
    mary accounts: `FIFTEEN_MINUTES`, `ONE_HOUR`, `SIX_HOURS`. See [AWS Documentation](https://docs.aws.
    amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html#guardduty_findings_cloudwatch_noti
    fication_frequency) for more information.
    """
    finding_publishing_frequency: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    The ID of the GuardDuty detector
    """
    id: str | core.StringOut = core.attr(str, computed=True)

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
        datasources: Datasources | None = None,
        enable: bool | core.BoolOut | None = None,
        finding_publishing_frequency: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Detector.Args(
                datasources=datasources,
                enable=enable,
                finding_publishing_frequency=finding_publishing_frequency,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        datasources: Datasources | None = core.arg(default=None)

        enable: bool | core.BoolOut | None = core.arg(default=None)

        finding_publishing_frequency: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
