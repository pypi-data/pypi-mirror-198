import terrascript.core as core


@core.schema
class ClassificationType(core.Schema):

    continuous: str | core.StringOut | None = core.attr(str, default=None)

    one_time: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continuous: str | core.StringOut | None = None,
        one_time: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ClassificationType.Args(
                continuous=continuous,
                one_time=one_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continuous: str | core.StringOut | None = core.arg(default=None)

        one_time: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_macie_s3_bucket_association", namespace="macie")
class S3BucketAssociation(core.Resource):
    """
    (Required) The name of the S3 bucket that you want to associate with Amazon Macie.
    """

    bucket_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The configuration of how Amazon Macie classifies the S3 objects.
    """
    classification_type: ClassificationType | None = core.attr(
        ClassificationType, default=None, computed=True
    )

    """
    The ID of the association.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID of the Amazon Macie member account whose S3 resources you want to associate with M
    acie. If `member_account_id` isn't specified, the action associates specified S3 resources with Maci
    e for the current master account.
    """
    member_account_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Object key prefix identifying one or more S3 objects to which the association applies.
    """
    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket_name: str | core.StringOut,
        classification_type: ClassificationType | None = None,
        member_account_id: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=S3BucketAssociation.Args(
                bucket_name=bucket_name,
                classification_type=classification_type,
                member_account_id=member_account_id,
                prefix=prefix,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket_name: str | core.StringOut = core.arg()

        classification_type: ClassificationType | None = core.arg(default=None)

        member_account_id: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)
