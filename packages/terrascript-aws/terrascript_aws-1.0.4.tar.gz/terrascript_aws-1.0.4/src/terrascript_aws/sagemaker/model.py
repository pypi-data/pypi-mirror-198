import terrascript.core as core


@core.schema
class RepositoryAuthConfig(core.Schema):

    repository_credentials_provider_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        repository_credentials_provider_arn: str | core.StringOut,
    ):
        super().__init__(
            args=RepositoryAuthConfig.Args(
                repository_credentials_provider_arn=repository_credentials_provider_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_credentials_provider_arn: str | core.StringOut = core.arg()


@core.schema
class ImageConfig(core.Schema):

    repository_access_mode: str | core.StringOut = core.attr(str)

    repository_auth_config: RepositoryAuthConfig | None = core.attr(
        RepositoryAuthConfig, default=None
    )

    def __init__(
        self,
        *,
        repository_access_mode: str | core.StringOut,
        repository_auth_config: RepositoryAuthConfig | None = None,
    ):
        super().__init__(
            args=ImageConfig.Args(
                repository_access_mode=repository_access_mode,
                repository_auth_config=repository_auth_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_access_mode: str | core.StringOut = core.arg()

        repository_auth_config: RepositoryAuthConfig | None = core.arg(default=None)


@core.schema
class PrimaryContainer(core.Schema):

    container_hostname: str | core.StringOut | None = core.attr(str, default=None)

    environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: str | core.StringOut = core.attr(str)

    image_config: ImageConfig | None = core.attr(ImageConfig, default=None)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    model_data_url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image: str | core.StringOut,
        container_hostname: str | core.StringOut | None = None,
        environment: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        image_config: ImageConfig | None = None,
        mode: str | core.StringOut | None = None,
        model_data_url: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PrimaryContainer.Args(
                image=image,
                container_hostname=container_hostname,
                environment=environment,
                image_config=image_config,
                mode=mode,
                model_data_url=model_data_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_hostname: str | core.StringOut | None = core.arg(default=None)

        environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        image: str | core.StringOut = core.arg()

        image_config: ImageConfig | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)

        model_data_url: str | core.StringOut | None = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_group_ids: list[str] | core.ArrayOut[core.StringOut],
        subnets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        subnets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Container(core.Schema):

    container_hostname: str | core.StringOut | None = core.attr(str, default=None)

    environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: str | core.StringOut = core.attr(str)

    image_config: ImageConfig | None = core.attr(ImageConfig, default=None)

    mode: str | core.StringOut | None = core.attr(str, default=None)

    model_data_url: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image: str | core.StringOut,
        container_hostname: str | core.StringOut | None = None,
        environment: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        image_config: ImageConfig | None = None,
        mode: str | core.StringOut | None = None,
        model_data_url: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Container.Args(
                image=image,
                container_hostname=container_hostname,
                environment=environment,
                image_config=image_config,
                mode=mode,
                model_data_url=model_data_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_hostname: str | core.StringOut | None = core.arg(default=None)

        environment: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        image: str | core.StringOut = core.arg()

        image_config: ImageConfig | None = core.arg(default=None)

        mode: str | core.StringOut | None = core.arg(default=None)

        model_data_url: str | core.StringOut | None = core.arg(default=None)


@core.schema
class InferenceExecutionConfig(core.Schema):

    mode: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        mode: str | core.StringOut,
    ):
        super().__init__(
            args=InferenceExecutionConfig.Args(
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode: str | core.StringOut = core.arg()


@core.resource(type="aws_sagemaker_model", namespace="sagemaker")
class Model(core.Resource):
    """
    The Amazon Resource Name (ARN) assigned by AWS to this model.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    container: list[Container] | core.ArrayOut[Container] | None = core.attr(
        Container, default=None, kind=core.Kind.array
    )

    enable_network_isolation: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) A role that SageMaker can assume to access model artifacts and docker images for deployme
    nt.
    """
    execution_role_arn: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies details of how containers in a multi-container endpoint are called. see [Infere
    nce Execution Config](#inference-execution-config).
    """
    inference_execution_config: InferenceExecutionConfig | None = core.attr(
        InferenceExecutionConfig, default=None, computed=True
    )

    """
    (Optional) The name of the model (must be unique). If omitted, Terraform will assign a random, uniqu
    e name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The primary docker image containing inference code that is used when the model is deploye
    d for predictions.  If not specified, the `container` argument is required. Fields are documented be
    low.
    """
    primary_container: PrimaryContainer | None = core.attr(PrimaryContainer, default=None)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
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

    vpc_config: VpcConfig | None = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        execution_role_arn: str | core.StringOut,
        container: list[Container] | core.ArrayOut[Container] | None = None,
        enable_network_isolation: bool | core.BoolOut | None = None,
        inference_execution_config: InferenceExecutionConfig | None = None,
        name: str | core.StringOut | None = None,
        primary_container: PrimaryContainer | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc_config: VpcConfig | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                execution_role_arn=execution_role_arn,
                container=container,
                enable_network_isolation=enable_network_isolation,
                inference_execution_config=inference_execution_config,
                name=name,
                primary_container=primary_container,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container: list[Container] | core.ArrayOut[Container] | None = core.arg(default=None)

        enable_network_isolation: bool | core.BoolOut | None = core.arg(default=None)

        execution_role_arn: str | core.StringOut = core.arg()

        inference_execution_config: InferenceExecutionConfig | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        primary_container: PrimaryContainer | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: VpcConfig | None = core.arg(default=None)
