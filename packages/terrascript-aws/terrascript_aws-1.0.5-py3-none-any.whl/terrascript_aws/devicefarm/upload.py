import terrascript.core as core


@core.resource(type="aws_devicefarm_upload", namespace="devicefarm")
class Upload(core.Resource):
    """
    The Amazon Resource Name of this upload.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The upload's category.
    """
    category: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The upload's content type (for example, application/octet-stream).
    """
    content_type: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The upload's metadata. For example, for Android, this contains information that is parsed from the m
    anifest and is displayed in the AWS Device Farm console after the associated app is uploaded.
    """
    metadata: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The upload's file name. The name should not contain any forward slashes (/). If you are u
    ploading an iOS app, the file name must end with the .ipa extension. If you are uploading an Android
    app, the file name must end with the .apk extension. For all others, the file name must end with th
    e .zip file extension.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of the project for the upload.
    """
    project_arn: str | core.StringOut = core.attr(str)

    """
    (Required) The upload's upload type. See [AWS Docs](https://docs.aws.amazon.com/devicefarm/latest/AP
    IReference/API_CreateUpload.html#API_CreateUpload_RequestSyntax) for valid list of values.
    """
    type: str | core.StringOut = core.attr(str)

    """
    The presigned Amazon S3 URL that was used to store a file using a PUT request.
    """
    url: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        project_arn: str | core.StringOut,
        type: str | core.StringOut,
        content_type: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Upload.Args(
                name=name,
                project_arn=project_arn,
                type=type,
                content_type=content_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_type: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        project_arn: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()
