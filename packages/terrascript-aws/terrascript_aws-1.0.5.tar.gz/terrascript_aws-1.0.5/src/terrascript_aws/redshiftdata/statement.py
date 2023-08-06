import terrascript.core as core


@core.schema
class Parameters(core.Schema):

    name: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Parameters.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_redshiftdata_statement", namespace="redshiftdata")
class Statement(core.Resource):
    """
    (Required) The cluster identifier.
    """

    cluster_identifier: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the database.
    """
    database: str | core.StringOut = core.attr(str)

    """
    (Optional) The database user name.
    """
    db_user: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Redshift Data Statement ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.attr(
        Parameters, default=None, kind=core.Kind.array
    )

    """
    (Optional) The name or ARN of the secret that enables access to the database.
    """
    secret_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The SQL statement text to run.
    """
    sql: str | core.StringOut = core.attr(str)

    """
    (Optional) The name of the SQL statement. You can name the SQL statement when you create it to ident
    ify the query.
    """
    statement_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) A value that indicates whether to send an event to the Amazon EventBridge event bus after
    the SQL statement runs.
    """
    with_event: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: str | core.StringOut,
        database: str | core.StringOut,
        sql: str | core.StringOut,
        db_user: str | core.StringOut | None = None,
        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = None,
        secret_arn: str | core.StringOut | None = None,
        statement_name: str | core.StringOut | None = None,
        with_event: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Statement.Args(
                cluster_identifier=cluster_identifier,
                database=database,
                sql=sql,
                db_user=db_user,
                parameters=parameters,
                secret_arn=secret_arn,
                statement_name=statement_name,
                with_event=with_event,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_identifier: str | core.StringOut = core.arg()

        database: str | core.StringOut = core.arg()

        db_user: str | core.StringOut | None = core.arg(default=None)

        parameters: list[Parameters] | core.ArrayOut[Parameters] | None = core.arg(default=None)

        secret_arn: str | core.StringOut | None = core.arg(default=None)

        sql: str | core.StringOut = core.arg()

        statement_name: str | core.StringOut | None = core.arg(default=None)

        with_event: bool | core.BoolOut | None = core.arg(default=None)
