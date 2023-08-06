import terrascript.core as core


@core.schema
class QueryArgProfilesItems(core.Schema):

    profile_id: str | core.StringOut = core.attr(str)

    query_arg: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        profile_id: str | core.StringOut,
        query_arg: str | core.StringOut,
    ):
        super().__init__(
            args=QueryArgProfilesItems.Args(
                profile_id=profile_id,
                query_arg=query_arg,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        profile_id: str | core.StringOut = core.arg()

        query_arg: str | core.StringOut = core.arg()


@core.schema
class QueryArgProfiles(core.Schema):

    items: list[QueryArgProfilesItems] | core.ArrayOut[QueryArgProfilesItems] | None = core.attr(
        QueryArgProfilesItems, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[QueryArgProfilesItems] | core.ArrayOut[QueryArgProfilesItems] | None = None,
    ):
        super().__init__(
            args=QueryArgProfiles.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[QueryArgProfilesItems] | core.ArrayOut[QueryArgProfilesItems] | None = core.arg(
            default=None
        )


@core.schema
class QueryArgProfileConfig(core.Schema):

    forward_when_query_arg_profile_is_unknown: bool | core.BoolOut = core.attr(bool)

    query_arg_profiles: QueryArgProfiles | None = core.attr(QueryArgProfiles, default=None)

    def __init__(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: bool | core.BoolOut,
        query_arg_profiles: QueryArgProfiles | None = None,
    ):
        super().__init__(
            args=QueryArgProfileConfig.Args(
                forward_when_query_arg_profile_is_unknown=forward_when_query_arg_profile_is_unknown,
                query_arg_profiles=query_arg_profiles,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        forward_when_query_arg_profile_is_unknown: bool | core.BoolOut = core.arg()

        query_arg_profiles: QueryArgProfiles | None = core.arg(default=None)


@core.schema
class ContentTypeProfilesItems(core.Schema):

    content_type: str | core.StringOut = core.attr(str)

    format: str | core.StringOut = core.attr(str)

    profile_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        content_type: str | core.StringOut,
        format: str | core.StringOut,
        profile_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ContentTypeProfilesItems.Args(
                content_type=content_type,
                format=format,
                profile_id=profile_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type: str | core.StringOut = core.arg()

        format: str | core.StringOut = core.arg()

        profile_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ContentTypeProfiles(core.Schema):

    items: list[ContentTypeProfilesItems] | core.ArrayOut[ContentTypeProfilesItems] = core.attr(
        ContentTypeProfilesItems, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[ContentTypeProfilesItems] | core.ArrayOut[ContentTypeProfilesItems],
    ):
        super().__init__(
            args=ContentTypeProfiles.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[ContentTypeProfilesItems] | core.ArrayOut[ContentTypeProfilesItems] = core.arg()


@core.schema
class ContentTypeProfileConfig(core.Schema):

    content_type_profiles: ContentTypeProfiles = core.attr(ContentTypeProfiles)

    forward_when_content_type_is_unknown: bool | core.BoolOut = core.attr(bool)

    def __init__(
        self,
        *,
        content_type_profiles: ContentTypeProfiles,
        forward_when_content_type_is_unknown: bool | core.BoolOut,
    ):
        super().__init__(
            args=ContentTypeProfileConfig.Args(
                content_type_profiles=content_type_profiles,
                forward_when_content_type_is_unknown=forward_when_content_type_is_unknown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content_type_profiles: ContentTypeProfiles = core.arg()

        forward_when_content_type_is_unknown: bool | core.BoolOut = core.arg()


@core.resource(type="aws_cloudfront_field_level_encryption_config", namespace="cloudfront")
class FieldLevelEncryptionConfig(core.Resource):
    """
    Internal value used by CloudFront to allow future updates to the Field Level Encryption Config.
    """

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An optional comment about the Field Level Encryption Config.
    """
    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) [Content Type Profile Config](#content-type-profile-config) specifies when to forward con
    tent if a content type isn't recognized and profiles to use as by default in a request if a query ar
    gument doesn't specify a profile to use.
    """
    content_type_profile_config: ContentTypeProfileConfig = core.attr(ContentTypeProfileConfig)

    """
    The current version of the Field Level Encryption Config. For example: `E2QWRUHAPOMQZL`.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the Field Level Encryption Config. For example: `K3D5EWEUDCCXON`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) [Query Arg Profile Config](#query-arg-profile-config) that specifies when to forward cont
    ent if a profile isn't found and the profile that can be provided as a query argument in a request.
    """
    query_arg_profile_config: QueryArgProfileConfig = core.attr(QueryArgProfileConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        content_type_profile_config: ContentTypeProfileConfig,
        query_arg_profile_config: QueryArgProfileConfig,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FieldLevelEncryptionConfig.Args(
                content_type_profile_config=content_type_profile_config,
                query_arg_profile_config=query_arg_profile_config,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        content_type_profile_config: ContentTypeProfileConfig = core.arg()

        query_arg_profile_config: QueryArgProfileConfig = core.arg()
