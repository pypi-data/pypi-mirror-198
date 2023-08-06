import terrascript.core as core


@core.schema
class SslConfiguration(core.Schema):

    certificate: str | core.StringOut = core.attr(str)

    chain: str | core.StringOut | None = core.attr(str, default=None)

    private_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        certificate: str | core.StringOut,
        private_key: str | core.StringOut,
        chain: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SslConfiguration.Args(
                certificate=certificate,
                private_key=private_key,
                chain=chain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: str | core.StringOut = core.arg()

        chain: str | core.StringOut | None = core.arg(default=None)

        private_key: str | core.StringOut = core.arg()


@core.schema
class Environment(core.Schema):

    key: str | core.StringOut = core.attr(str)

    secure: bool | core.BoolOut | None = core.attr(bool, default=None)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
        secure: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Environment.Args(
                key=key,
                value=value,
                secure=secure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        secure: bool | core.BoolOut | None = core.arg(default=None)

        value: str | core.StringOut = core.arg()


@core.schema
class AppSource(core.Schema):

    password: str | core.StringOut | None = core.attr(str, default=None)

    revision: str | core.StringOut | None = core.attr(str, default=None)

    ssh_key: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    url: str | core.StringOut | None = core.attr(str, default=None)

    username: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        password: str | core.StringOut | None = None,
        revision: str | core.StringOut | None = None,
        ssh_key: str | core.StringOut | None = None,
        url: str | core.StringOut | None = None,
        username: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AppSource.Args(
                type=type,
                password=password,
                revision=revision,
                ssh_key=ssh_key,
                url=url,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut | None = core.arg(default=None)

        revision: str | core.StringOut | None = core.arg(default=None)

        ssh_key: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        url: str | core.StringOut | None = core.arg(default=None)

        username: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_opsworks_application", namespace="aws_opsworks")
class Application(core.Resource):

    app_source: list[AppSource] | core.ArrayOut[AppSource] | None = core.attr(
        AppSource, default=None, computed=True, kind=core.Kind.array
    )

    auto_bundle_on_deploy: str | core.StringOut | None = core.attr(str, default=None)

    aws_flow_ruby_settings: str | core.StringOut | None = core.attr(str, default=None)

    data_source_arn: str | core.StringOut | None = core.attr(str, default=None)

    data_source_database_name: str | core.StringOut | None = core.attr(str, default=None)

    data_source_type: str | core.StringOut | None = core.attr(str, default=None)

    description: str | core.StringOut | None = core.attr(str, default=None)

    document_root: str | core.StringOut | None = core.attr(str, default=None)

    domains: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enable_ssl: bool | core.BoolOut | None = core.attr(bool, default=None)

    environment: list[Environment] | core.ArrayOut[Environment] | None = core.attr(
        Environment, default=None, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    rails_env: str | core.StringOut | None = core.attr(str, default=None)

    short_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    ssl_configuration: list[SslConfiguration] | core.ArrayOut[SslConfiguration] | None = core.attr(
        SslConfiguration, default=None, kind=core.Kind.array
    )

    stack_id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        stack_id: str | core.StringOut,
        type: str | core.StringOut,
        app_source: list[AppSource] | core.ArrayOut[AppSource] | None = None,
        auto_bundle_on_deploy: str | core.StringOut | None = None,
        aws_flow_ruby_settings: str | core.StringOut | None = None,
        data_source_arn: str | core.StringOut | None = None,
        data_source_database_name: str | core.StringOut | None = None,
        data_source_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        document_root: str | core.StringOut | None = None,
        domains: list[str] | core.ArrayOut[core.StringOut] | None = None,
        enable_ssl: bool | core.BoolOut | None = None,
        environment: list[Environment] | core.ArrayOut[Environment] | None = None,
        rails_env: str | core.StringOut | None = None,
        short_name: str | core.StringOut | None = None,
        ssl_configuration: list[SslConfiguration] | core.ArrayOut[SslConfiguration] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                stack_id=stack_id,
                type=type,
                app_source=app_source,
                auto_bundle_on_deploy=auto_bundle_on_deploy,
                aws_flow_ruby_settings=aws_flow_ruby_settings,
                data_source_arn=data_source_arn,
                data_source_database_name=data_source_database_name,
                data_source_type=data_source_type,
                description=description,
                document_root=document_root,
                domains=domains,
                enable_ssl=enable_ssl,
                environment=environment,
                rails_env=rails_env,
                short_name=short_name,
                ssl_configuration=ssl_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_source: list[AppSource] | core.ArrayOut[AppSource] | None = core.arg(default=None)

        auto_bundle_on_deploy: str | core.StringOut | None = core.arg(default=None)

        aws_flow_ruby_settings: str | core.StringOut | None = core.arg(default=None)

        data_source_arn: str | core.StringOut | None = core.arg(default=None)

        data_source_database_name: str | core.StringOut | None = core.arg(default=None)

        data_source_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        document_root: str | core.StringOut | None = core.arg(default=None)

        domains: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        enable_ssl: bool | core.BoolOut | None = core.arg(default=None)

        environment: list[Environment] | core.ArrayOut[Environment] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        rails_env: str | core.StringOut | None = core.arg(default=None)

        short_name: str | core.StringOut | None = core.arg(default=None)

        ssl_configuration: list[SslConfiguration] | core.ArrayOut[
            SslConfiguration
        ] | None = core.arg(default=None)

        stack_id: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()
