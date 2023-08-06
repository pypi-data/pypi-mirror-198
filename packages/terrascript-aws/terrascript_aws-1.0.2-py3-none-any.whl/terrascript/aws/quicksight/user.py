import terrascript.core as core


@core.resource(type="aws_quicksight_user", namespace="aws_quicksight")
class User(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    email: str | core.StringOut = core.attr(str)

    iam_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    identity_type: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    session_name: str | core.StringOut | None = core.attr(str, default=None)

    user_name: str | core.StringOut | None = core.attr(str, default=None)

    user_role: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        email: str | core.StringOut,
        identity_type: str | core.StringOut,
        user_role: str | core.StringOut,
        aws_account_id: str | core.StringOut | None = None,
        iam_arn: str | core.StringOut | None = None,
        namespace: str | core.StringOut | None = None,
        session_name: str | core.StringOut | None = None,
        user_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                email=email,
                identity_type=identity_type,
                user_role=user_role,
                aws_account_id=aws_account_id,
                iam_arn=iam_arn,
                namespace=namespace,
                session_name=session_name,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: str | core.StringOut | None = core.arg(default=None)

        email: str | core.StringOut = core.arg()

        iam_arn: str | core.StringOut | None = core.arg(default=None)

        identity_type: str | core.StringOut = core.arg()

        namespace: str | core.StringOut | None = core.arg(default=None)

        session_name: str | core.StringOut | None = core.arg(default=None)

        user_name: str | core.StringOut | None = core.arg(default=None)

        user_role: str | core.StringOut = core.arg()
