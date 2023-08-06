import terrascript.core as core


@core.data(type="aws_db_event_categories", namespace="rds")
class DsDbEventCategories(core.Data):
    """
    A list of the event categories.
    """

    event_categories: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    Region of the event categories.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The type of source that will be generating the events. Valid options are db-instance, db-
    security-group, db-parameter-group, db-snapshot, db-cluster or db-cluster-snapshot.
    """
    source_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        source_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbEventCategories.Args(
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_type: str | core.StringOut | None = core.arg(default=None)
