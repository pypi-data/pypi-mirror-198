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


@core.resource(type="aws_s3control_multi_region_access_point_policy", namespace="aws_s3control")
class MultiRegionAccessPointPolicy(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    details: Details = core.attr(Details)

    established: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

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
