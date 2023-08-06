import terrascript.core as core


@core.schema
class ClientPolicyTlsValidationTrustFile(core.Schema):

    certificate_chain: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        certificate_chain: str | core.StringOut,
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrustFile.Args(
                certificate_chain=certificate_chain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_chain: str | core.StringOut = core.arg()


@core.schema
class Sds(core.Schema):

    secret_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        secret_name: str | core.StringOut,
    ):
        super().__init__(
            args=Sds.Args(
                secret_name=secret_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        secret_name: str | core.StringOut = core.arg()


@core.schema
class ClientPolicyTlsValidationTrustAcm(core.Schema):

    certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrustAcm.Args(
                certificate_authority_arns=certificate_authority_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_authority_arns: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ClientPolicyTlsValidationTrust(core.Schema):

    acm: ClientPolicyTlsValidationTrustAcm | None = core.attr(
        ClientPolicyTlsValidationTrustAcm, default=None
    )

    file: ClientPolicyTlsValidationTrustFile | None = core.attr(
        ClientPolicyTlsValidationTrustFile, default=None
    )

    sds: Sds | None = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        acm: ClientPolicyTlsValidationTrustAcm | None = None,
        file: ClientPolicyTlsValidationTrustFile | None = None,
        sds: Sds | None = None,
    ):
        super().__init__(
            args=ClientPolicyTlsValidationTrust.Args(
                acm=acm,
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm: ClientPolicyTlsValidationTrustAcm | None = core.arg(default=None)

        file: ClientPolicyTlsValidationTrustFile | None = core.arg(default=None)

        sds: Sds | None = core.arg(default=None)


@core.schema
class Match(core.Schema):

    exact: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        exact: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=Match.Args(
                exact=exact,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exact: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class SubjectAlternativeNames(core.Schema):

    match: Match = core.attr(Match)

    def __init__(
        self,
        *,
        match: Match,
    ):
        super().__init__(
            args=SubjectAlternativeNames.Args(
                match=match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        match: Match = core.arg()


@core.schema
class ClientPolicyTlsValidation(core.Schema):

    subject_alternative_names: SubjectAlternativeNames | None = core.attr(
        SubjectAlternativeNames, default=None
    )

    trust: ClientPolicyTlsValidationTrust = core.attr(ClientPolicyTlsValidationTrust)

    def __init__(
        self,
        *,
        trust: ClientPolicyTlsValidationTrust,
        subject_alternative_names: SubjectAlternativeNames | None = None,
    ):
        super().__init__(
            args=ClientPolicyTlsValidation.Args(
                trust=trust,
                subject_alternative_names=subject_alternative_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subject_alternative_names: SubjectAlternativeNames | None = core.arg(default=None)

        trust: ClientPolicyTlsValidationTrust = core.arg()


@core.schema
class ClientPolicyTlsCertificateFile(core.Schema):

    certificate_chain: str | core.StringOut = core.attr(str)

    private_key: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        certificate_chain: str | core.StringOut,
        private_key: str | core.StringOut,
    ):
        super().__init__(
            args=ClientPolicyTlsCertificateFile.Args(
                certificate_chain=certificate_chain,
                private_key=private_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_chain: str | core.StringOut = core.arg()

        private_key: str | core.StringOut = core.arg()


@core.schema
class ClientPolicyTlsCertificate(core.Schema):

    file: ClientPolicyTlsCertificateFile | None = core.attr(
        ClientPolicyTlsCertificateFile, default=None
    )

    sds: Sds | None = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        file: ClientPolicyTlsCertificateFile | None = None,
        sds: Sds | None = None,
    ):
        super().__init__(
            args=ClientPolicyTlsCertificate.Args(
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: ClientPolicyTlsCertificateFile | None = core.arg(default=None)

        sds: Sds | None = core.arg(default=None)


@core.schema
class ClientPolicyTls(core.Schema):

    certificate: ClientPolicyTlsCertificate | None = core.attr(
        ClientPolicyTlsCertificate, default=None
    )

    enforce: bool | core.BoolOut | None = core.attr(bool, default=None)

    ports: list[int] | core.ArrayOut[core.IntOut] | None = core.attr(
        int, default=None, kind=core.Kind.array
    )

    validation: ClientPolicyTlsValidation = core.attr(ClientPolicyTlsValidation)

    def __init__(
        self,
        *,
        validation: ClientPolicyTlsValidation,
        certificate: ClientPolicyTlsCertificate | None = None,
        enforce: bool | core.BoolOut | None = None,
        ports: list[int] | core.ArrayOut[core.IntOut] | None = None,
    ):
        super().__init__(
            args=ClientPolicyTls.Args(
                validation=validation,
                certificate=certificate,
                enforce=enforce,
                ports=ports,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: ClientPolicyTlsCertificate | None = core.arg(default=None)

        enforce: bool | core.BoolOut | None = core.arg(default=None)

        ports: list[int] | core.ArrayOut[core.IntOut] | None = core.arg(default=None)

        validation: ClientPolicyTlsValidation = core.arg()


@core.schema
class ClientPolicy(core.Schema):

    tls: ClientPolicyTls | None = core.attr(ClientPolicyTls, default=None)

    def __init__(
        self,
        *,
        tls: ClientPolicyTls | None = None,
    ):
        super().__init__(
            args=ClientPolicy.Args(
                tls=tls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tls: ClientPolicyTls | None = core.arg(default=None)


@core.schema
class BackendDefaults(core.Schema):

    client_policy: ClientPolicy | None = core.attr(ClientPolicy, default=None)

    def __init__(
        self,
        *,
        client_policy: ClientPolicy | None = None,
    ):
        super().__init__(
            args=BackendDefaults.Args(
                client_policy=client_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_policy: ClientPolicy | None = core.arg(default=None)


@core.schema
class ListenerTlsCertificateAcm(core.Schema):

    certificate_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        certificate_arn: str | core.StringOut,
    ):
        super().__init__(
            args=ListenerTlsCertificateAcm.Args(
                certificate_arn=certificate_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_arn: str | core.StringOut = core.arg()


@core.schema
class ListenerTlsCertificate(core.Schema):

    acm: ListenerTlsCertificateAcm | None = core.attr(ListenerTlsCertificateAcm, default=None)

    file: ClientPolicyTlsCertificateFile | None = core.attr(
        ClientPolicyTlsCertificateFile, default=None
    )

    sds: Sds | None = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        acm: ListenerTlsCertificateAcm | None = None,
        file: ClientPolicyTlsCertificateFile | None = None,
        sds: Sds | None = None,
    ):
        super().__init__(
            args=ListenerTlsCertificate.Args(
                acm=acm,
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acm: ListenerTlsCertificateAcm | None = core.arg(default=None)

        file: ClientPolicyTlsCertificateFile | None = core.arg(default=None)

        sds: Sds | None = core.arg(default=None)


@core.schema
class ListenerTlsValidationTrust(core.Schema):

    file: ClientPolicyTlsValidationTrustFile | None = core.attr(
        ClientPolicyTlsValidationTrustFile, default=None
    )

    sds: Sds | None = core.attr(Sds, default=None)

    def __init__(
        self,
        *,
        file: ClientPolicyTlsValidationTrustFile | None = None,
        sds: Sds | None = None,
    ):
        super().__init__(
            args=ListenerTlsValidationTrust.Args(
                file=file,
                sds=sds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: ClientPolicyTlsValidationTrustFile | None = core.arg(default=None)

        sds: Sds | None = core.arg(default=None)


@core.schema
class ListenerTlsValidation(core.Schema):

    subject_alternative_names: SubjectAlternativeNames | None = core.attr(
        SubjectAlternativeNames, default=None
    )

    trust: ListenerTlsValidationTrust = core.attr(ListenerTlsValidationTrust)

    def __init__(
        self,
        *,
        trust: ListenerTlsValidationTrust,
        subject_alternative_names: SubjectAlternativeNames | None = None,
    ):
        super().__init__(
            args=ListenerTlsValidation.Args(
                trust=trust,
                subject_alternative_names=subject_alternative_names,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subject_alternative_names: SubjectAlternativeNames | None = core.arg(default=None)

        trust: ListenerTlsValidationTrust = core.arg()


@core.schema
class ListenerTls(core.Schema):

    certificate: ListenerTlsCertificate = core.attr(ListenerTlsCertificate)

    mode: str | core.StringOut = core.attr(str)

    validation: ListenerTlsValidation | None = core.attr(ListenerTlsValidation, default=None)

    def __init__(
        self,
        *,
        certificate: ListenerTlsCertificate,
        mode: str | core.StringOut,
        validation: ListenerTlsValidation | None = None,
    ):
        super().__init__(
            args=ListenerTls.Args(
                certificate=certificate,
                mode=mode,
                validation=validation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: ListenerTlsCertificate = core.arg()

        mode: str | core.StringOut = core.arg()

        validation: ListenerTlsValidation | None = core.arg(default=None)


@core.schema
class Grpc(core.Schema):

    max_requests: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: int | core.IntOut,
    ):
        super().__init__(
            args=Grpc.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: int | core.IntOut = core.arg()


@core.schema
class Http(core.Schema):

    max_connections: int | core.IntOut = core.attr(int)

    max_pending_requests: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_connections: int | core.IntOut,
        max_pending_requests: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Http.Args(
                max_connections=max_connections,
                max_pending_requests=max_pending_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_connections: int | core.IntOut = core.arg()

        max_pending_requests: int | core.IntOut | None = core.arg(default=None)


@core.schema
class Http2(core.Schema):

    max_requests: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        max_requests: int | core.IntOut,
    ):
        super().__init__(
            args=Http2.Args(
                max_requests=max_requests,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_requests: int | core.IntOut = core.arg()


@core.schema
class ConnectionPool(core.Schema):

    grpc: Grpc | None = core.attr(Grpc, default=None)

    http: Http | None = core.attr(Http, default=None)

    http2: Http2 | None = core.attr(Http2, default=None)

    def __init__(
        self,
        *,
        grpc: Grpc | None = None,
        http: Http | None = None,
        http2: Http2 | None = None,
    ):
        super().__init__(
            args=ConnectionPool.Args(
                grpc=grpc,
                http=http,
                http2=http2,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        grpc: Grpc | None = core.arg(default=None)

        http: Http | None = core.arg(default=None)

        http2: Http2 | None = core.arg(default=None)


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: int | core.IntOut = core.attr(int)

    interval_millis: int | core.IntOut = core.attr(int)

    path: str | core.StringOut | None = core.attr(str, default=None)

    port: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    protocol: str | core.StringOut = core.attr(str)

    timeout_millis: int | core.IntOut = core.attr(int)

    unhealthy_threshold: int | core.IntOut = core.attr(int)

    def __init__(
        self,
        *,
        healthy_threshold: int | core.IntOut,
        interval_millis: int | core.IntOut,
        protocol: str | core.StringOut,
        timeout_millis: int | core.IntOut,
        unhealthy_threshold: int | core.IntOut,
        path: str | core.StringOut | None = None,
        port: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval_millis=interval_millis,
                protocol=protocol,
                timeout_millis=timeout_millis,
                unhealthy_threshold=unhealthy_threshold,
                path=path,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: int | core.IntOut = core.arg()

        interval_millis: int | core.IntOut = core.arg()

        path: str | core.StringOut | None = core.arg(default=None)

        port: int | core.IntOut | None = core.arg(default=None)

        protocol: str | core.StringOut = core.arg()

        timeout_millis: int | core.IntOut = core.arg()

        unhealthy_threshold: int | core.IntOut = core.arg()


@core.schema
class PortMapping(core.Schema):

    port: int | core.IntOut = core.attr(int)

    protocol: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        port: int | core.IntOut,
        protocol: str | core.StringOut,
    ):
        super().__init__(
            args=PortMapping.Args(
                port=port,
                protocol=protocol,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: int | core.IntOut = core.arg()

        protocol: str | core.StringOut = core.arg()


@core.schema
class Listener(core.Schema):

    connection_pool: ConnectionPool | None = core.attr(ConnectionPool, default=None)

    health_check: HealthCheck | None = core.attr(HealthCheck, default=None)

    port_mapping: PortMapping = core.attr(PortMapping)

    tls: ListenerTls | None = core.attr(ListenerTls, default=None)

    def __init__(
        self,
        *,
        port_mapping: PortMapping,
        connection_pool: ConnectionPool | None = None,
        health_check: HealthCheck | None = None,
        tls: ListenerTls | None = None,
    ):
        super().__init__(
            args=Listener.Args(
                port_mapping=port_mapping,
                connection_pool=connection_pool,
                health_check=health_check,
                tls=tls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_pool: ConnectionPool | None = core.arg(default=None)

        health_check: HealthCheck | None = core.arg(default=None)

        port_mapping: PortMapping = core.arg()

        tls: ListenerTls | None = core.arg(default=None)


@core.schema
class AccessLogFile(core.Schema):

    path: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        path: str | core.StringOut,
    ):
        super().__init__(
            args=AccessLogFile.Args(
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: str | core.StringOut = core.arg()


@core.schema
class AccessLog(core.Schema):

    file: AccessLogFile | None = core.attr(AccessLogFile, default=None)

    def __init__(
        self,
        *,
        file: AccessLogFile | None = None,
    ):
        super().__init__(
            args=AccessLog.Args(
                file=file,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file: AccessLogFile | None = core.arg(default=None)


@core.schema
class Logging(core.Schema):

    access_log: AccessLog | None = core.attr(AccessLog, default=None)

    def __init__(
        self,
        *,
        access_log: AccessLog | None = None,
    ):
        super().__init__(
            args=Logging.Args(
                access_log=access_log,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_log: AccessLog | None = core.arg(default=None)


@core.schema
class Spec(core.Schema):

    backend_defaults: BackendDefaults | None = core.attr(BackendDefaults, default=None)

    listener: Listener = core.attr(Listener)

    logging: Logging | None = core.attr(Logging, default=None)

    def __init__(
        self,
        *,
        listener: Listener,
        backend_defaults: BackendDefaults | None = None,
        logging: Logging | None = None,
    ):
        super().__init__(
            args=Spec.Args(
                listener=listener,
                backend_defaults=backend_defaults,
                logging=logging,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        backend_defaults: BackendDefaults | None = core.arg(default=None)

        listener: Listener = core.arg()

        logging: Logging | None = core.arg(default=None)


@core.resource(type="aws_appmesh_virtual_gateway", namespace="appmesh")
class VirtualGateway(core.Resource):
    """
    The ARN of the virtual gateway.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The creation date of the virtual gateway.
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The ID of the virtual gateway.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    The last update date of the virtual gateway.
    """
    last_updated_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the service mesh in which to create the virtual gateway. Must be between 1 an
    d 255 characters in length.
    """
    mesh_name: str | core.StringOut = core.attr(str)

    """
    (Optional) The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provi
    der][1] is currently connected to.
    """
    mesh_owner: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The name to use for the virtual gateway. Must be between 1 and 255 characters in length.
    """
    name: str | core.StringOut = core.attr(str)

    """
    The resource owner's AWS account ID.
    """
    resource_owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The virtual gateway specification to apply.
    """
    spec: Spec = core.attr(Spec)

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
        mesh_name: str | core.StringOut,
        name: str | core.StringOut,
        spec: Spec,
        mesh_owner: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=VirtualGateway.Args(
                mesh_name=mesh_name,
                name=name,
                spec=spec,
                mesh_owner=mesh_owner,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        mesh_name: str | core.StringOut = core.arg()

        mesh_owner: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        spec: Spec = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
