import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    default_value: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    name: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_value: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Parameter.Args(
                default_value=default_value,
                description=description,
                name=name,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AttachmentsSource(core.Schema):

    key: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None)

    values: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut],
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AttachmentsSource.Args(
                key=key,
                values=values,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.resource(type="aws_ssm_document", namespace="aws_ssm")
class Document(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    attachments_source: list[AttachmentsSource] | core.ArrayOut[
        AttachmentsSource
    ] | None = core.attr(AttachmentsSource, default=None, kind=core.Kind.array)

    content: str | core.StringOut = core.attr(str)

    created_date: str | core.StringOut = core.attr(str, computed=True)

    default_version: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    document_format: str | core.StringOut | None = core.attr(str, default=None)

    document_type: str | core.StringOut = core.attr(str)

    document_version: str | core.StringOut = core.attr(str, computed=True)

    hash: str | core.StringOut = core.attr(str, computed=True)

    hash_type: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    latest_version: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    owner: str | core.StringOut = core.attr(str, computed=True)

    parameter: list[Parameter] | core.ArrayOut[Parameter] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    permissions: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    platform_types: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    schema_version: str | core.StringOut = core.attr(str, computed=True)

    status: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: str | core.StringOut | None = core.attr(str, default=None)

    version_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content: str | core.StringOut,
        document_type: str | core.StringOut,
        name: str | core.StringOut,
        attachments_source: list[AttachmentsSource]
        | core.ArrayOut[AttachmentsSource]
        | None = None,
        document_format: str | core.StringOut | None = None,
        permissions: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        target_type: str | core.StringOut | None = None,
        version_name: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Document.Args(
                content=content,
                document_type=document_type,
                name=name,
                attachments_source=attachments_source,
                document_format=document_format,
                permissions=permissions,
                tags=tags,
                tags_all=tags_all,
                target_type=target_type,
                version_name=version_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachments_source: list[AttachmentsSource] | core.ArrayOut[
            AttachmentsSource
        ] | None = core.arg(default=None)

        content: str | core.StringOut = core.arg()

        document_format: str | core.StringOut | None = core.arg(default=None)

        document_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        permissions: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        target_type: str | core.StringOut | None = core.arg(default=None)

        version_name: str | core.StringOut | None = core.arg(default=None)
