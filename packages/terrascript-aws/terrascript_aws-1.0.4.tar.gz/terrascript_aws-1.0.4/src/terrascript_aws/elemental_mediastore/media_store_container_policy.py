import terrascript.core as core


@core.resource(type="aws_media_store_container_policy", namespace="elemental_mediastore")
class MediaStoreContainerPolicy(core.Resource):
    """
    (Required) The name of the container.
    """

    container_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The contents of the policy. For more information about building AWS IAM policy documents
    with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/ia
    m-policy).
    """
    policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        container_name: str | core.StringOut,
        policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaStoreContainerPolicy.Args(
                container_name=container_name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_name: str | core.StringOut = core.arg()

        policy: str | core.StringOut = core.arg()
