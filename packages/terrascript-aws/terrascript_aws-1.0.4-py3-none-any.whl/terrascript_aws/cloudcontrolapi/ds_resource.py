import terrascript.core as core


@core.data(type="aws_cloudcontrolapi_resource", namespace="cloudcontrolapi")
class DsResource(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Identifier of the CloudFormation resource type. For example, `vpc-12345678`.
    """
    identifier: str | core.StringOut = core.attr(str)

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
    (Required) CloudFormation resource type name. For example, `AWS::EC2::VPC`.
    """
    type_name: str | core.StringOut = core.attr(str)

    """
    (Optional) Identifier of the CloudFormation resource type version.
    """
    type_version_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        identifier: str | core.StringOut,
        type_name: str | core.StringOut,
        role_arn: str | core.StringOut | None = None,
        type_version_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                identifier=identifier,
                type_name=type_name,
                role_arn=role_arn,
                type_version_id=type_version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifier: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        type_name: str | core.StringOut = core.arg()

        type_version_id: str | core.StringOut | None = core.arg(default=None)
