import terrascript.core as core


@core.schema
class IncludeMap(core.Schema):

    account: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: list[str] | core.ArrayOut[core.StringOut] | None = None,
        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=IncludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ExcludeMap(core.Schema):

    account: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        account: list[str] | core.ArrayOut[core.StringOut] | None = None,
        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ExcludeMap.Args(
                account=account,
                orgunit=orgunit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        orgunit: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class SecurityServicePolicyData(core.Schema):

    managed_service_data: str | core.StringOut | None = core.attr(str, default=None)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        type: str | core.StringOut,
        managed_service_data: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=SecurityServicePolicyData.Args(
                type=type,
                managed_service_data=managed_service_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        managed_service_data: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.resource(type="aws_fms_policy", namespace="fms")
class Policy(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If true, the request will also perform a clean-up process. Defaults to `true`. More infor
    mation can be found here [AWS Firewall Manager delete policy](https://docs.aws.amazon.com/fms/2018-0
    1-01/APIReference/API_DeletePolicy.html)
    """
    delete_all_policy_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) If true, Firewall Manager will automatically remove protections from resources that leave
    the policy scope. Defaults to `false`. More information can be found here [AWS Firewall Manager pol
    icy contents](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html)
    """
    delete_unused_fm_managed_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of lists of accounts and OU's to exclude from the policy.
    """
    exclude_map: ExcludeMap | None = core.attr(ExcludeMap, default=None)

    """
    (Required, Forces new resource) A boolean value, if true the tags that are specified in the `resourc
    e_tags` are not protected by this policy. If set to false and resource_tags are populated, resources
    that contain tags will be protected by this policy.
    """
    exclude_resource_tags: bool | core.BoolOut = core.attr(bool)

    """
    The AWS account ID of the AWS Firewall Manager administrator account.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) A map of lists of accounts and OU's to include in the policy.
    """
    include_map: IncludeMap | None = core.attr(IncludeMap, default=None)

    """
    (Required, Forces new resource) The friendly name of the AWS Firewall Manager Policy.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A unique identifier for each update to the policy.
    """
    policy_update_token: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) A boolean value, indicates if the policy should automatically applied to resources that a
    lready exist in the account.
    """
    remediation_enabled: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) A map of resource tags, that if present will filter protections on resources based on the
    exclude_resource_tags.
    """
    resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A resource type to protect. Conflicts with `resource_type_list`. See the [FMS API Referen
    ce](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html#fms-Type-Policy-Resource
    Type) for more information about supported values.
    """
    resource_type: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) A list of resource types to protect. Conflicts with `resource_type`. See the [FMS API Ref
    erence](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html#fms-Type-Policy-Reso
    urceType) for more information about supported values. Lists with only one element are not supported
    , instead use `resource_type`.
    """
    resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Required) The objects to include in Security Service Policy Data. Documented below.
    """
    security_service_policy_data: SecurityServicePolicyData = core.attr(SecurityServicePolicyData)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
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
        exclude_resource_tags: bool | core.BoolOut,
        name: str | core.StringOut,
        security_service_policy_data: SecurityServicePolicyData,
        delete_all_policy_resources: bool | core.BoolOut | None = None,
        delete_unused_fm_managed_resources: bool | core.BoolOut | None = None,
        exclude_map: ExcludeMap | None = None,
        include_map: IncludeMap | None = None,
        remediation_enabled: bool | core.BoolOut | None = None,
        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        resource_type: str | core.StringOut | None = None,
        resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                exclude_resource_tags=exclude_resource_tags,
                name=name,
                security_service_policy_data=security_service_policy_data,
                delete_all_policy_resources=delete_all_policy_resources,
                delete_unused_fm_managed_resources=delete_unused_fm_managed_resources,
                exclude_map=exclude_map,
                include_map=include_map,
                remediation_enabled=remediation_enabled,
                resource_tags=resource_tags,
                resource_type=resource_type,
                resource_type_list=resource_type_list,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_all_policy_resources: bool | core.BoolOut | None = core.arg(default=None)

        delete_unused_fm_managed_resources: bool | core.BoolOut | None = core.arg(default=None)

        exclude_map: ExcludeMap | None = core.arg(default=None)

        exclude_resource_tags: bool | core.BoolOut = core.arg()

        include_map: IncludeMap | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        remediation_enabled: bool | core.BoolOut | None = core.arg(default=None)

        resource_tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        resource_type: str | core.StringOut | None = core.arg(default=None)

        resource_type_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        security_service_policy_data: SecurityServicePolicyData = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
