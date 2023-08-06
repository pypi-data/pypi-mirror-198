import terrascript.core as core


@core.schema
class Grantee(core.Schema):

    display_name: str | core.StringOut = core.attr(str, computed=True)

    email_address: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        display_name: str | core.StringOut,
        type: str | core.StringOut,
        email_address: str | core.StringOut | None = None,
        id: str | core.StringOut | None = None,
        uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Grantee.Args(
                display_name=display_name,
                type=type,
                email_address=email_address,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: str | core.StringOut = core.arg()

        email_address: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        uri: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetGrant(core.Schema):

    grantee: Grantee = core.attr(Grantee)

    permission: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        grantee: Grantee,
        permission: str | core.StringOut,
    ):
        super().__init__(
            args=TargetGrant.Args(
                grantee=grantee,
                permission=permission,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grantee: Grantee = core.arg()

        permission: str | core.StringOut = core.arg()


@core.resource(type="aws_s3_bucket_logging", namespace="s3")
class BucketLogging(core.Resource):
    """
    (Required, Forces new resource) The name of the bucket.
    """

    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The canonical user ID of the grantee.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the bucket where you want Amazon S3 to store server access logs.
    """
    target_bucket: str | core.StringOut = core.attr(str)

    """
    (Optional) Set of configuration blocks with information for granting permissions [documented below](
    #target_grant).
    """
    target_grant: list[TargetGrant] | core.ArrayOut[TargetGrant] | None = core.attr(
        TargetGrant, default=None, kind=core.Kind.array
    )

    """
    (Required) A prefix for all log object keys.
    """
    target_prefix: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        target_bucket: str | core.StringOut,
        target_prefix: str | core.StringOut,
        expected_bucket_owner: str | core.StringOut | None = None,
        target_grant: list[TargetGrant] | core.ArrayOut[TargetGrant] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketLogging.Args(
                bucket=bucket,
                target_bucket=target_bucket,
                target_prefix=target_prefix,
                expected_bucket_owner=expected_bucket_owner,
                target_grant=target_grant,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)

        target_bucket: str | core.StringOut = core.arg()

        target_grant: list[TargetGrant] | core.ArrayOut[TargetGrant] | None = core.arg(default=None)

        target_prefix: str | core.StringOut = core.arg()
