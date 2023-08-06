import terrascript.core as core


@core.data(type="aws_iam_instance_profiles", namespace="iam")
class DsInstanceProfiles(core.Data):
    """
    Set of Amazon Resource Name (ARN) specifying the instance profile.
    """

    arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Set of IAM instance profile names.
    """
    names: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Set of IAM instance profile paths.
    """
    paths: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Required) The IAM role name.
    """
    role_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        role_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceProfiles.Args(
                role_name=role_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_name: str | core.StringOut = core.arg()
