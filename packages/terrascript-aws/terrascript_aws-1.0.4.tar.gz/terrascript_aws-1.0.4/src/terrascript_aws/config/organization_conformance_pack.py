import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    parameter_name: str | core.StringOut = core.attr(str)

    parameter_value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        parameter_name: str | core.StringOut,
        parameter_value: str | core.StringOut,
    ):
        super().__init__(
            args=InputParameter.Args(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_name: str | core.StringOut = core.arg()

        parameter_value: str | core.StringOut = core.arg()


@core.resource(type="aws_config_organization_conformance_pack", namespace="config")
class OrganizationConformancePack(core.Resource):
    """
    Amazon Resource Name (ARN) of the organization conformance pack.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon S3 bucket where AWS Config stores conformance pack templates. Delivery bucket must
    begin with `awsconfigconforms` prefix. Maximum length of 63.
    """
    delivery_s3_bucket: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The prefix for the Amazon S3 bucket. Maximum length of 1024.
    """
    delivery_s3_key_prefix: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Set of AWS accounts to be excluded from an organization conformance pack while deploying
    a conformance pack. Maximum of 1000 accounts.
    """
    excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The name of the organization conformance pack.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Set of configuration blocks describing input parameters passed to the conformance pack te
    mplate. Documented below. When configured, the parameters must also be included in the `template_bod
    y` or in the template stored in Amazon S3 if using `template_s3_uri`.
    """
    input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.attr(
        InputParameter, default=None, kind=core.Kind.array
    )

    """
    (Required, Forces new resource) The name of the organization conformance pack. Must begin with a let
    ter and contain from 1 to 128 alphanumeric characters and hyphens.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional, Conflicts with `template_s3_uri`) A string containing full conformance pack template body
    . Maximum length of 51200. Drift detection is not possible with this argument.
    """
    template_body: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional, Conflicts with `template_body`) Location of file, e.g., `s3://bucketname/prefix`, contain
    ing the template body. The uri must point to the conformance pack template that is located in an Ama
    zon S3 bucket in the same region as the conformance pack. Maximum length of 1024. Drift detection is
    not possible with this argument.
    """
    template_s3_uri: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        delivery_s3_bucket: str | core.StringOut | None = None,
        delivery_s3_key_prefix: str | core.StringOut | None = None,
        excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = None,
        template_body: str | core.StringOut | None = None,
        template_s3_uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConformancePack.Args(
                name=name,
                delivery_s3_bucket=delivery_s3_bucket,
                delivery_s3_key_prefix=delivery_s3_key_prefix,
                excluded_accounts=excluded_accounts,
                input_parameter=input_parameter,
                template_body=template_body,
                template_s3_uri=template_s3_uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delivery_s3_bucket: str | core.StringOut | None = core.arg(default=None)

        delivery_s3_key_prefix: str | core.StringOut | None = core.arg(default=None)

        excluded_accounts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        template_body: str | core.StringOut | None = core.arg(default=None)

        template_s3_uri: str | core.StringOut | None = core.arg(default=None)
