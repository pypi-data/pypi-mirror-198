import terrascript.core as core


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


@core.resource(type="aws_fsx_data_repository_association", namespace="fsx")
class DataRepositoryAssociation(core.Resource):
    """
    Amazon Resource Name of the file system.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    association_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set to true to run an import data repository task to import metadata from the data reposi
    tory to the file system after the data repository association is created. Defaults to `false`.
    """
    batch_import_meta_data_on_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The path to the Amazon S3 data repository that will be linked to the file system. The pat
    h must be an S3 bucket s3://myBucket/myPrefix/. This path specifies where in the S3 data repository
    files will be imported from or exported to. The same S3 bucket cannot be linked more than once to th
    e same file system.
    """
    data_repository_path: str | core.StringOut = core.attr(str)

    """
    (Optional) Set to true to delete files from the file system upon deleting this data repository assoc
    iation. Defaults to `false`.
    """
    delete_data_in_filesystem: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The ID of the Amazon FSx file system to on which to create a data repository association.
    """
    file_system_id: str | core.StringOut = core.attr(str)

    """
    (Required) A path on the file system that points to a high-level directory (such as `/ns1/`) or subd
    irectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `data_repository_path`. The leading f
    orward slash in the name is required. Two data repository associations cannot have overlapping file
    system paths. For example, if a data repository is associated with file system path `/ns1/`, then yo
    u cannot link another data repository with file system path `/ns1/ns2`. This path specifies where in
    your file system files will be exported from or imported to. This file system directory can be link
    ed to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.
    """
    file_system_path: str | core.StringOut = core.attr(str)

    """
    Identifier of the data repository association, e.g., `dra-12345678`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) For files imported from a data repository, this value determines the stripe count and max
    imum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks
    that a single file can be striped across is limited by the total number of disks that make up the fi
    le system.
    """
    imported_file_chunk_size: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) See the [`s3` configuration](#s3-arguments) block. Max of 1.
    """
    s3: S3 | None = core.attr(S3, default=None, computed=True)

    """
    (Optional) A map of tags to assign to the data repository association. If configured with a provider
    [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/d
    ocs#default_tags-configuration-block) present, tags with matching keys will overwrite those defined
    at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
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
