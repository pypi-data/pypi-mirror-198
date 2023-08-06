import terrascript.core as core


@core.resource(type="aws_glue_dev_endpoint", namespace="glue")
class DevEndpoint(core.Resource):

    arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    arn: str | core.StringOut = core.attr(str, computed=True)

    availability_zone: str | core.StringOut = core.attr(str, computed=True)

    extra_jars_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    extra_python_libs_s3_path: str | core.StringOut | None = core.attr(str, default=None)

    failure_reason: str | core.StringOut = core.attr(str, computed=True)

    glue_version: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    number_of_nodes: int | core.IntOut | None = core.attr(int, default=None)

    number_of_workers: int | core.IntOut | None = core.attr(int, default=None)

    private_address: str | core.StringOut = core.attr(str, computed=True)

    public_address: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut | None = core.attr(str, default=None)

    public_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: str | core.StringOut = core.attr(str)

    security_configuration: str | core.StringOut | None = core.attr(str, default=None)

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: str | core.StringOut = core.attr(str, computed=True)

    worker_type: str | core.StringOut | None = core.attr(str, default=None)

    yarn_endpoint_address: str | core.StringOut = core.attr(str, computed=True)

    zeppelin_remote_spark_interpreter_port: int | core.IntOut = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        arguments: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        extra_jars_s3_path: str | core.StringOut | None = None,
        extra_python_libs_s3_path: str | core.StringOut | None = None,
        glue_version: str | core.StringOut | None = None,
        number_of_nodes: int | core.IntOut | None = None,
        number_of_workers: int | core.IntOut | None = None,
        public_key: str | core.StringOut | None = None,
        public_keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
        security_configuration: str | core.StringOut | None = None,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        worker_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DevEndpoint.Args(
                name=name,
                role_arn=role_arn,
                arguments=arguments,
                extra_jars_s3_path=extra_jars_s3_path,
                extra_python_libs_s3_path=extra_python_libs_s3_path,
                glue_version=glue_version,
                number_of_nodes=number_of_nodes,
                number_of_workers=number_of_workers,
                public_key=public_key,
                public_keys=public_keys,
                security_configuration=security_configuration,
                security_group_ids=security_group_ids,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arguments: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        extra_jars_s3_path: str | core.StringOut | None = core.arg(default=None)

        extra_python_libs_s3_path: str | core.StringOut | None = core.arg(default=None)

        glue_version: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        number_of_nodes: int | core.IntOut | None = core.arg(default=None)

        number_of_workers: int | core.IntOut | None = core.arg(default=None)

        public_key: str | core.StringOut | None = core.arg(default=None)

        public_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()

        security_configuration: str | core.StringOut | None = core.arg(default=None)

        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        worker_type: str | core.StringOut | None = core.arg(default=None)
