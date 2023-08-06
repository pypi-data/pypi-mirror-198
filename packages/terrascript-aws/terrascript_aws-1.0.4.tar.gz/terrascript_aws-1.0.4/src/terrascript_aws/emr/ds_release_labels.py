import terrascript.core as core


@core.schema
class Filters(core.Schema):

    application: str | core.StringOut | None = core.attr(str, default=None)

    prefix: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application: str | core.StringOut | None = None,
        prefix: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Filters.Args(
                application=application,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application: str | core.StringOut | None = core.arg(default=None)

        prefix: str | core.StringOut | None = core.arg(default=None)


@core.data(type="aws_emr_release_labels", namespace="emr")
class DsReleaseLabels(core.Data):

    filters: Filters | None = core.attr(Filters, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    release_labels: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filters: Filters | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsReleaseLabels.Args(
                filters=filters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filters: Filters | None = core.arg(default=None)
