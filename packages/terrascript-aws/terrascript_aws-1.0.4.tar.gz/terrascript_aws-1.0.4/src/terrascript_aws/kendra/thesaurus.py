import terrascript.core as core


@core.schema
class SourceS3Path(core.Schema):

    bucket: str | core.StringOut = core.attr(str)

    key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut,
        key: str | core.StringOut,
    ):
        super().__init__(
            args=SourceS3Path.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut = core.arg()

        key: str | core.StringOut = core.arg()


@core.resource(type="aws_kendra_thesaurus", namespace="kendra")
class Thesaurus(core.Resource):
    """
    ARN of the thesaurus.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description for a thesaurus.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The unique identifiers of the thesaurus and index separated by a slash (`/`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    index_id: str | core.StringOut = core.attr(str)

    """
    (Required) The name for the thesaurus.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The IAM (Identity and Access Management) role used to access the thesaurus file in S3.
    """
    role_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The S3 path where your thesaurus file sits in S3. Detailed below.
    """
    source_s3_path: SourceS3Path = core.attr(SourceS3Path)

    """
    The current status of the thesaurus.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    thesaurus_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        index_id: str | core.StringOut,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        source_s3_path: SourceS3Path,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Thesaurus.Args(
                index_id=index_id,
                name=name,
                role_arn=role_arn,
                source_s3_path=source_s3_path,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        index_id: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        source_s3_path: SourceS3Path = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
