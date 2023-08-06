import terrascript.core as core


@core.resource(type="aws_cloudcontrolapi_resource", namespace="cloudcontrolapi")
class Resource(core.Resource):
    """
    (Required) JSON string matching the CloudFormation resource type schema with desired configuration.
    Terraform configuration expressions can be converted into JSON using the [`jsonencode()` function](h
    ttps://www.terraform.io/docs/language/functions/jsonencode.html).
    """

    desired_state: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    JSON string matching the CloudFormation resource type schema with current configuration. Underlying
    attributes can be referenced via the [`jsondecode()` function](https://www.terraform.io/docs/languag
    e/functions/jsondecode.html), for example, `jsondecode(data.aws_cloudcontrolapi_resource.example.pro
    perties)["example"]`.
    """
    properties: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the IAM Role to assume for operations.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) JSON string of the CloudFormation resource type schema which is used for plan time valida
    tion where possible. Automatically fetched if not provided. In large scale environments with multipl
    e resources using the same `type_name`, it is recommended to fetch the schema once via the [`aws_clo
    udformation_type` data source](/docs/providers/aws/d/cloudformation_type.html) and use this argument
    to reduce `DescribeType` API operation throttling. This value is marked sensitive only to prevent l
    arge plan differences from showing.
    """
    schema: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) CloudFormation resource type name. For example, `AWS::EC2::VPC`.
    """
    type_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Identifier of the CloudFormation resource type version.
    """
    type_version_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        desired_state: str | core.StringOut,
        type_name: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        schema: str | core.StringOut | None = None,
        type_version_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resource.Args(
                desired_state=desired_state,
                type_name=type_name,
                role_arn=role_arn,
                schema=schema,
                type_version_id=type_version_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        desired_state: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        schema: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()

        type_version_id: str | core.StringOut | None = core.arg(default=None)
