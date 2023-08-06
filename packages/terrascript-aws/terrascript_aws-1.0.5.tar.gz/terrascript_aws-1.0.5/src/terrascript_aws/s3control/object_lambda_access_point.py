import terrascript.core as core


@core.schema
class AwsLambda(core.Schema):

    function_arn: str | core.StringOut = core.attr(str)

    function_payload: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        function_arn: str | core.StringOut,
        function_payload: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AwsLambda.Args(
                function_arn=function_arn,
                function_payload=function_payload,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: str | core.StringOut = core.arg()

        function_payload: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ContentTransformation(core.Schema):

    aws_lambda: AwsLambda = core.attr(AwsLambda)

    def __init__(
        self,
        *,
        aws_lambda: AwsLambda,
    ):
        super().__init__(
            args=ContentTransformation.Args(
                aws_lambda=aws_lambda,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_lambda: AwsLambda = core.arg()


@core.schema
class TransformationConfiguration(core.Schema):

    actions: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    content_transformation: ContentTransformation = core.attr(ContentTransformation)

    def __init__(
        self,
        *,
        actions: list[str] | core.ArrayOut[core.StringOut],
        content_transformation: ContentTransformation,
    ):
        super().__init__(
            args=TransformationConfiguration.Args(
                actions=actions,
                content_transformation=content_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        content_transformation: ContentTransformation = core.arg()


@core.schema
class Configuration(core.Schema):

    allowed_features: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cloud_watch_metrics_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    supporting_access_point: str | core.StringOut = core.attr(str)

    transformation_configuration: list[TransformationConfiguration] | core.ArrayOut[
        TransformationConfiguration
    ] = core.attr(TransformationConfiguration, kind=core.Kind.array)

    def __init__(
        self,
        *,
        supporting_access_point: str | core.StringOut,
        transformation_configuration: list[TransformationConfiguration]
        | core.ArrayOut[TransformationConfiguration],
        allowed_features: list[str] | core.ArrayOut[core.StringOut] | None = None,
        cloud_watch_metrics_enabled: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            args=Configuration.Args(
                supporting_access_point=supporting_access_point,
                transformation_configuration=transformation_configuration,
                allowed_features=allowed_features,
                cloud_watch_metrics_enabled=cloud_watch_metrics_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_features: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        cloud_watch_metrics_enabled: bool | core.BoolOut | None = core.arg(default=None)

        supporting_access_point: str | core.StringOut = core.arg()

        transformation_configuration: list[TransformationConfiguration] | core.ArrayOut[
            TransformationConfiguration
        ] = core.arg()


@core.resource(type="aws_s3control_object_lambda_access_point", namespace="s3control")
class ObjectLambdaAccessPoint(core.Resource):
    """
    (Optional) The AWS account ID for the owner of the bucket for which you want to create an Object Lam
    bda Access Point. Defaults to automatically determined account ID of the Terraform AWS provider.
    """

    account_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Amazon Resource Name (ARN) of the Object Lambda Access Point.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A configuration block containing details about the Object Lambda Access Point. See [Confi
    guration](#configuration) below for more details.
    """
    configuration: Configuration = core.attr(Configuration)

    """
    The AWS account ID and access point name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name for this Object Lambda Access Point.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        configuration: Configuration,
        name: str | core.StringOut,
        account_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObjectLambdaAccessPoint.Args(
                configuration=configuration,
                name=name,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: str | core.StringOut | None = core.arg(default=None)

        configuration: Configuration = core.arg()

        name: str | core.StringOut = core.arg()
