import terrascript.core as core


@core.resource(type="aws_timestreamwrite_database", namespace="timestreamwrite")
class Database(core.Resource):
    """
    The ARN that uniquely identifies this database.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    database_name: str | core.StringOut = core.attr(str)

    """
    The name of the Timestream database.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The ARN (not Alias ARN) of the KMS key to be used to encrypt the data stored in the datab
    ase. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS k
    ey located in your account. Refer to [AWS managed KMS keys](https://docs.aws.amazon.com/kms/latest/d
    eveloperguide/concepts.html#aws-managed-cmk) for more info.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The total number of tables found within the Timestream database.
    """
    table_count: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) Map of tags to assign to this resource. If configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
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
        database_name: str | core.StringOut,
        kms_key_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Database.Args(
                database_name=database_name,
                kms_key_id=kms_key_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database_name: str | core.StringOut = core.arg()

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
