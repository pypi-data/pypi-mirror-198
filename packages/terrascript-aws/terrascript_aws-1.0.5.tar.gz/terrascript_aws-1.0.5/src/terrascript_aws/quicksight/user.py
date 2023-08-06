import terrascript.core as core


@core.resource(type="aws_quicksight_user", namespace="quicksight")
class User(core.Resource):
    """
    Amazon Resource Name (ARN) of the user
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ID for the AWS account that the user is in. Currently, you use the ID for the AWS acc
    ount that contains your Amazon QuickSight account.
    """
    aws_account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The email address of the user that you want to register.
    """
    email: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of the IAM user or role that you are registering with Amazon QuickSight.
    """
    iam_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Amazon QuickSight supports several ways of managing the identity of users. This parameter
    accepts either  `IAM` or `QUICKSIGHT`. If `IAM` is specified, the `iam_arn` must also be specified.
    """
    identity_type: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The name of the IAM session to use when assuming roles that can embed QuickSight dashboar
    ds. Only valid for registering users using an assumed IAM role. Additionally, if registering multipl
    e users using the same IAM role, each user needs to have a unique session name.
    """
    session_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Amazon QuickSight user name that you want to create for the user you are registering.
    Only valid for registering a user with `identity_type` set to `QUICKSIGHT`.
    """
    user_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The Amazon QuickSight role of the user. The user role can be one of the following: `READE
    R`, `AUTHOR`, or `ADMIN`
    """
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
