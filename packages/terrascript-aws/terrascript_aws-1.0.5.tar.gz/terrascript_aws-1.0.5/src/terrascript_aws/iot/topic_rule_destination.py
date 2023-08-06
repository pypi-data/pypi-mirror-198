import terrascript.core as core


@core.schema
class VpcConfiguration(core.Schema):

    role_arn: str | core.StringOut = core.attr(str)

    security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    vpc_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: str | core.StringOut,
        subnet_ids: list[str] | core.ArrayOut[core.StringOut],
        vpc_id: str | core.StringOut,
        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                role_arn=role_arn,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
                security_groups=security_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: str | core.StringOut = core.arg()

        security_groups: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        vpc_id: str | core.StringOut = core.arg()


@core.resource(type="aws_iot_topic_rule_destination", namespace="iot")
class TopicRuleDestination(core.Resource):
    """
    The ARN of the topic rule destination
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Whether or not to enable the destination. Default: `true`.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Configuration of the virtual private cloud (VPC) connection. For more info, see the [AWS
    documentation](https://docs.aws.amazon.com/iot/latest/developerguide/vpc-rule-action.html).
    """
    vpc_configuration: VpcConfiguration = core.attr(VpcConfiguration)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_configuration: VpcConfiguration,
        enabled: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicRuleDestination.Args(
                vpc_configuration=vpc_configuration,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        vpc_configuration: VpcConfiguration = core.arg()
