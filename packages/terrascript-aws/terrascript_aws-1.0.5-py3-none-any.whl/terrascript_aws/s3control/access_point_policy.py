import terrascript.core as core


@core.resource(type="aws_s3control_access_point_policy", namespace="s3control")
class AccessPointPolicy(core.Resource):
    """
    (Required) The ARN of the access point that you want to associate with the specified policy.
    """

    access_point_arn: str | core.StringOut = core.attr(str)

    """
    Indicates whether this access point currently has a policy that allows public access.
    """
    has_public_access_policy: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    The AWS account ID and access point name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The policy that you want to apply to the specified access point.
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        access_point_arn: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPointPolicy.Args(
                access_point_arn=access_point_arn,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_point_arn: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
