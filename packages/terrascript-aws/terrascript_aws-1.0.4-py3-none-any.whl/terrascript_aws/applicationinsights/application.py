import terrascript.core as core


@core.resource(type="aws_applicationinsights_application", namespace="applicationinsights")
class Application(core.Resource):
    """
    Amazon Resource Name (ARN) of the Application.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional)  Indicates whether Application Insights automatically configures unmonitored resources in
    the resource group.
    """
    auto_config_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Configures all of the resources in the resource group by applying the recommended configu
    rations.
    """
    auto_create: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional)  Indicates whether Application Insights can listen to CloudWatch events for the applicati
    on resources, such as instance terminated, failed deployment, and others.
    """
    cwe_monitor_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Application Insights can create applications based on a resource group or on an account.
    To create an account-based application using all of the resources in the account, set this parameter
    to `ACCOUNT_BASED`.
    """
    grouping_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    The name of the resource group.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) When set to `true`, creates opsItems for any problems detected on an application.
    """
    ops_center_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The SNS topic provided to Application Insights that is associated to the created opsItem.
    Allows you to receive notifications for updates to the opsItem.
    """
    ops_item_sns_topic_arn: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The name of the resource group.
    """
    resource_group_name: str | core.StringOut = core.attr(str)

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
        resource_group_name: str | core.StringOut,
        auto_config_enabled: bool | core.BoolOut | None = None,
        auto_create: bool | core.BoolOut | None = None,
        cwe_monitor_enabled: bool | core.BoolOut | None = None,
        grouping_type: str | core.StringOut | None = None,
        ops_center_enabled: bool | core.BoolOut | None = None,
        ops_item_sns_topic_arn: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                resource_group_name=resource_group_name,
                auto_config_enabled=auto_config_enabled,
                auto_create=auto_create,
                cwe_monitor_enabled=cwe_monitor_enabled,
                grouping_type=grouping_type,
                ops_center_enabled=ops_center_enabled,
                ops_item_sns_topic_arn=ops_item_sns_topic_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_config_enabled: bool | core.BoolOut | None = core.arg(default=None)

        auto_create: bool | core.BoolOut | None = core.arg(default=None)

        cwe_monitor_enabled: bool | core.BoolOut | None = core.arg(default=None)

        grouping_type: str | core.StringOut | None = core.arg(default=None)

        ops_center_enabled: bool | core.BoolOut | None = core.arg(default=None)

        ops_item_sns_topic_arn: str | core.StringOut | None = core.arg(default=None)

        resource_group_name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
