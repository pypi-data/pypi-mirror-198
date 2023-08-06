import terrascript.core as core


@core.schema
class CustomCookbooksSource(core.Schema):

    password: str | core.StringOut | None = core.attr(str, default=None)

    revision: str | core.StringOut | None = core.attr(str, default=None)

    ssh_key: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    url: str | core.StringOut = core.attr(str)

    username: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        url: str | core.StringOut,
        password: str | core.StringOut | None = None,
        revision: str | core.StringOut | None = None,
        ssh_key: str | core.StringOut | None = None,
        username: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=CustomCookbooksSource.Args(
                type=type,
                url=url,
                password=password,
                revision=revision,
                ssh_key=ssh_key,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: str | core.StringOut | None = core.arg(default=None)

        revision: str | core.StringOut | None = core.arg(default=None)

        ssh_key: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()

        url: str | core.StringOut = core.arg()

        username: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_opsworks_stack", namespace="opsworks")
class Stack(core.Resource):
    """
    (Optional) If set to `"LATEST"`, OpsWorks will automatically install the latest version.
    """

    agent_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If `manage_berkshelf` is enabled, the version of Berkshelf to use.
    """
    berkshelf_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Color to paint next to the stack's resources in the OpsWorks console.
    """
    color: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the configuration manager to use. Defaults to "Chef".
    """
    configuration_manager_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version of the configuration manager to use. Defaults to "11.4".
    """
    configuration_manager_version: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) When `use_custom_cookbooks` is set, provide this sub-object as
    """
    custom_cookbooks_source: CustomCookbooksSource | None = core.attr(
        CustomCookbooksSource, default=None, computed=True
    )

    """
    (Optional) User defined JSON passed to "Chef". Use a "here doc" for multiline JSON.
    """
    custom_json: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the availability zone where instances will be created
    """
    default_availability_zone: str | core.StringOut | None = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) The ARN of an IAM Instance Profile that created instances
    """
    default_instance_profile_arn: str | core.StringOut = core.attr(str)

    """
    (Optional) Name of OS that will be installed on instances by default.
    """
    default_os: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the type of root device instances will have by default.
    """
    default_root_device_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Name of the SSH keypair that instances will have by default.
    """
    default_ssh_key_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Id of the subnet in which instances will be created by default. Mandatory
    """
    default_subnet_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Keyword representing the naming scheme that will be used for instance hostnames
    """
    hostname_theme: str | core.StringOut | None = core.attr(str, default=None)

    """
    The id of the stack.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Boolean value controlling whether Opsworks will run Berkshelf for this stack.
    """
    manage_berkshelf: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The name of the stack.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the region where the stack will exist.
    """
    region: str | core.StringOut = core.attr(str)

    """
    (Required) The ARN of an IAM role that the OpsWorks service will act as.
    """
    service_role_arn: str | core.StringOut = core.attr(str)

    stack_endpoint: str | core.StringOut = core.attr(str, computed=True)

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
    (Optional) Boolean value controlling whether the custom cookbook settings are
    """
    use_custom_cookbooks: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Boolean value controlling whether the standard OpsWorks
    """
    use_opsworks_security_groups: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The id of the VPC that this stack belongs to.
    """
    vpc_id: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_instance_profile_arn: str | core.StringOut,
        name: str | core.StringOut,
        region: str | core.StringOut,
        service_role_arn: str | core.StringOut,
        agent_version: str | core.StringOut | None = None,
        berkshelf_version: str | core.StringOut | None = None,
        color: str | core.StringOut | None = None,
        configuration_manager_name: str | core.StringOut | None = None,
        configuration_manager_version: str | core.StringOut | None = None,
        custom_cookbooks_source: CustomCookbooksSource | None = None,
        custom_json: str | core.StringOut | None = None,
        default_availability_zone: str | core.StringOut | None = None,
        default_os: str | core.StringOut | None = None,
        default_root_device_type: str | core.StringOut | None = None,
        default_ssh_key_name: str | core.StringOut | None = None,
        default_subnet_id: str | core.StringOut | None = None,
        hostname_theme: str | core.StringOut | None = None,
        manage_berkshelf: bool | core.BoolOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        use_custom_cookbooks: bool | core.BoolOut | None = None,
        use_opsworks_security_groups: bool | core.BoolOut | None = None,
        vpc_id: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                default_instance_profile_arn=default_instance_profile_arn,
                name=name,
                region=region,
                service_role_arn=service_role_arn,
                agent_version=agent_version,
                berkshelf_version=berkshelf_version,
                color=color,
                configuration_manager_name=configuration_manager_name,
                configuration_manager_version=configuration_manager_version,
                custom_cookbooks_source=custom_cookbooks_source,
                custom_json=custom_json,
                default_availability_zone=default_availability_zone,
                default_os=default_os,
                default_root_device_type=default_root_device_type,
                default_ssh_key_name=default_ssh_key_name,
                default_subnet_id=default_subnet_id,
                hostname_theme=hostname_theme,
                manage_berkshelf=manage_berkshelf,
                tags=tags,
                tags_all=tags_all,
                use_custom_cookbooks=use_custom_cookbooks,
                use_opsworks_security_groups=use_opsworks_security_groups,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        agent_version: str | core.StringOut | None = core.arg(default=None)

        berkshelf_version: str | core.StringOut | None = core.arg(default=None)

        color: str | core.StringOut | None = core.arg(default=None)

        configuration_manager_name: str | core.StringOut | None = core.arg(default=None)

        configuration_manager_version: str | core.StringOut | None = core.arg(default=None)

        custom_cookbooks_source: CustomCookbooksSource | None = core.arg(default=None)

        custom_json: str | core.StringOut | None = core.arg(default=None)

        default_availability_zone: str | core.StringOut | None = core.arg(default=None)

        default_instance_profile_arn: str | core.StringOut = core.arg()

        default_os: str | core.StringOut | None = core.arg(default=None)

        default_root_device_type: str | core.StringOut | None = core.arg(default=None)

        default_ssh_key_name: str | core.StringOut | None = core.arg(default=None)

        default_subnet_id: str | core.StringOut | None = core.arg(default=None)

        hostname_theme: str | core.StringOut | None = core.arg(default=None)

        manage_berkshelf: bool | core.BoolOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        region: str | core.StringOut = core.arg()

        service_role_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        use_custom_cookbooks: bool | core.BoolOut | None = core.arg(default=None)

        use_opsworks_security_groups: bool | core.BoolOut | None = core.arg(default=None)

        vpc_id: str | core.StringOut | None = core.arg(default=None)
