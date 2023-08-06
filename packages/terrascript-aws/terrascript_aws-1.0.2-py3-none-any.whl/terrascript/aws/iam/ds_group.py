import terrascript.core as core


@core.schema
class Users(core.Schema):

    arn: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    user_id: str | core.StringOut = core.attr(str, computed=True)

    user_name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: str | core.StringOut,
        path: str | core.StringOut,
        user_id: str | core.StringOut,
        user_name: str | core.StringOut,
    ):
        super().__init__(
            args=Users.Args(
                arn=arn,
                path=path,
                user_id=user_id,
                user_name=user_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut = core.arg()

        path: str | core.StringOut = core.arg()

        user_id: str | core.StringOut = core.arg()

        user_name: str | core.StringOut = core.arg()


@core.data(type="aws_iam_group", namespace="aws_iam")
class DsGroup(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    group_id: str | core.StringOut = core.attr(str, computed=True)

    group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    path: str | core.StringOut = core.attr(str, computed=True)

    users: list[Users] | core.ArrayOut[Users] = core.attr(
        Users, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        group_name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                group_name=group_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_name: str | core.StringOut = core.arg()
