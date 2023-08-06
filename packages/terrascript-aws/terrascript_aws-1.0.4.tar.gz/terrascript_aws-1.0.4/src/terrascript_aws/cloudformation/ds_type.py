import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: str | core.StringOut = core.attr(str, computed=True)

    log_role_arn: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        log_group_name: str | core.StringOut,
        log_role_arn: str | core.StringOut,
    ):
        super().__init__(
            args=LoggingConfig.Args(
                log_group_name=log_group_name,
                log_role_arn=log_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name: str | core.StringOut = core.arg()

        log_role_arn: str | core.StringOut = core.arg()


@core.data(type="aws_cloudformation_type", namespace="cloudformation")
class DsType(core.Data):
    """
    (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. For example, `arn:aws:cloudformati
    on:us-west-2::type/resource/AWS-EC2-VPC`.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Identifier of the CloudFormation Type default version.
    """
    default_version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Deprecation status of the CloudFormation Type.
    """
    deprecated_status: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the CloudFormation Type.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    URL of the documentation for the CloudFormation Type.
    """
    documentation_url: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the IAM Role used to register the CloudFormation Type.
    """
    execution_role_arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the CloudFormation Type version is the default version.
    """
    is_default_version: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    List of objects containing logging configuration.
    """
    logging_config: list[LoggingConfig] | core.ArrayOut[LoggingConfig] = core.attr(
        LoggingConfig, computed=True, kind=core.Kind.array
    )

    """
    Provisioning behavior of the CloudFormation Type.
    """
    provisioning_type: str | core.StringOut = core.attr(str, computed=True)

    """
    JSON document of the CloudFormation Type schema.
    """
    schema: str | core.StringOut = core.attr(str, computed=True)

    """
    URL of the source code for the CloudFormation Type.
    """
    source_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) CloudFormation Registry Type. For example, `RESOURCE`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) CloudFormation Type name. For example, `AWS::EC2::VPC`.
    """
    type_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Identifier of the CloudFormation Type version.
    """
    version_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    Scope of the CloudFormation Type.
    """
    visibility: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        type: str | core.StringOut | None = None,
        type_name: str | core.StringOut | None = None,
        version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsType.Args(
                arn=arn,
                type=type,
                type_name=type_name,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut | None = core.arg(default=None)

        version_id: str | core.StringOut | None = core.arg(default=None)
