import terrascript.core as core


@core.resource(type="aws_mq_configuration", namespace="mq")
class Configuration(core.Resource):
    """
    ARN of the configuration.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Authentication strategy associated with the configuration. Valid values are `simple` and
    ldap`. `ldap` is not supported for `engine_type` `RabbitMQ`.
    """
    authentication_strategy: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) Broker configuration in XML format. See [official docs](https://docs.aws.amazon.com/amazo
    n-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html) for supported parameters
    and format of the XML.
    """
    data: str | core.StringOut = core.attr(str)

    """
    (Optional) Description of the configuration.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Type of broker engine. Valid values are `ActiveMQ` and `RabbitMQ`.
    """
    engine_type: str | core.StringOut = core.attr(str)

    """
    (Required) Version of the broker engine.
    """
    engine_version: str | core.StringOut = core.attr(str)

    """
    Unique ID that Amazon MQ generates for the configuration.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Latest revision of the configuration.
    """
    latest_revision: int | core.IntOut = core.attr(int, computed=True)

    """
    (Required) Name of the configuration.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
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
        data: str | core.StringOut,
        engine_type: str | core.StringOut,
        engine_version: str | core.StringOut,
        name: str | core.StringOut,
        authentication_strategy: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Configuration.Args(
                data=data,
                engine_type=engine_type,
                engine_version=engine_version,
                name=name,
                authentication_strategy=authentication_strategy,
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
        authentication_strategy: str | core.StringOut | None = core.arg(default=None)

        data: str | core.StringOut = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        engine_type: str | core.StringOut = core.arg()

        engine_version: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
