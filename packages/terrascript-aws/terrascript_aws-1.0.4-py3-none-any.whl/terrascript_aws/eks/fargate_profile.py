import terrascript.core as core


@core.schema
class Selector(core.Schema):

    labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    namespace: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        namespace: str | core.StringOut,
        labels: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Selector.Args(
                namespace=namespace,
                labels=labels,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        labels: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        namespace: str | core.StringOut = core.arg()


@core.resource(type="aws_eks_fargate_profile", namespace="eks")
class FargateProfile(core.Resource):
    """
    Amazon Resource Name (ARN) of the EKS Fargate Profile.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    cluster_name: str | core.StringOut = core.attr(str)

    fargate_profile_name: str | core.StringOut = core.attr(str)

    """
    EKS Cluster name and EKS Fargate Profile name separated by a colon (`:`).
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    pod_execution_role_arn: str | core.StringOut = core.attr(str)

    """
    (Required) Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Pro
    file. Detailed below.
    """
    selector: list[Selector] | core.ArrayOut[Selector] = core.attr(Selector, kind=core.Kind.array)

    """
    Status of the EKS Fargate Profile.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
        cluster_name: str | core.StringOut,
        fargate_profile_name: str | core.StringOut,
        pod_execution_role_arn: str | core.StringOut,
        selector: list[Selector] | core.ArrayOut[Selector],
        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=FargateProfile.Args(
                cluster_name=cluster_name,
                fargate_profile_name=fargate_profile_name,
                pod_execution_role_arn=pod_execution_role_arn,
                selector=selector,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_name: str | core.StringOut = core.arg()

        fargate_profile_name: str | core.StringOut = core.arg()

        pod_execution_role_arn: str | core.StringOut = core.arg()

        selector: list[Selector] | core.ArrayOut[Selector] = core.arg()

        subnet_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
