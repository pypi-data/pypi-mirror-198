import terrascript.core as core


@core.data(type="aws_iam_instance_profile", namespace="aws_iam")
class DsInstanceProfile(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    create_date: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    path: str | core.StringOut = core.attr(str, computed=True)

    role_arn: str | core.StringOut = core.attr(str, computed=True)

    role_id: str | core.StringOut = core.attr(str, computed=True)

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
