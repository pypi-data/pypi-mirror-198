import terrascript.core as core


@core.data(type="aws_redshift_cluster_credentials", namespace="redshift")
class DsClusterCredentials(core.Data):
    """
    (Optional)  Create a database user with the name specified for the user named in `db_user` if one do
    es not exist.
    """

    auto_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The unique identifier of the cluster that contains the database for which your are reques
    ting credentials.
    """
    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Optional) A list of the names of existing database groups that the user named in `db_user` will joi
    n for the current session, in addition to any group memberships for an existing user. If not specifi
    ed, a new user is added only to `PUBLIC`.
    """
    db_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The name of a database that DbUser is authorized to log on to. If `db_name` is not specif
    ied, `db_user` can log on to any existing database.
    """
    db_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    A temporary password that authorizes the user name returned by `db_user` to log on to the database `
    db_name`.
    """
    db_password: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of a database user. If a user name matching `db_user` exists in the database, th
    e temporary user credentials have the same permissions as the  existing user. If `db_user` doesn't e
    xist in the database and `auto_create` is `True`, a new user is created using the value for `db_user
    with `PUBLIC` permissions.  If a database user matching the value for `db_user` doesn't exist and
    not` is `False`, then the command succeeds but the connection attempt will fail because the user do
    esn't exist in the database.
    """
    db_user: str | core.StringOut = core.attr(str)

    """
    (Optional)  The number of seconds until the returned temporary password expires. Valid values are be
    tween `900` and `3600`. Default value is `900`.
    """
    duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    """
    The date and time the password in `db_password` expires.
    """
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
