import terrascript.core as core


@core.schema
class RecordingGroup(core.Schema):

    all_supported: bool | core.BoolOut | None = core.attr(bool, default=None)

    include_global_resource_types: bool | core.BoolOut | None = core.attr(bool, default=None)

    resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        all_supported: bool | core.BoolOut | None = None,
        include_global_resource_types: bool | core.BoolOut | None = None,
        resource_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=RecordingGroup.Args(
                all_supported=all_supported,
                include_global_resource_types=include_global_resource_types,
                resource_types=resource_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_supported: bool | core.BoolOut | None = core.arg(default=None)

        include_global_resource_types: bool | core.BoolOut | None = core.arg(default=None)

        resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.resource(type="aws_config_configuration_recorder", namespace="config")
class ConfigurationRecorder(core.Resource):
    """
    Name of the recorder
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name of the recorder. Defaults to `default`. Changing it recreates the resource.
    """
    name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Recording group - see below.
    """
    recording_group: RecordingGroup | None = core.attr(RecordingGroup, default=None, computed=True)

    """
    (Required) Amazon Resource Name (ARN) of the IAM role. Used to make read or write requests to the de
    livery channel and to describe the AWS resources associated with the account. See [AWS Docs](http://
    docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.
    """
    role_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        role_arn: str | core.StringOut,
        name: str | core.StringOut | None = None,
        recording_group: RecordingGroup | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationRecorder.Args(
                role_arn=role_arn,
                name=name,
                recording_group=recording_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: str | core.StringOut | None = core.arg(default=None)

        recording_group: RecordingGroup | None = core.arg(default=None)

        role_arn: str | core.StringOut = core.arg()
