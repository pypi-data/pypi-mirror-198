import terrascript.core as core


@core.resource(type="aws_db_instance_automated_backups_replication", namespace="rds")
class DbInstanceAutomatedBackupsReplication(core.Resource):

    id: str | core.StringOut = core.attr(str, computed=True)

    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    pre_signed_url: str | core.StringOut | None = core.attr(str, default=None)

    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    source_db_instance_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        source_db_instance_arn: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
        pre_signed_url: str | core.StringOut | None = None,
        retention_period: int | core.IntOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbInstanceAutomatedBackupsReplication.Args(
                source_db_instance_arn=source_db_instance_arn,
                kms_key_id=kms_key_id,
                pre_signed_url=pre_signed_url,
                retention_period=retention_period,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        pre_signed_url: str | core.StringOut | None = core.arg(default=None)

        retention_period: int | core.IntOut | None = core.arg(default=None)

        source_db_instance_arn: str | core.StringOut = core.arg()
