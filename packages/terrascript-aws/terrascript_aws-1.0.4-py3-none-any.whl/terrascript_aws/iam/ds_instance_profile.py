import terrascript.core as core


@core.data(type="aws_iam_instance_profile", namespace="iam")
class DsInstanceProfile(core.Data):
    """
    The Amazon Resource Name (ARN) specifying the instance profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The string representation of the date the instance profile
    """
    create_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly IAM instance profile name to match.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The path to the instance profile.
    """
    path: str | core.StringOut = core.attr(str, computed=True)

    """
    The role arn associated with this instance profile.
    """
    role_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The role id associated with this instance profile.
    """
    role_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The role name associated with this instance profile.
    """
    role_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceProfile.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
