import terrascript.core as core


@core.resource(type="aws_dynamodb_table_replica", namespace="dynamodb")
class TableReplica(core.Resource):
    """
    ARN of the table replica.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) ARN of the _main_ or global table which this resource will replicate.
    """
    global_table_arn: str | core.StringOut = core.attr(str)

    """
    Name of the table and region of the main global table joined with a semicolon (_e.g._, `TableName:us
    east-1`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) ARN of the CMK that should be used for the AWS KMS encryption.
    """
    kms_key_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Whether to enable Point In Time Recovery for the replica. Default is `false`.
    """
    point_in_time_recovery: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional, Forces new resource) Storage class of the table replica. Valid values are `STANDARD` and
    STANDARD_INFREQUENT_ACCESS`. If not used, the table replica will use the same class as the global t
    able.
    """
    table_class_override: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Map of tags to populate on the created table. If configured with a provider [`default_tag
    s` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_ta
    gs-configuration-block) present, tags with matching keys will overwrite those defined at the provide
    r-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        global_table_arn: str | core.StringOut,
        kms_key_arn: str | core.StringOut | None = None,
        point_in_time_recovery: bool | core.BoolOut | None = None,
        table_class_override: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TableReplica.Args(
                global_table_arn=global_table_arn,
                kms_key_arn=kms_key_arn,
                point_in_time_recovery=point_in_time_recovery,
                table_class_override=table_class_override,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_table_arn: str | core.StringOut = core.arg()

        kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        point_in_time_recovery: bool | core.BoolOut | None = core.arg(default=None)

        table_class_override: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
