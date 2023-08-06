import terrascript.core as core


@core.resource(type="aws_db_instance_automated_backups_replication", namespace="aws_rds")
class DbInstanceAutomatedBackupsReplication(core.Resource):
    """
    The Amazon Resource Name (ARN) of the replicated automated backups.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional, Forces new resource) The AWS KMS key identifier for encryption of the replicated automate
    d backups. The KMS key ID is the Amazon Resource Name (ARN) for the KMS encryption key in the destin
    ation AWS Region, for example, `arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE`.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional, Forces new resource) A URL that contains a [Signature Version 4](https://docs.aws.amazon.
    com/general/latest/gr/signature-version-4.html) signed request for the [`StartDBInstanceAutomatedBac
    kupsReplication`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstanceAutom
    atedBackupsReplication.html) action to be called in the AWS Region of the source DB instance.
    """
    pre_signed_url: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Forces new resource) The retention period for the replicated automated backups, defaults
    to `7`.
    """
    retention_period: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the source DB instance for the rep
    licated automated backups, for example, `arn:aws:rds:us-west-2:123456789012:db:mydatabase`.
    """
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
