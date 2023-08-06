import terrascript.core as core


@core.schema
class VpcConfiguration(core.Schema):

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        vpc_id: str | core.StringOut,
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_id: str | core.StringOut = core.arg()


@core.schema
class PublicAccessBlockConfiguration(core.Schema):

    block_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    block_public_policy: bool | core.BoolOut | None = core.attr(bool, default=None)

    ignore_public_acls: bool | core.BoolOut | None = core.attr(bool, default=None)

    restrict_public_buckets: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        block_public_acls: bool | core.BoolOut | None = None,
        block_public_policy: bool | core.BoolOut | None = None,
        ignore_public_acls: bool | core.BoolOut | None = None,
        restrict_public_buckets: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=PublicAccessBlockConfiguration.Args(
                block_public_acls=block_public_acls,
                block_public_policy=block_public_policy,
                ignore_public_acls=ignore_public_acls,
                restrict_public_buckets=restrict_public_buckets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        block_public_policy: bool | core.BoolOut | None = core.arg(default=None)

        ignore_public_acls: bool | core.BoolOut | None = core.arg(default=None)

        restrict_public_buckets: bool | core.BoolOut | None = core.arg(default=None)


@core.resource(type="aws_s3_access_point", namespace="s3")
class AccessPoint(core.Resource):
    """
    (Optional) AWS account ID for the owner of the bucket for which you want to create an access point.
    Defaults to automatically determined account ID of the Terraform AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The alias of the S3 Access Point.
    """
    alias: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the S3 Access Point.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bu
    cket that you want to associate this access point with.
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._reg
    ion_.amazonaws.com.
    """
    domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The VPC endpoints for the S3 Access Point.
    """
    endpoints: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    """
    Indicates whether this access point currently has a policy that allows public access.
    """
    has_public_access_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    For Access Point of an AWS Partition S3 Bucket, the AWS account ID and access point name separated b
    y a colon (`:`). For S3 on Outposts Bucket, the Amazon Resource Name (ARN) of the Access Point.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Name you want to assign to this access point.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Indicates whether this access point allows access from the public Internet. Values are `VPC` (the ac
    cess point doesn't allow access from the public Internet) and `Internet` (the access point allows ac
    cess from the public Internet, subject to the access point and bucket access policies).
    """
    network_origin: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Valid JSON document that specifies the policy that you want to apply to this access point
    . Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `p
    olicy = ""`) _will not_ delete the policy since it could have been set by `aws_s3control_access_poin
    t_policy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
    """
    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Configuration block to manage the `PublicAccessBlock` configuration that you want to appl
    y to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed be
    low.
    """
    public_access_block_configuration: PublicAccessBlockConfiguration | None = core.attr(
        PublicAccessBlockConfiguration, default=None
    )

    """
    (Optional) Configuration block to restrict access to this access point to requests from the specifie
    d Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
    """
    vpc_configuration: VpcConfiguration | None = core.attr(VpcConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        name: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        public_access_block_configuration: PublicAccessBlockConfiguration | None = None,
        vpc_configuration: VpcConfiguration | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPoint.Args(
                bucket=bucket,
                name=name,
                account_id=account_id,
                policy=policy,
                public_access_block_configuration=public_access_block_configuration,
                vpc_configuration=vpc_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut | None = core.arg(default=None)

        public_access_block_configuration: PublicAccessBlockConfiguration | None = core.arg(
            default=None
        )

        vpc_configuration: VpcConfiguration | None = core.arg(default=None)
