import terrascript.core as core


@core.schema
class S3Logs(core.Schema):

    auto_enable: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        auto_enable: bool | core.BoolOut,
    ):
        super().__init__(
            args=S3Logs.Args(
                auto_enable=auto_enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_enable: bool | core.BoolOut = core.arg()


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

    auto_enable: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        auto_enable: bool | core.BoolOut,
    ):
        super().__init__(
            args=EbsVolumes.Args(
                auto_enable=auto_enable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_enable: bool | core.BoolOut = core.arg()


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


@core.resource(type="aws_guardduty_organization_configuration", namespace="guardduty")
class OrganizationConfiguration(core.Resource):
    """
    (Required) When this setting is enabled, all new accounts that are created in, or added to, the orga
    nization are added as a member accounts of the organization’s GuardDuty delegated administrator and
    GuardDuty is enabled in that AWS Region.
    """

    auto_enable: bool | core.BoolOut = core.attr(bool)

    """
    (Optional) Configuration for the collected datasources.
    """
    datasources: Datasources | None = core.attr(Datasources, default=None, computed=True)

    """
    (Required) The detector ID of the GuardDuty account.
    """
    detector_id: str | core.StringOut = core.attr(str)

    """
    Identifier of the GuardDuty Detector.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auto_enable: bool | core.BoolOut,
        detector_id: str | core.StringOut,
        datasources: Datasources | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConfiguration.Args(
                auto_enable=auto_enable,
                detector_id=detector_id,
                datasources=datasources,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_enable: bool | core.BoolOut = core.arg()

        datasources: Datasources | None = core.arg(default=None)

        detector_id: str | core.StringOut = core.arg()
