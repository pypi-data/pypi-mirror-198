import terrascript.core as core


@core.data(type="aws_api_gateway_sdk", namespace="api_gateway")
class DsSdk(core.Data):
    """
    The SDK as a string.
    """

    body: str | core.StringOut = core.attr(str, computed=True)

    """
    The content-disposition header value in the HTTP response.
    """
    content_disposition: str | core.StringOut = core.attr(str, computed=True)

    """
    The content-type header value in the HTTP response.
    """
    content_type: str | core.StringOut = core.attr(str, computed=True)

    """
    The `REST-API-ID:STAGE-NAME`
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A key-value map of query string parameters `sdk_type` properties of the SDK. For SDK Type
    of `objectivec` or `swift`, a parameter named `classPrefix` is required. For SDK Type of `android`,
    parameters named `groupId`, `artifactId`, `artifactVersion`, and `invokerPackage` are required. For
    SDK Type of `java`, parameters named `serviceName` and `javaPackageName` are required.
    """
    parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The identifier of the associated REST API.
    """
    rest_api_id: str | core.StringOut = core.attr(str)

    """
    (Required) The language for the generated SDK. Currently `java`, `javascript`, `android`, `objective
    c` (for iOS), `swift` (for iOS), and `ruby` are supported.
    """
    sdk_type: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the Stage that will be exported.
    """
    stage_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        rest_api_id: str | core.StringOut,
        sdk_type: str | core.StringOut,
        stage_name: str | core.StringOut,
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSdk.Args(
                rest_api_id=rest_api_id,
                sdk_type=sdk_type,
                stage_name=stage_name,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        rest_api_id: str | core.StringOut = core.arg()

        sdk_type: str | core.StringOut = core.arg()

        stage_name: str | core.StringOut = core.arg()
