import terrascript.core as core


@core.schema
class Idp(core.Schema):

    entity_id: str | core.StringOut = core.attr(str)

    metadata_content: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        entity_id: str | core.StringOut,
        metadata_content: str | core.StringOut,
    ):
        super().__init__(
            args=Idp.Args(
                entity_id=entity_id,
                metadata_content=metadata_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        entity_id: str | core.StringOut = core.arg()

        metadata_content: str | core.StringOut = core.arg()


@core.schema
class SamlOptions(core.Schema):

    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    idp: Idp | None = core.attr(Idp, default=None)

    master_backend_role: str | core.StringOut | None = core.attr(str, default=None)

    master_user_name: str | core.StringOut | None = core.attr(str, default=None)

    roles_key: str | core.StringOut | None = core.attr(str, default=None)

    session_timeout_minutes: int | core.IntOut | None = core.attr(int, default=None)

    subject_key: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: bool | core.BoolOut | None = None,
        idp: Idp | None = None,
        master_backend_role: str | core.StringOut | None = None,
        master_user_name: str | core.StringOut | None = None,
        roles_key: str | core.StringOut | None = None,
        session_timeout_minutes: int | core.IntOut | None = None,
        subject_key: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SamlOptions.Args(
                enabled=enabled,
                idp=idp,
                master_backend_role=master_backend_role,
                master_user_name=master_user_name,
                roles_key=roles_key,
                session_timeout_minutes=session_timeout_minutes,
                subject_key=subject_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: bool | core.BoolOut | None = core.arg(default=None)

        idp: Idp | None = core.arg(default=None)

        master_backend_role: str | core.StringOut | None = core.arg(default=None)

        master_user_name: str | core.StringOut | None = core.arg(default=None)

        roles_key: str | core.StringOut | None = core.arg(default=None)

        session_timeout_minutes: int | core.IntOut | None = core.arg(default=None)

        subject_key: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_elasticsearch_domain_saml_options", namespace="elasticsearch")
class DomainSamlOptions(core.Resource):
    """
    (Required) Name of the domain.
    """

    domain_name: str | core.StringOut = core.attr(str)

    """
    The name of the domain the SAML options are associated with.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The SAML authentication options for an AWS Elasticsearch Domain.
    """
    saml_options: SamlOptions | None = core.attr(SamlOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: str | core.StringOut,
        saml_options: SamlOptions | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainSamlOptions.Args(
                domain_name=domain_name,
                saml_options=saml_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: str | core.StringOut = core.arg()

        saml_options: SamlOptions | None = core.arg(default=None)
