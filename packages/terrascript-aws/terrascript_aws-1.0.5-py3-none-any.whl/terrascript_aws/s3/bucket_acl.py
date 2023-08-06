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
class Grant(core.Schema):

    grantee: Grantee | None = core.attr(Grantee, default=None)

    permission: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        permission: str | core.StringOut,
        grantee: Grantee | None = None,
    ):
        super().__init__(
            args=Grant.Args(
                permission=permission,
                grantee=grantee,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grantee: Grantee | None = core.arg(default=None)

        permission: str | core.StringOut = core.arg()


@core.schema
class Owner(core.Schema):

    display_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        display_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Owner.Args(
                id=id,
                display_name=display_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: str | core.StringOut | None = core.arg(default=None)

        id: str | core.StringOut = core.arg()


@core.schema
class AccessControlPolicy(core.Schema):

    grant: list[Grant] | core.ArrayOut[Grant] | None = core.attr(
        Grant, default=None, kind=core.Kind.array
    )

    owner: Owner = core.attr(Owner)

    def __init__(
        self,
        *,
        owner: Owner,
        grant: list[Grant] | core.ArrayOut[Grant] | None = None,
    ):
        super().__init__(
            args=AccessControlPolicy.Args(
                owner=owner,
                grant=grant,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grant: list[Grant] | core.ArrayOut[Grant] | None = core.arg(default=None)

        owner: Owner = core.arg()


@core.resource(type="aws_s3_bucket_acl", namespace="s3")
class BucketAcl(core.Resource):
    """
    (Optional, Conflicts with `acl`) A configuration block that sets the ACL permissions for an object p
    er grantee [documented below](#access_control_policy).
    """

    access_control_policy: AccessControlPolicy | None = core.attr(
        AccessControlPolicy, default=None, computed=True
    )

    """
    (Optional, Conflicts with `access_control_policy`) The canned ACL to apply to the bucket.
    """
    acl: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required, Forces new resource) The name of the bucket.
    """
    bucket: str | core.StringOut = core.attr(str)

    """
    (Optional, Forces new resource) The account ID of the expected bucket owner.
    """
    expected_bucket_owner: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The ID of the owner.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: str | core.StringOut,
        access_control_policy: AccessControlPolicy | None = None,
        acl: str | core.StringOut | None = None,
        expected_bucket_owner: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAcl.Args(
                bucket=bucket,
                access_control_policy=access_control_policy,
                acl=acl,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_control_policy: AccessControlPolicy | None = core.arg(default=None)

        acl: str | core.StringOut | None = core.arg(default=None)

        bucket: str | core.StringOut = core.arg()

        expected_bucket_owner: str | core.StringOut | None = core.arg(default=None)
