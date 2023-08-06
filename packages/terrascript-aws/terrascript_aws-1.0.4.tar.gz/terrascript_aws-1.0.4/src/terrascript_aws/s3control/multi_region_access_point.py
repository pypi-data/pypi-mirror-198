import terrascript.core as core


@core.schema
class PublicAccessBlock(core.Schema):

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
            args=PublicAccessBlock.Args(
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


@core.schema
class Region(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
    ):
        super().__init__(
            args=Region.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()


@core.schema
class Details(core.Schema):

    name: str | core.StringOut = core.attr(str)

    public_access_block: PublicAccessBlock | None = core.attr(PublicAccessBlock, default=None)

    region: list[Region] | core.ArrayOut[Region] = core.attr(Region, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        region: list[Region] | core.ArrayOut[Region],
        public_access_block: PublicAccessBlock | None = None,
    ):
        super().__init__(
            args=Details.Args(
                name=name,
                region=region,
                public_access_block=public_access_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        public_access_block: PublicAccessBlock | None = core.arg(default=None)

        region: list[Region] | core.ArrayOut[Region] = core.arg()


@core.resource(type="aws_s3control_multi_region_access_point", namespace="s3control")
class MultiRegionAccessPoint(core.Resource):
    """
    (Optional) The AWS account ID for the owner of the buckets for which you want to create a Multi-Regi
    on Access Point. Defaults to automatically determined account ID of the Terraform AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The alias for the Multi-Region Access Point.
    """
    alias: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the Multi-Region Access Point.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A configuration block containing details about the Multi-Region Access Point. See [Detail
    s Configuration Block](#details-configuration) below for more details
    """
    details: Details = core.attr(Details)

    """
    The DNS domain name of the S3 Multi-Region Access Point in the format _`alias`_.accesspoint.s3-globa
    l.amazonaws.com. For more information, see the documentation on [Multi-Region Access Point Requests]
    (https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRequests.html).
    """
    domain_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID and access point name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The current status of the Multi-Region Access Point. One of: `READY`, `INCONSISTENT_ACROSS_REGIONS`,
    CREATING`, `PARTIALLY_CREATED`, `PARTIALLY_DELETED`, `DELETING`.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        details: Details,
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MultiRegionAccessPoint.Args(
                details=details,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        details: Details = core.arg()
