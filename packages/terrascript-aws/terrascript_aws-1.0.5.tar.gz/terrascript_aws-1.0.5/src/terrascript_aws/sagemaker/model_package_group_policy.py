import terrascript.core as core


@core.resource(type="aws_sagemaker_model_package_group_policy", namespace="sagemaker")
class ModelPackageGroupPolicy(core.Resource):
    """
    The name of the Model Package Package Group.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the model package group.
    """
    model_package_group_name: str | core.StringOut = core.attr(str)

    resource_policy: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        model_package_group_name: str | core.StringOut,
        resource_policy: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ModelPackageGroupPolicy.Args(
                model_package_group_name=model_package_group_name,
                resource_policy=resource_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        model_package_group_name: str | core.StringOut = core.arg()

        resource_policy: str | core.StringOut = core.arg()
