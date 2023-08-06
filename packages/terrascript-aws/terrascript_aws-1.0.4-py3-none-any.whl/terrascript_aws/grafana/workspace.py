import terrascript.core as core


@core.resource(type="aws_grafana_workspace", namespace="grafana")
class Workspace(core.Resource):
    """
    (Required) The type of account access for the workspace. Valid values are `CURRENT_ACCOUNT` and `ORG
    ANIZATION`. If `ORGANIZATION` is specified, then `organizational_units` must also be present.
    """

    account_access_type: str | core.StringOut = core.attr(str)

    """
    The Amazon Resource Name (ARN) of the Grafana workspace.
    """
    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The authentication providers for the workspace. Valid values are `AWS_SSO`, `SAML`, or bo
    th.
    """
    authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, kind=core.Kind.array
    )

    """
    (Optional) The data sources for the workspace. Valid values are `AMAZON_OPENSEARCH_SERVICE`, `ATHENA
    , `CLOUDWATCH`, `PROMETHEUS`, `REDSHIFT`, `SITEWISE`, `TIMESTREAM`, `XRAY`
    """
    data_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The workspace description.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The endpoint of the Grafana workspace.
    """
    endpoint: str | core.StringOut = core.attr(str, computed=True)

    """
    The version of Grafana running on the workspace.
    """
    grafana_version: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The Grafana workspace name.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The notification destinations. If a data source is specified here, Amazon Managed Grafana
    will create IAM roles and permissions needed to use these destinations. Must be set to `SNS`.
    """
    notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) The role name that the workspace uses to access resources through Amazon Organizations.
    """
    organization_role_name: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The Amazon Organizations organizational units that the workspace is authorized to use dat
    a sources from.
    """
    organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Required) The permission type of the workspace. If `SERVICE_MANAGED` is specified, the IAM roles an
    d IAM policy attachments are generated automatically. If `CUSTOMER_MANAGED` is specified, the IAM ro
    les and IAM policy attachments will not be created.
    """
    permission_type: str | core.StringOut = core.attr(str)

    """
    (Optional) The IAM role ARN that the workspace assumes.
    """
    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    saml_configuration_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The AWS CloudFormation stack set name that provisions IAM roles to be used by the workspa
    ce.
    """
    stack_set_name: str | core.StringOut | None = core.attr(str, default=None)

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
        account_access_type: str | core.StringOut,
        authentication_providers: list[str] | core.ArrayOut[core.StringOut],
        permission_type: str | core.StringOut,
        data_sources: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = None,
        organization_role_name: str | core.StringOut | None = None,
        organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = None,
        role_arn: str | core.StringOut | None = None,
        stack_set_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workspace.Args(
                account_access_type=account_access_type,
                authentication_providers=authentication_providers,
                permission_type=permission_type,
                data_sources=data_sources,
                description=description,
                name=name,
                notification_destinations=notification_destinations,
                organization_role_name=organization_role_name,
                organizational_units=organizational_units,
                role_arn=role_arn,
                stack_set_name=stack_set_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_access_type: str | core.StringOut = core.arg()

        authentication_providers: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        data_sources: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)

        notification_destinations: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        organization_role_name: str | core.StringOut | None = core.arg(default=None)

        organizational_units: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        permission_type: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut | None = core.arg(default=None)

        stack_set_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
