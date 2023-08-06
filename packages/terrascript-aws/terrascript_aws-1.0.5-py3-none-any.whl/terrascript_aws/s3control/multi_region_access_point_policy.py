import terrascript.core as core


@core.schema
class Details(core.Schema):

    name: str | core.StringOut = core.attr(str)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        policy: str | core.StringOut,
    ):
        super().__init__(
            args=Details.Args(
                name=name,
                policy=policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()


@core.resource(type="aws_s3control_multi_region_access_point_policy", namespace="s3control")
class MultiRegionAccessPointPolicy(core.Resource):
    """
    (Optional) The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatica
    lly determined account ID of the Terraform AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) A configuration block containing details about the policy for the Multi-Region Access Poi
    nt. See [Details Configuration Block](#details-configuration) below for more details
    """
    details: Details = core.attr(Details)

    """
    The last established policy for the Multi-Region Access Point.
    """
    established: str | core.StringOut = core.attr(str, computed=True)

    """
    The AWS account ID and access point name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The proposed policy for the Multi-Region Access Point.
    """
    proposed: str | core.StringOut = core.attr(str, computed=True)

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
            args=MultiRegionAccessPointPolicy.Args(
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
