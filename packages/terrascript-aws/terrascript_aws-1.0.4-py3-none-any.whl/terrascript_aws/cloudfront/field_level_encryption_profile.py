import terrascript.core as core


@core.schema
class FieldPatterns(core.Schema):

    items: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=FieldPatterns.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Items(core.Schema):

    field_patterns: FieldPatterns = core.attr(FieldPatterns)

    provider_id: str | core.StringOut = core.attr(str)

    public_key_id: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        field_patterns: FieldPatterns,
        provider_id: str | core.StringOut,
        public_key_id: str | core.StringOut,
    ):
        super().__init__(
            args=Items.Args(
                field_patterns=field_patterns,
                provider_id=provider_id,
                public_key_id=public_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_patterns: FieldPatterns = core.arg()

        provider_id: str | core.StringOut = core.arg()

        public_key_id: str | core.StringOut = core.arg()


@core.schema
class EncryptionEntities(core.Schema):

    items: list[Items] | core.ArrayOut[Items] | None = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        items: list[Items] | core.ArrayOut[Items] | None = None,
    ):
        super().__init__(
            args=EncryptionEntities.Args(
                items=items,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        items: list[Items] | core.ArrayOut[Items] | None = core.arg(default=None)


@core.resource(type="aws_cloudfront_field_level_encryption_profile", namespace="cloudfront")
class FieldLevelEncryptionProfile(core.Resource):
    """
    Internal value used by CloudFront to allow future updates to the Field Level Encryption Profile.
    """

    caller_reference: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) An optional comment about the Field Level Encryption Profile.
    """
    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The [encryption entities](#encryption-entities) config block for field-level encryption p
    rofiles that contains an attribute `items` which includes the encryption key and field pattern speci
    fications.
    """
    encryption_entities: EncryptionEntities = core.attr(EncryptionEntities)

    """
    The current version of the Field Level Encryption Profile. For example: `E2QWRUHAPOMQZL`.
    """
    etag: str | core.StringOut = core.attr(str, computed=True)

    """
    The identifier for the Field Level Encryption Profile. For example: `K3D5EWEUDCCXON`.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the Field Level Encryption Profile.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        encryption_entities: EncryptionEntities,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FieldLevelEncryptionProfile.Args(
                encryption_entities=encryption_entities,
                name=name,
                comment=comment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        encryption_entities: EncryptionEntities = core.arg()

        name: str | core.StringOut = core.arg()
