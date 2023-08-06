import terrascript.core as core


@core.schema
class Vpc(core.Schema):

    vpc_id: str | core.StringOut = core.attr(str)

    vpc_region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        vpc_id: str | core.StringOut,
        vpc_region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Vpc.Args(
                vpc_id=vpc_id,
                vpc_region=vpc_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_id: str | core.StringOut = core.arg()

        vpc_region: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_route53_zone", namespace="route53")
class Zone(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Hosted Zone.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A comment for the hosted zone. Defaults to 'Managed by Terraform'.
    """
    comment: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The ID of the reusable delegation set whose NS records you want to assign to the hosted z
    one. Conflicts with `vpc` as delegation sets can only be used for public zones.
    """
    delegation_set_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to destroy all records (possibly managed outside of Terraform) in the zone when d
    estroying the zone.
    """
    force_destroy: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) This is the name of the hosted zone.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A list of name servers in associated (or default) delegation set.
    """
    name_servers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A map of tags to assign to the zone. If configured with a provider [`default_tags` config
    uration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-config
    uration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    (Optional) Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflic
    ts with the `delegation_set_id` argument in this resource and any [`aws_route53_zone_association` re
    source](/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed b
    elow.
    """
    vpc: list[Vpc] | core.ArrayOut[Vpc] | None = core.attr(Vpc, default=None, kind=core.Kind.array)

    """
    The Hosted Zone ID. This can be referenced by zone records.
    """
    zone_id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        comment: str | core.StringOut | None = None,
        delegation_set_id: str | core.StringOut | None = None,
        force_destroy: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        vpc: list[Vpc] | core.ArrayOut[Vpc] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Zone.Args(
                name=name,
                comment=comment,
                delegation_set_id=delegation_set_id,
                force_destroy=force_destroy,
                tags=tags,
                tags_all=tags_all,
                vpc=vpc,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        comment: str | core.StringOut | None = core.arg(default=None)

        delegation_set_id: str | core.StringOut | None = core.arg(default=None)

        force_destroy: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        vpc: list[Vpc] | core.ArrayOut[Vpc] | None = core.arg(default=None)
