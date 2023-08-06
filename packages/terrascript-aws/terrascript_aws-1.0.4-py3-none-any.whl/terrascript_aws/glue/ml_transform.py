import terrascript.core as core


@core.schema
class InputRecordTables(core.Schema):

    catalog_id: str | core.StringOut | None = core.attr(str, default=None)

    connection_name: str | core.StringOut | None = core.attr(str, default=None)

    database_name: str | core.StringOut = core.attr(str)

    table_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        database_name: str | core.StringOut,
        table_name: str | core.StringOut,
        catalog_id: str | core.StringOut | None = None,
        connection_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputRecordTables.Args(
                database_name=database_name,
                table_name=table_name,
                catalog_id=catalog_id,
                connection_name=connection_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: str | core.StringOut | None = core.arg(default=None)

        connection_name: str | core.StringOut | None = core.arg(default=None)

        database_name: str | core.StringOut = core.arg()

        table_name: str | core.StringOut = core.arg()


@core.schema
class FindMatchesParameters(core.Schema):

    accuracy_cost_trade_off: float | core.FloatOut | None = core.attr(float, default=None)

    enforce_provided_labels: bool | core.BoolOut | None = core.attr(bool, default=None)

    precision_recall_trade_off: float | core.FloatOut | None = core.attr(float, default=None)

    primary_key_column_name: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        accuracy_cost_trade_off: float | core.FloatOut | None = None,
        enforce_provided_labels: bool | core.BoolOut | None = None,
        precision_recall_trade_off: float | core.FloatOut | None = None,
        primary_key_column_name: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=FindMatchesParameters.Args(
                accuracy_cost_trade_off=accuracy_cost_trade_off,
                enforce_provided_labels=enforce_provided_labels,
                precision_recall_trade_off=precision_recall_trade_off,
                primary_key_column_name=primary_key_column_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accuracy_cost_trade_off: float | core.FloatOut | None = core.arg(default=None)

        enforce_provided_labels: bool | core.BoolOut | None = core.arg(default=None)

        precision_recall_trade_off: float | core.FloatOut | None = core.arg(default=None)

        primary_key_column_name: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Parameters(core.Schema):

    find_matches_parameters: FindMatchesParameters = core.attr(FindMatchesParameters)

    transform_type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        find_matches_parameters: FindMatchesParameters,
        transform_type: str | core.StringOut,
    ):
        super().__init__(
            args=Parameters.Args(
                find_matches_parameters=find_matches_parameters,
                transform_type=transform_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        find_matches_parameters: FindMatchesParameters = core.arg()

        transform_type: str | core.StringOut = core.arg()


@core.schema
class Schema(core.Schema):

    data_type: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        data_type: str | core.StringOut,
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Schema.Args(
                data_type=data_type,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()


@core.resource(type="aws_glue_ml_transform", namespace="glue")
class MlTransform(core.Resource):
    """
    Amazon Resource Name (ARN) of Glue ML Transform.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The version of glue to use, for example "1.0". For information about available versions,
    see the [AWS Glue Release Notes](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
    """
    glue_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Glue ML Transform ID.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required)  A list of AWS Glue table definitions used by the transform. see [Input Record Tables](#i
    nput_record_tables).
    """
    input_record_tables: list[InputRecordTables] | core.ArrayOut[InputRecordTables] = core.attr(
        InputRecordTables, kind=core.Kind.array
    )

    """
    The number of labels available for this transform.
    """
    label_count: int | core.IntOut = core.attr(int, computed=True)

    max_capacity: float | core.FloatOut | None = core.attr(float, default=None, computed=True)

    max_retries: int | core.IntOut | None = core.attr(int, default=None)

    """
    The name of the column.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The number of workers of a defined `worker_type` that are allocated when an ML Transform
    runs. Required with `worker_type`.
    """
    number_of_workers: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Required) The algorithmic parameters that are specific to the transform type used. Conditionally de
    pendent on the transform type. see [Parameters](#parameters).
    """
    parameters: Parameters = core.attr(Parameters)

    role_arn: str | core.StringOut = core.attr(str)

    """
    The object that represents the schema that this transform accepts. see [Schema](#schema).
    """
    schema: list[Schema] | core.ArrayOut[Schema] = core.attr(
        Schema, computed=True, kind=core.Kind.array
    )

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

    timeout: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The type of predefined worker that is allocated when an ML Transform runs. Accepts a valu
    e of `Standard`, `G.1X`, or `G.2X`. Required with `number_of_workers`.
    """
    worker_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        input_record_tables: list[InputRecordTables] | core.ArrayOut[InputRecordTables],
        name: str | core.StringOut,
        parameters: Parameters,
        role_arn: str | core.StringOut,
        description: str | core.StringOut | None = None,
        glue_version: str | core.StringOut | None = None,
        max_capacity: float | core.FloatOut | None = None,
        max_retries: int | core.IntOut | None = None,
        number_of_workers: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        timeout: int | core.IntOut | None = None,
        worker_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MlTransform.Args(
                input_record_tables=input_record_tables,
                name=name,
                parameters=parameters,
                role_arn=role_arn,
                description=description,
                glue_version=glue_version,
                max_capacity=max_capacity,
                max_retries=max_retries,
                number_of_workers=number_of_workers,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        glue_version: str | core.StringOut | None = core.arg(default=None)

        input_record_tables: list[InputRecordTables] | core.ArrayOut[InputRecordTables] = core.arg()

        max_capacity: float | core.FloatOut | None = core.arg(default=None)

        max_retries: int | core.IntOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        number_of_workers: int | core.IntOut | None = core.arg(default=None)

        parameters: Parameters = core.arg()

        role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        timeout: int | core.IntOut | None = core.arg(default=None)

        worker_type: str | core.StringOut | None = core.arg(default=None)
