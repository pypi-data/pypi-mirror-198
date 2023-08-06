import terrascript.core as core


@core.schema
class LoggingConfig(core.Schema):

    log_group_name: str | core.StringOut = core.attr(str)

    log_role_arn: str | core.StringOut = core.attr(str)

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


@core.resource(type="aws_cloudformation_type", namespace="cloudformation")
class Type(core.Resource):
    """
    (Optional) Amazon Resource Name (ARN) of the CloudFormation Type version. See also `type_arn`.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Identifier of the CloudFormation Type default version.
    """
    default_version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Deprecation status of the version.
    """
    deprecated_status: str | core.StringOut = core.attr(str, computed=True)

    """
    Description of the version.
    """
    description: str | core.StringOut = core.attr(str, computed=True)

    """
    URL of the documentation for the CloudFormation Type.
    """
    documentation_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the
    extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM executio
    n role that includes the necessary permissions to call those AWS APIs, and provision that execution
    role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assu
    mes this execution role to create a temporary session token, which it then passes to the extension h
    andler, thereby supplying your extension with the appropriate credentials.
    """
    execution_role_arn: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the CloudFormation Type version is the default version.
    """
    is_default_version: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional) Configuration block containing logging configuration.
    """
    logging_config: LoggingConfig | None = core.attr(LoggingConfig, default=None)

    """
    Provisioning behavior of the CloudFormation Type.
    """
    provisioning_type: str | core.StringOut = core.attr(str, computed=True)

    """
    JSON document of the CloudFormation Type schema.
    """
    schema: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) URL to the S3 bucket containing the extension project package that contains the necessary
    files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `
    s3://example-bucket/example-object`.
    """
    schema_handler_package: str | core.StringOut = core.attr(str)

    """
    URL of the source code for the CloudFormation Type.
    """
    source_url: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.
    """
    type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the CloudFormation Type. See also `arn`.
    """
    type_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.
    """
    type_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Identifier of the CloudFormation Type version.
    """
    version_id: str | core.StringOut = core.attr(str, computed=True)

    """
    Scope of the CloudFormation Type.
    """
    visibility: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        schema_handler_package: str | core.StringOut,
        type_name: str | core.StringOut,
        execution_role_arn: str | core.StringOut | None = None,
        logging_config: LoggingConfig | None = None,
        type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Type.Args(
                schema_handler_package=schema_handler_package,
                type_name=type_name,
                execution_role_arn=execution_role_arn,
                logging_config=logging_config,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        execution_role_arn: str | core.StringOut | None = core.arg(default=None)

        logging_config: LoggingConfig | None = core.arg(default=None)

        schema_handler_package: str | core.StringOut = core.arg()

        type: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()
