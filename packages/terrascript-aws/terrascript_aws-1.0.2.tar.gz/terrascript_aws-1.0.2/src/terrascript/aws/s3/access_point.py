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


@core.resource(type="aws_s3_access_point", namespace="aws_s3")
class AccessPoint(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    alias: str | core.StringOut = core.attr(str, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    bucket: str | core.StringOut = core.attr(str)

    domain_name: str | core.StringOut = core.attr(str, computed=True)

    endpoints: dict[str, str] | core.MapOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    has_public_access_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    network_origin: str | core.StringOut = core.attr(str, computed=True)

    policy: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    public_access_block_configuration: PublicAccessBlockConfiguration | None = core.attr(
        PublicAccessBlockConfiguration, default=None
    )

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
