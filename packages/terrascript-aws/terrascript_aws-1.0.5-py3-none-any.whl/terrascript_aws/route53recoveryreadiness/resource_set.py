import terrascript.core as core


@core.schema
class NlbResource(core.Schema):

    arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=NlbResource.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)


@core.schema
class R53Resource(core.Schema):

    domain_name: str | core.StringOut | None = core.attr(str, default=None)

    record_set_id: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut | None = None,
        record_set_id: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=R53Resource.Args(
                domain_name=domain_name,
                record_set_id=record_set_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut | None = core.arg(default=None)

        record_set_id: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TargetResource(core.Schema):

    nlb_resource: NlbResource | None = core.attr(NlbResource, default=None)

    r53_resource: R53Resource | None = core.attr(R53Resource, default=None)

    def __init__(
        self,
        *,
        nlb_resource: NlbResource | None = None,
        r53_resource: R53Resource | None = None,
    ):
        super().__init__(
            args=TargetResource.Args(
                nlb_resource=nlb_resource,
                r53_resource=r53_resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        nlb_resource: NlbResource | None = core.arg(default=None)

        r53_resource: R53Resource | None = core.arg(default=None)


@core.schema
class DnsTargetResource(core.Schema):

    domain_name: str | core.StringOut = core.attr(str)

    hosted_zone_arn: str | core.StringOut | None = core.attr(str, default=None)

    record_set_id: str | core.StringOut | None = core.attr(str, default=None)

    record_type: str | core.StringOut | None = core.attr(str, default=None)

    target_resource: TargetResource | None = core.attr(TargetResource, default=None)

    def __init__(
        self,
        *,
        domain_name: str | core.StringOut,
        hosted_zone_arn: str | core.StringOut | None = None,
        record_set_id: str | core.StringOut | None = None,
        record_type: str | core.StringOut | None = None,
        target_resource: TargetResource | None = None,
    ):
        super().__init__(
            args=DnsTargetResource.Args(
                domain_name=domain_name,
                hosted_zone_arn=hosted_zone_arn,
                record_set_id=record_set_id,
                record_type=record_type,
                target_resource=target_resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: str | core.StringOut = core.arg()

        hosted_zone_arn: str | core.StringOut | None = core.arg(default=None)

        record_set_id: str | core.StringOut | None = core.arg(default=None)

        record_type: str | core.StringOut | None = core.arg(default=None)

        target_resource: TargetResource | None = core.arg(default=None)


@core.schema
class Resources(core.Schema):

    component_id: str | core.StringOut = core.attr(str, computed=True)

    dns_target_resource: DnsTargetResource | None = core.attr(DnsTargetResource, default=None)

    readiness_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    resource_arn: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        component_id: str | core.StringOut,
        dns_target_resource: DnsTargetResource | None = None,
        readiness_scopes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_arn: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Resources.Args(
                component_id=component_id,
                dns_target_resource=dns_target_resource,
                readiness_scopes=readiness_scopes,
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_id: str | core.StringOut = core.arg()

        dns_target_resource: DnsTargetResource | None = core.arg(default=None)

        readiness_scopes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        resource_arn: str | core.StringOut | None = core.arg(default=None)


@core.resource(
    type="aws_route53recoveryreadiness_resource_set", namespace="route53recoveryreadiness"
)
class ResourceSet(core.Resource):
    """
    (Required) NLB resource ARN.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Unique name describing the resource set.
    """
    resource_set_name: str | core.StringOut = core.attr(str)

    """
    (Required) Type of the resources in the resource set.
    """
    resource_set_type: str | core.StringOut = core.attr(str)

    """
    (Required) List of resources to add to this resource set. See below.
    """
    resources: list[Resources] | core.ArrayOut[Resources] = core.attr(
        Resources, kind=core.Kind.array
    )

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        resource_set_name: str | core.StringOut,
        resource_set_type: str | core.StringOut,
        resources: list[Resources] | core.ArrayOut[Resources],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceSet.Args(
                resource_set_name=resource_set_name,
                resource_set_type=resource_set_type,
                resources=resources,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_set_name: str | core.StringOut = core.arg()

        resource_set_type: str | core.StringOut = core.arg()

        resources: list[Resources] | core.ArrayOut[Resources] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
