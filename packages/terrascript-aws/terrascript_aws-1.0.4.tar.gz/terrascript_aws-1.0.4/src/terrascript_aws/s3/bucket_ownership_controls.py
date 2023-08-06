import terrascript.core as core


@core.schema
class Rule(core.Schema):

    object_ownership: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        object_ownership: str | core.StringOut,
    ):
        super().__init__(
            args=Rule.Args(
                object_ownership=object_ownership,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_ownership: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_ownership_controls", namespace="s3")
class BucketOwnershipControls(core.Resource):
    """
    (Required) The name of the bucket that you want to associate this access point with.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    S3 Bucket name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration block(s) with Ownership Controls rules. Detailed below.
    """
    rule: Rule = core.attr(Rule)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        rule: Rule,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketOwnershipControls.Args(
                bucket=bucket,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        rule: Rule = core.arg()
