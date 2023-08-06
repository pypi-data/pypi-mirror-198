import terrascript.core as core


@core.schema
class InputDataConfig(core.Schema):

    data_access_role_arn: str | core.StringOut = core.attr(str)

    s3_uri: str | core.StringOut = core.attr(str)

    tuning_data_s3_uri: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        data_access_role_arn: str | core.StringOut,
        s3_uri: str | core.StringOut,
        tuning_data_s3_uri: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputDataConfig.Args(
                data_access_role_arn=data_access_role_arn,
                s3_uri=s3_uri,
                tuning_data_s3_uri=tuning_data_s3_uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_access_role_arn: str | core.StringOut = core.arg()

        s3_uri: str | core.StringOut = core.arg()

        tuning_data_s3_uri: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_transcribe_language_model", namespace="transcribe")
class LanguageModel(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    base_model_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    input_data_config: InputDataConfig = core.attr(InputDataConfig)

    language_code: str | core.StringOut = core.attr(str)

    model_name: str | core.StringOut = core.attr(str)

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
        base_model_name: str | core.StringOut,
        input_data_config: InputDataConfig,
        language_code: str | core.StringOut,
        model_name: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LanguageModel.Args(
                base_model_name=base_model_name,
                input_data_config=input_data_config,
                language_code=language_code,
                model_name=model_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        base_model_name: str | core.StringOut = core.arg()

        input_data_config: InputDataConfig = core.arg()

        language_code: str | core.StringOut = core.arg()

        model_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
