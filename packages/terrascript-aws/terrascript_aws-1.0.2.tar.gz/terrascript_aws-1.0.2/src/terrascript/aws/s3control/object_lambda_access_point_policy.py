import terrascript.core as core


@core.resource(type="aws_s3control_object_lambda_access_point_policy", namespace="aws_s3control")
class ObjectLambdaAccessPointPolicy(core.Resource):

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    has_public_access_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        policy: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObjectLambdaAccessPointPolicy.Args(
                name=name,
                policy=policy,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
