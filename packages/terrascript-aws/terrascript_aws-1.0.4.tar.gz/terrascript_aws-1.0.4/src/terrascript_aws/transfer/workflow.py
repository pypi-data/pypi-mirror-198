import terrascript.core as core


@core.schema
class EfsFileLocation(core.Schema):

    file_system_id: str | core.StringOut | None = core.attr(str, default=None)

    path: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        file_system_id: str | core.StringOut | None = None,
        path: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=EfsFileLocation.Args(
                file_system_id=file_system_id,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_id: str | core.StringOut | None = core.arg(default=None)

        path: str | core.StringOut | None = core.arg(default=None)


@core.schema
class S3FileLocation(core.Schema):

    bucket: str | core.StringOut | None = core.attr(str, default=None)

    key: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut | None = None,
        key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=S3FileLocation.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)


@core.schema
class DestinationFileLocation(core.Schema):

    efs_file_location: EfsFileLocation | None = core.attr(EfsFileLocation, default=None)

    s3_file_location: S3FileLocation | None = core.attr(S3FileLocation, default=None)

    def __init__(
        self,
        *,
        efs_file_location: EfsFileLocation | None = None,
        s3_file_location: S3FileLocation | None = None,
    ):
        super().__init__(
            args=DestinationFileLocation.Args(
                efs_file_location=efs_file_location,
                s3_file_location=s3_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        efs_file_location: EfsFileLocation | None = core.arg(default=None)

        s3_file_location: S3FileLocation | None = core.arg(default=None)


@core.schema
class CopyStepDetails(core.Schema):

    destination_file_location: DestinationFileLocation | None = core.attr(
        DestinationFileLocation, default=None
    )

    name: str | core.StringOut | None = core.attr(str, default=None)

    overwrite_existing: str | core.StringOut | None = core.attr(str, default=None)

    source_file_location: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination_file_location: DestinationFileLocation | None = None,
        name: str | core.StringOut | None = None,
        overwrite_existing: str | core.StringOut | None = None,
        source_file_location: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CopyStepDetails.Args(
                destination_file_location=destination_file_location,
                name=name,
                overwrite_existing=overwrite_existing,
                source_file_location=source_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_file_location: DestinationFileLocation | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        overwrite_existing: str | core.StringOut | None = core.arg(default=None)

        source_file_location: str | core.StringOut | None = core.arg(default=None)


@core.schema
class CustomStepDetails(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    source_file_location: str | core.StringOut | None = core.attr(str, default=None)

    target: str | core.StringOut | None = core.attr(str, default=None)

    timeout_seconds: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        source_file_location: str | core.StringOut | None = None,
        target: str | core.StringOut | None = None,
        timeout_seconds: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=CustomStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
                target=target,
                timeout_seconds=timeout_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        source_file_location: str | core.StringOut | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)

        timeout_seconds: int | core.IntOut | None = core.arg(default=None)


@core.schema
class DeleteStepDetails(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    source_file_location: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        source_file_location: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=DeleteStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        source_file_location: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Tags(core.Schema):

    key: str | core.StringOut = core.attr(str)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Tags.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.schema
class TagStepDetails(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    source_file_location: str | core.StringOut | None = core.attr(str, default=None)

    tags: list[Tags] | core.ArrayOut[Tags] | None = core.attr(
        Tags, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        source_file_location: str | core.StringOut | None = None,
        tags: list[Tags] | core.ArrayOut[Tags] | None = None,
    ):
        super().__init__(
            args=TagStepDetails.Args(
                name=name,
                source_file_location=source_file_location,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        source_file_location: str | core.StringOut | None = core.arg(default=None)

        tags: list[Tags] | core.ArrayOut[Tags] | None = core.arg(default=None)


@core.schema
class Steps(core.Schema):

    copy_step_details: CopyStepDetails | None = core.attr(CopyStepDetails, default=None)

    custom_step_details: CustomStepDetails | None = core.attr(CustomStepDetails, default=None)

    delete_step_details: DeleteStepDetails | None = core.attr(DeleteStepDetails, default=None)

    tag_step_details: TagStepDetails | None = core.attr(TagStepDetails, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        copy_step_details: CopyStepDetails | None = None,
        custom_step_details: CustomStepDetails | None = None,
        delete_step_details: DeleteStepDetails | None = None,
        tag_step_details: TagStepDetails | None = None,
    ):
        super().__init__(
            args=Steps.Args(
                type=type,
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_step_details: CopyStepDetails | None = core.arg(default=None)

        custom_step_details: CustomStepDetails | None = core.arg(default=None)

        delete_step_details: DeleteStepDetails | None = core.arg(default=None)

        tag_step_details: TagStepDetails | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class OnExceptionSteps(core.Schema):

    copy_step_details: CopyStepDetails | None = core.attr(CopyStepDetails, default=None)

    custom_step_details: CustomStepDetails | None = core.attr(CustomStepDetails, default=None)

    delete_step_details: DeleteStepDetails | None = core.attr(DeleteStepDetails, default=None)

    tag_step_details: TagStepDetails | None = core.attr(TagStepDetails, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        copy_step_details: CopyStepDetails | None = None,
        custom_step_details: CustomStepDetails | None = None,
        delete_step_details: DeleteStepDetails | None = None,
        tag_step_details: TagStepDetails | None = None,
    ):
        super().__init__(
            args=OnExceptionSteps.Args(
                type=type,
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_step_details: CopyStepDetails | None = core.arg(default=None)

        custom_step_details: CustomStepDetails | None = core.arg(default=None)

        delete_step_details: DeleteStepDetails | None = core.arg(default=None)

        tag_step_details: TagStepDetails | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_transfer_workflow", namespace="transfer")
class Workflow(core.Resource):
    """
    The Workflow ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A textual description for the workflow.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Workflow id.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies the steps (actions) to take if errors are encountered during execution of the w
    orkflow. See Workflow Steps below.
    """
    on_exception_steps: list[OnExceptionSteps] | core.ArrayOut[OnExceptionSteps] | None = core.attr(
        OnExceptionSteps, default=None, kind=core.Kind.array
    )

    """
    (Required) Specifies the details for the steps that are in the specified workflow. See Workflow Step
    s below.
    """
    steps: list[Steps] | core.ArrayOut[Steps] = core.attr(Steps, kind=core.Kind.array)

    """
    (Optional) A map of tags to assign to the resource. If configured with a provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block) present, tags with matching keys will overwrite those defined at the provider-lev
    el.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        steps: list[Steps] | core.ArrayOut[Steps],
        description: str | core.StringOut | None = None,
        on_exception_steps: list[OnExceptionSteps] | core.ArrayOut[OnExceptionSteps] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workflow.Args(
                steps=steps,
                description=description,
                on_exception_steps=on_exception_steps,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        on_exception_steps: list[OnExceptionSteps] | core.ArrayOut[
            OnExceptionSteps
        ] | None = core.arg(default=None)

        steps: list[Steps] | core.ArrayOut[Steps] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
