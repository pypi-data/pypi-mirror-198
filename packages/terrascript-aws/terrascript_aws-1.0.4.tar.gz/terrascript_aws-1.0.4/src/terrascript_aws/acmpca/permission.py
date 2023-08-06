import terrascript.core as core


@core.resource(type="aws_acmpca_permission", namespace="acmpca")
class Permission(core.Resource):
    """
    (Required) The actions that the specified AWS service principal can use. These include `IssueCertifi
    cate`, `GetCertificate`, and `ListPermissions`. Note that in order for ACM to automatically rotate c
    ertificates issued by a PCA, it must be granted permission on all 3 actions, as per the example abov
    e.
    """

    actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    """
    (Required) The Amazon Resource Name (ARN) of the CA that grants the permissions.
    """
    certificate_authority_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The IAM policy that is associated with the permission.
    """
    policy: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The AWS service or identity that receives the permission. At this time, the only valid pr
    incipal is `acm.amazonaws.com`.
    """
    principal: str | core.StringOut = core.attr(str)

    """
    (Optional) The ID of the calling account
    """
    source_account: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut],
        certificate_authority_arn: str | core.StringOut,
        principal: str | core.StringOut,
        source_account: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                actions=actions,
                certificate_authority_arn=certificate_authority_arn,
                principal=principal,
                source_account=source_account,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        certificate_authority_arn: str | core.StringOut = core.arg()

        principal: str | core.StringOut = core.arg()

        source_account: str | core.StringOut | None = core.arg(default=None)
