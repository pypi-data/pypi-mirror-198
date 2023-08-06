import terrascript.core as core


@core.schema
class PreProvisioningHook(core.Schema):

    payload_version: str | core.StringOut | None = core.attr(str, default=None)

    target_arn: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        target_arn: str | core.StringOut,
        payload_version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=PreProvisioningHook.Args(
                target_arn=target_arn,
                payload_version=payload_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        payload_version: str | core.StringOut | None = core.arg(default=None)

        target_arn: str | core.StringOut = core.arg()


@core.resource(type="aws_iot_provisioning_template", namespace="iot")
class ProvisioningTemplate(core.Resource):
    """
    The ARN that identifies the provisioning template.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    The default version of the fleet provisioning template.
    """
    default_version_id: int | core.IntOut = core.attr(int, computed=True)

    """
    (Optional) The description of the fleet provisioning template.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) True to enable the fleet provisioning template, otherwise false.
    """
    enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the fleet provisioning template.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) Creates a pre-provisioning hook template. Details below.
    """
    pre_provisioning_hook: PreProvisioningHook | None = core.attr(PreProvisioningHook, default=None)

    """
    (Required) The role ARN for the role associated with the fleet provisioning template. This IoT role
    grants permission to provision a device.
    """
    provisioning_role_arn: str | core.StringOut = core.attr(str)

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

    """
    (Required) The JSON formatted contents of the fleet provisioning template.
    """
    template_body: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        provisioning_role_arn: str | core.StringOut,
        template_body: str | core.StringOut,
        description: str | core.StringOut | None = None,
        enabled: bool | core.BoolOut | None = None,
        pre_provisioning_hook: PreProvisioningHook | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisioningTemplate.Args(
                name=name,
                provisioning_role_arn=provisioning_role_arn,
                template_body=template_body,
                description=description,
                enabled=enabled,
                pre_provisioning_hook=pre_provisioning_hook,
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

        enabled: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        pre_provisioning_hook: PreProvisioningHook | None = core.arg(default=None)

        provisioning_role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        template_body: str | core.StringOut = core.arg()
