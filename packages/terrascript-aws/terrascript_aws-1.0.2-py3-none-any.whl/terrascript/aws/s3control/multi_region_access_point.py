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


@core.resource(type="aws_s3control_multi_region_access_point", namespace="aws_s3control")
class MultiRegionAccessPoint(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    alias: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    details: Details = core.attr(Details)

    domain_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
