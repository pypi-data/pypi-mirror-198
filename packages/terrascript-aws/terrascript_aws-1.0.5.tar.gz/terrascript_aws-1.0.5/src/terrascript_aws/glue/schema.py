import terrascript.core as core


@core.resource(type="aws_glue_schema", namespace="glue")
class Schema(core.Resource):
    """
    Amazon Resource Name (ARN) of the schema.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The compatibility mode of the schema. Values values are: `NONE`, `DISABLED`, `BACKWARD`,
    BACKWARD_ALL`, `FORWARD`, `FORWARD_ALL`, `FULL`, and `FULL_ALL`.
    """
    compatibility: str | core.StringOut = core.attr(str)

    """
    (Required) The data format of the schema definition. Valid values are `AVRO`, `JSON` and `PROTOBUF`.
    """
    data_format: str | core.StringOut = core.attr(str)

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Amazon Resource Name (ARN) of the schema.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The latest version of the schema associated with the returned schema definition.
    """
    latest_schema_version: int | core.IntOut = core.attr(int, computed=True)

    """
    The next version of the schema associated with the returned schema definition.
    """
    next_schema_version: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The ARN of the Glue Registry to create the schema in.
    """
    registry_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The name of the Glue Registry.
    """
    registry_name: str | core.StringOut = core.attr(str, computed=True)

    """
    The version number of the checkpoint (the last time the compatibility mode was changed).
    """
    schema_checkpoint: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) The schema definition using the `data_format` setting for `schema_name`.
    """
    schema_definition: str | core.StringOut = core.attr(str)

    schema_name: str | core.StringOut = core.attr(str)

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

    def __init__(
        self,
        resource_name: str,
        *,
        compatibility: str | core.StringOut,
        data_format: str | core.StringOut,
        schema_definition: str | core.StringOut,
        schema_name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        registry_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Schema.Args(
                compatibility=compatibility,
                data_format=data_format,
                schema_definition=schema_definition,
                schema_name=schema_name,
                description=description,
                registry_arn=registry_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compatibility: str | core.StringOut = core.arg()

        data_format: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        registry_arn: str | core.StringOut | None = core.arg(default=None)

        schema_definition: str | core.StringOut = core.arg()

        schema_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
