import terrascript.core as core


@core.schema
class ContentConfig(core.Schema):

    bucket: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    storage_class: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut | None = None,
        storage_class: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ContentConfig.Args(
                bucket=bucket,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ThumbnailConfig(core.Schema):

    bucket: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    storage_class: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: str | core.StringOut | None = None,
        storage_class: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ThumbnailConfig.Args(
                bucket=bucket,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: str | core.StringOut | None = core.arg(default=None)

        storage_class: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Notifications(core.Schema):

    completed: str | core.StringOut | None = core.attr(str, default=None)

    error: str | core.StringOut | None = core.attr(str, default=None)

    progressing: str | core.StringOut | None = core.attr(str, default=None)

    warning: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        completed: str | core.StringOut | None = None,
        error: str | core.StringOut | None = None,
        progressing: str | core.StringOut | None = None,
        warning: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Notifications.Args(
                completed=completed,
                error=error,
                progressing=progressing,
                warning=warning,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        completed: str | core.StringOut | None = core.arg(default=None)

        error: str | core.StringOut | None = core.arg(default=None)

        progressing: str | core.StringOut | None = core.arg(default=None)

        warning: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ContentConfigPermissions(core.Schema):

    access: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grantee: str | core.StringOut | None = core.attr(str, default=None)

    grantee_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access: list[str] | core.ArrayOut[core.StringOut] | None = None,
        grantee: str | core.StringOut | None = None,
        grantee_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ContentConfigPermissions.Args(
                access=access,
                grantee=grantee,
                grantee_type=grantee_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        grantee: str | core.StringOut | None = core.arg(default=None)

        grantee_type: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ThumbnailConfigPermissions(core.Schema):

    access: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grantee: str | core.StringOut | None = core.attr(str, default=None)

    grantee_type: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access: list[str] | core.ArrayOut[core.StringOut] | None = None,
        grantee: str | core.StringOut | None = None,
        grantee_type: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ThumbnailConfigPermissions.Args(
                access=access,
                grantee=grantee,
                grantee_type=grantee_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        grantee: str | core.StringOut | None = core.arg(default=None)

        grantee_type: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_elastictranscoder_pipeline", namespace="aws_elastictranscoder")
class Pipeline(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    aws_kms_key_arn: str | core.StringOut | None = core.attr(str, default=None)

    content_config: ContentConfig | None = core.attr(ContentConfig, default=None, computed=True)

    content_config_permissions: list[ContentConfigPermissions] | core.ArrayOut[
        ContentConfigPermissions
    ] | None = core.attr(ContentConfigPermissions, default=None, kind=core.Kind.array)

    id: str | core.StringOut = core.attr(str, computed=True)

    input_bucket: str | core.StringOut = core.attr(str)

    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    notifications: Notifications | None = core.attr(Notifications, default=None)

    output_bucket: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role: str | core.StringOut = core.attr(str)

    thumbnail_config: ThumbnailConfig | None = core.attr(
        ThumbnailConfig, default=None, computed=True
    )

    thumbnail_config_permissions: list[ThumbnailConfigPermissions] | core.ArrayOut[
        ThumbnailConfigPermissions
    ] | None = core.attr(ThumbnailConfigPermissions, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        input_bucket: str | core.StringOut,
        role: str | core.StringOut,
        aws_kms_key_arn: str | core.StringOut | None = None,
        content_config: ContentConfig | None = None,
        content_config_permissions: list[ContentConfigPermissions]
        | core.ArrayOut[ContentConfigPermissions]
        | None = None,
        name: str | core.StringOut | None = None,
        notifications: Notifications | None = None,
        output_bucket: str | core.StringOut | None = None,
        thumbnail_config: ThumbnailConfig | None = None,
        thumbnail_config_permissions: list[ThumbnailConfigPermissions]
        | core.ArrayOut[ThumbnailConfigPermissions]
        | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Pipeline.Args(
                input_bucket=input_bucket,
                role=role,
                aws_kms_key_arn=aws_kms_key_arn,
                content_config=content_config,
                content_config_permissions=content_config_permissions,
                name=name,
                notifications=notifications,
                output_bucket=output_bucket,
                thumbnail_config=thumbnail_config,
                thumbnail_config_permissions=thumbnail_config_permissions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_kms_key_arn: str | core.StringOut | None = core.arg(default=None)

        content_config: ContentConfig | None = core.arg(default=None)

        content_config_permissions: list[ContentConfigPermissions] | core.ArrayOut[
            ContentConfigPermissions
        ] | None = core.arg(default=None)

        input_bucket: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        notifications: Notifications | None = core.arg(default=None)

        output_bucket: str | core.StringOut | None = core.arg(default=None)

        role: str | core.StringOut = core.arg()

        thumbnail_config: ThumbnailConfig | None = core.arg(default=None)

        thumbnail_config_permissions: list[ThumbnailConfigPermissions] | core.ArrayOut[
            ThumbnailConfigPermissions
        ] | None = core.arg(default=None)
