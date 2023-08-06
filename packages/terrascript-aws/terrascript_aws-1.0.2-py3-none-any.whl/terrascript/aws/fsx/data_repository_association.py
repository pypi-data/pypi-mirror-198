import terrascript.core as core


@core.schema
class AutoExportPolicy(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AutoExportPolicy.Args(
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AutoImportPolicy(core.Schema):

    events: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        events: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AutoImportPolicy.Args(
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class S3(core.Schema):

    auto_export_policy: AutoExportPolicy | None = core.attr(
        AutoExportPolicy, default=None, computed=True
    )

    auto_import_policy: AutoImportPolicy | None = core.attr(
        AutoImportPolicy, default=None, computed=True
    )

    def __init__(
        self,
        *,
        auto_export_policy: AutoExportPolicy | None = None,
        auto_import_policy: AutoImportPolicy | None = None,
    ):
        super().__init__(
            args=S3.Args(
                auto_export_policy=auto_export_policy,
                auto_import_policy=auto_import_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_export_policy: AutoExportPolicy | None = core.arg(default=None)

        auto_import_policy: AutoImportPolicy | None = core.arg(default=None)


@core.resource(type="aws_fsx_data_repository_association", namespace="aws_fsx")
class DataRepositoryAssociation(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    association_id: str | core.StringOut = core.attr(str, computed=True)

    batch_import_meta_data_on_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    data_repository_path: str | core.StringOut = core.attr(str)

    delete_data_in_filesystem: bool | core.BoolOut | None = core.attr(bool, default=None)

    file_system_id: str | core.StringOut = core.attr(str)

    file_system_path: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    imported_file_chunk_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    s3: S3 | None = core.attr(S3, default=None, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        data_repository_path: str | core.StringOut,
        file_system_id: str | core.StringOut,
        file_system_path: str | core.StringOut,
        batch_import_meta_data_on_create: bool | core.BoolOut | None = None,
        delete_data_in_filesystem: bool | core.BoolOut | None = None,
        imported_file_chunk_size: int | core.IntOut | None = None,
        s3: S3 | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataRepositoryAssociation.Args(
                data_repository_path=data_repository_path,
                file_system_id=file_system_id,
                file_system_path=file_system_path,
                batch_import_meta_data_on_create=batch_import_meta_data_on_create,
                delete_data_in_filesystem=delete_data_in_filesystem,
                imported_file_chunk_size=imported_file_chunk_size,
                s3=s3,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        batch_import_meta_data_on_create: bool | core.BoolOut | None = core.arg(default=None)

        data_repository_path: str | core.StringOut = core.arg()

        delete_data_in_filesystem: bool | core.BoolOut | None = core.arg(default=None)

        file_system_id: str | core.StringOut = core.arg()

        file_system_path: str | core.StringOut = core.arg()

        imported_file_chunk_size: int | core.IntOut | None = core.arg(default=None)

        s3: S3 | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
