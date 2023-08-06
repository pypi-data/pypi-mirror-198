import terrascript.core as core


@core.data(type="aws_redshift_cluster_credentials", namespace="aws_redshift")
class DsClusterCredentials(core.Data):

    auto_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    cluster_identifier: str | core.StringOut = core.attr(str)

    db_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    db_name: str | core.StringOut | None = core.attr(str, default=None)

    db_password: str | core.StringOut = core.attr(str, computed=True)

    db_user: str | core.StringOut = core.attr(str)

    duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    expiration: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        db_user: str | core.StringOut,
        auto_create: bool | core.BoolOut | None = None,
        db_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
        db_name: str | core.StringOut | None = None,
        duration_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsClusterCredentials.Args(
                cluster_identifier=cluster_identifier,
                db_user=db_user,
                auto_create=auto_create,
                db_groups=db_groups,
                db_name=db_name,
                duration_seconds=duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_create: bool | core.BoolOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        db_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        db_name: str | core.StringOut | None = core.arg(default=None)

        db_user: str | core.StringOut = core.arg()

        duration_seconds: int | core.IntOut | None = core.arg(default=None)
