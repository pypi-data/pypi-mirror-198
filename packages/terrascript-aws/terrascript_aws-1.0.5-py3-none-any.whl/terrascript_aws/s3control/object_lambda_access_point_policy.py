import terrascript.core as core


@core.resource(type="aws_s3control_object_lambda_access_point_policy", namespace="s3control")
class ObjectLambdaAccessPointPolicy(core.Resource):
    """
    (Optional) The AWS account ID for the account that owns the Object Lambda Access Point. Defaults to
    automatically determined account ID of the Terraform AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Indicates whether this access point currently has a policy that allows public access.
    """
    has_public_access_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The AWS account ID and access point name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Object Lambda Access Point.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The Object Lambda Access Point resource policy document.
    """
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
