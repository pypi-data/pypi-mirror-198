import terrascript.core as core


@core.schema
class Filter(core.Schema):

    exclude_matched_pattern: bool | core.BoolOut | None = core.attr(bool, default=None)

    pattern: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        pattern: str | core.StringOut,
        type: str | core.StringOut,
        exclude_matched_pattern: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Filter.Args(
                pattern=pattern,
                type=type,
                exclude_matched_pattern=exclude_matched_pattern,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_matched_pattern: bool | core.BoolOut | None = core.arg(default=None)

        pattern: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class FilterGroup(core.Schema):

    filter: list[Filter] | core.ArrayOut[Filter] | None = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        filter: list[Filter] | core.ArrayOut[Filter] | None = None,
    ):
        super().__init__(
            args=FilterGroup.Args(
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: list[Filter] | core.ArrayOut[Filter] | None = core.arg(default=None)


@core.resource(type="aws_codebuild_webhook", namespace="aws_codebuild")
class Webhook(core.Resource):

    branch_filter: str | core.StringOut | None = core.attr(str, default=None)

    build_type: str | core.StringOut | None = core.attr(str, default=None)

    filter_group: list[FilterGroup] | core.ArrayOut[FilterGroup] | None = core.attr(
        FilterGroup, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    payload_url: str | core.StringOut = core.attr(str, computed=True)

    project_name: str | core.StringOut = core.attr(str)

    secret: str | core.StringOut = core.attr(str, computed=True)

    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        project_name: str | core.StringOut,
        branch_filter: str | core.StringOut | None = None,
        build_type: str | core.StringOut | None = None,
        filter_group: list[FilterGroup] | core.ArrayOut[FilterGroup] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Webhook.Args(
                project_name=project_name,
                branch_filter=branch_filter,
                build_type=build_type,
                filter_group=filter_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        branch_filter: str | core.StringOut | None = core.arg(default=None)

        build_type: str | core.StringOut | None = core.arg(default=None)

        filter_group: list[FilterGroup] | core.ArrayOut[FilterGroup] | None = core.arg(default=None)

        project_name: str | core.StringOut = core.arg()
