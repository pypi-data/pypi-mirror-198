import terrascript.core as core


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


@core.resource(type="aws_guardduty_detector", namespace="aws_guardduty")
class Detector(core.Resource):

    account_id: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    datasources: Datasources | None = core.attr(Datasources, default=None, computed=True)

    enable: bool | core.BoolOut | None = core.attr(bool, default=None)

    finding_publishing_frequency: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

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
