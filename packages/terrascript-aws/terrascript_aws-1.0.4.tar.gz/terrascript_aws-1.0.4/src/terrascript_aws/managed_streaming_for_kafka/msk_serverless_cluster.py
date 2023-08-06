import terrascript.core as core


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                subnet_ids=subnet_ids,
                security_group_ids=security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class Iam(core.Schema):

    enabled: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut,
    ):
        super().__init__(
            args=Iam.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut = core.arg()


@core.schema
class Sasl(core.Schema):

    iam: Iam = core.attr(Iam)

    def __init__(
        self,
        *,
        iam: Iam,
    ):
        super().__init__(
            args=Sasl.Args(
                iam=iam,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam: Iam = core.arg()


@core.schema
class ClientAuthentication(core.Schema):

    sasl: Sasl = core.attr(Sasl)

    def __init__(
        self,
        *,
        sasl: Sasl,
    ):
        super().__init__(
            args=ClientAuthentication.Args(
                sasl=sasl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sasl: Sasl = core.arg()


@core.resource(type="aws_msk_serverless_cluster", namespace="managed_streaming_for_kafka")
class MskServerlessCluster(core.Resource):
    """
    The ARN of the serverless cluster.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Specifies client authentication information for the serverless cluster. See below.
    """
    client_authentication: ClientAuthentication = core.attr(ClientAuthentication)

    """
    (Required) The name of the serverless cluster.
    """
    cluster_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

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

    """
    (Required) VPC configuration information. See below.
    """
    vpc_config: list[VpcConfig] | core.ArrayOut[VpcConfig] = core.attr(
        VpcConfig, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        client_authentication: ClientAuthentication,
        cluster_name: str | core.StringOut,
        vpc_config: list[VpcConfig] | core.ArrayOut[VpcConfig],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskServerlessCluster.Args(
                client_authentication=client_authentication,
                cluster_name=cluster_name,
                vpc_config=vpc_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_authentication: ClientAuthentication = core.arg()

        cluster_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc_config: list[VpcConfig] | core.ArrayOut[VpcConfig] = core.arg()
