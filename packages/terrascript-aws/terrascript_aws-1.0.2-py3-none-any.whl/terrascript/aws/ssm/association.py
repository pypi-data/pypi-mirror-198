import terrascript.core as core


@core.schema
class Targets(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class OutputLocation(core.Schema):

    s3_bucket_name: str | core.StringOut = core.attr(str)

    s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    s3_region: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_bucket_name: str | core.StringOut,
        s3_key_prefix: str | core.StringOut | None = None,
        s3_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=OutputLocation.Args(
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
                s3_region=s3_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_name: str | core.StringOut = core.arg()

        s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_region: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_ssm_association", namespace="aws_ssm")
class Association(core.Resource):

    apply_only_at_cron_interval: bool | core.BoolOut | None = core.attr(bool, default=None)

    arn: str | core.StringOut = core.attr(str, computed=True)

    association_id: str | core.StringOut = core.attr(str, computed=True)

    association_name: str | core.StringOut | None = core.attr(str, default=None)

    automation_target_parameter_name: str | core.StringOut | None = core.attr(str, default=None)

    compliance_severity: str | core.StringOut | None = core.attr(str, default=None)

    document_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_id: str | core.StringOut | None = core.attr(str, default=None)

    max_concurrency: str | core.StringOut | None = core.attr(str, default=None)

    max_errors: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut = core.attr(str)

    output_location: OutputLocation | None = core.attr(OutputLocation, default=None)

    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    schedule_expression: str | core.StringOut | None = core.attr(str, default=None)

    targets: list[Targets] | core.ArrayOut[Targets] | None = core.attr(
        Targets, default=None, computed=True, kind=core.Kind.array
    )

    wait_for_success_timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        apply_only_at_cron_interval: bool | core.BoolOut | None = None,
        association_name: str | core.StringOut | None = None,
        automation_target_parameter_name: str | core.StringOut | None = None,
        compliance_severity: str | core.StringOut | None = None,
        document_version: str | core.StringOut | None = None,
        instance_id: str | core.StringOut | None = None,
        max_concurrency: str | core.StringOut | None = None,
        max_errors: str | core.StringOut | None = None,
        output_location: OutputLocation | None = None,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        schedule_expression: str | core.StringOut | None = None,
        targets: list[Targets] | core.ArrayOut[Targets] | None = None,
        wait_for_success_timeout_seconds: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Association.Args(
                name=name,
                apply_only_at_cron_interval=apply_only_at_cron_interval,
                association_name=association_name,
                automation_target_parameter_name=automation_target_parameter_name,
                compliance_severity=compliance_severity,
                document_version=document_version,
                instance_id=instance_id,
                max_concurrency=max_concurrency,
                max_errors=max_errors,
                output_location=output_location,
                parameters=parameters,
                schedule_expression=schedule_expression,
                targets=targets,
                wait_for_success_timeout_seconds=wait_for_success_timeout_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_only_at_cron_interval: bool | core.BoolOut | None = core.arg(default=None)

        association_name: str | core.StringOut | None = core.arg(default=None)

        automation_target_parameter_name: str | core.StringOut | None = core.arg(default=None)

        compliance_severity: str | core.StringOut | None = core.arg(default=None)

        document_version: str | core.StringOut | None = core.arg(default=None)

        instance_id: str | core.StringOut | None = core.arg(default=None)

        max_concurrency: str | core.StringOut | None = core.arg(default=None)

        max_errors: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        output_location: OutputLocation | None = core.arg(default=None)

        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        schedule_expression: str | core.StringOut | None = core.arg(default=None)

        targets: list[Targets] | core.ArrayOut[Targets] | None = core.arg(default=None)

        wait_for_success_timeout_seconds: int | core.IntOut | None = core.arg(default=None)
