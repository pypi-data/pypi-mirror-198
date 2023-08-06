import terrascript.core as core


@core.schema
class TagFilter(core.Schema):

    key: str | core.StringOut = core.attr(str)

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=TagFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ComplianceDetails(core.Schema):

    compliance_status: bool | core.BoolOut = core.attr(bool, computed=True)

    keys_with_noncompliant_values: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    non_compliant_keys: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        compliance_status: bool | core.BoolOut,
        keys_with_noncompliant_values: list[str] | core.ArrayOut[core.StringOut],
        non_compliant_keys: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=ComplianceDetails.Args(
                compliance_status=compliance_status,
                keys_with_noncompliant_values=keys_with_noncompliant_values,
                non_compliant_keys=non_compliant_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_status: bool | core.BoolOut = core.arg()

        keys_with_noncompliant_values: list[str] | core.ArrayOut[core.StringOut] = core.arg()

        non_compliant_keys: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class ResourceTagMappingList(core.Schema):

    compliance_details: list[ComplianceDetails] | core.ArrayOut[ComplianceDetails] = core.attr(
        ComplianceDetails, computed=True, kind=core.Kind.array
    )

    resource_arn: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_details: list[ComplianceDetails] | core.ArrayOut[ComplianceDetails],
        resource_arn: str | core.StringOut,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=ResourceTagMappingList.Args(
                compliance_details=compliance_details,
                resource_arn=resource_arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_details: list[ComplianceDetails] | core.ArrayOut[ComplianceDetails] = core.arg()

        resource_arn: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.data(type="aws_resourcegroupstaggingapi_resources", namespace="resourcegroupstagging")
class DsApiResources(core.Data):
    """
    (Optional) Specifies whether to exclude resources that are compliant with the tag policy. You can us
    e this parameter only if the `include_compliance_details` argument is also set to `true`.
    """

    exclude_compliant_resources: bool | core.BoolOut | None = core.attr(bool, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether to include details regarding the compliance with the effective tag poli
    cy.
    """
    include_compliance_details: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) Specifies a list of ARNs of resources for which you want to retrieve tag data. Conflicts
    with `filter`.
    """
    resource_arn_list: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    List of objects matching the search criteria.
    """
    resource_tag_mapping_list: list[ResourceTagMappingList] | core.ArrayOut[
        ResourceTagMappingList
    ] = core.attr(ResourceTagMappingList, computed=True, kind=core.Kind.array)

    """
    (Optional) The constraints on the resources that you want returned. The format of each resource type
    is `service:resourceType`. For example, specifying a resource type of `ec2` returns all Amazon EC2
    resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only
    EC2 instances.
    """
    resource_type_filters: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Specifies a list of Tag Filters (keys and values) to restrict the output to only those re
    sources that have the specified tag and, if included, the specified value. See [Tag Filter](#tag-fil
    ter) below. Conflicts with `resource_arn_list`.
    """
    tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = core.attr(
        TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        exclude_compliant_resources: bool | core.BoolOut | None = None,
        include_compliance_details: bool | core.BoolOut | None = None,
        resource_arn_list: list[str] | core.ArrayOut[core.StringOut] | None = None,
        resource_type_filters: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsApiResources.Args(
                exclude_compliant_resources=exclude_compliant_resources,
                include_compliance_details=include_compliance_details,
                resource_arn_list=resource_arn_list,
                resource_type_filters=resource_type_filters,
                tag_filter=tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_compliant_resources: bool | core.BoolOut | None = core.arg(default=None)

        include_compliance_details: bool | core.BoolOut | None = core.arg(default=None)

        resource_arn_list: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        resource_type_filters: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tag_filter: list[TagFilter] | core.ArrayOut[TagFilter] | None = core.arg(default=None)
