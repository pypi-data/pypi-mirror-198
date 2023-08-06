import terrascript.core as core


@core.resource(type="aws_ssoadmin_permission_set", namespace="ssoadmin")
class PermissionSet(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Permission Set.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The date the Permission Set was created in [RFC3339 format](https://tools.ietf.org/html/rfc3339#sect
    ion-5.8).
    """
    created_date: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the Permission Set.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The Amazon Resource Names (ARNs) of the Permission Set and SSO Instance, separated by a comma (`,`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) The Amazon Resource Name (ARN) of the SSO Instance under which the o
    peration will be executed.
    """
    instance_arn: str | core.StringOut = core.attr(str)

    """
    (Required, Forces new resource) The name of the Permission Set.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The relay state URL used to redirect users within the application during the federation a
    uthentication process.
    """
    relay_state: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The length of time that the application user sessions are valid in the ISO-8601 standard.
    Default: `PT1H`.
    """
    session_duration: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        instance_arn: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        relay_state: str | core.StringOut | None = None,
        session_duration: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=PermissionSet.Args(
                instance_arn=instance_arn,
                name=name,
                description=description,
                relay_state=relay_state,
                session_duration=session_duration,
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

        instance_arn: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        relay_state: str | core.StringOut | None = core.arg(default=None)

        session_duration: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
