import terrascript.core as core


@core.resource(type="aws_apprunner_auto_scaling_configuration_version", namespace="apprunner")
class AutoScalingConfigurationVersion(core.Resource):
    """
    ARN of this auto scaling configuration version.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required, Forces new resource) Name of the auto scaling configuration.
    """
    auto_scaling_configuration_name: str | core.StringOut = core.attr(str)

    """
    The revision of this auto scaling configuration.
    """
    auto_scaling_configuration_revision: int | core.IntOut = core.attr(int, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    Whether the auto scaling configuration has the highest `auto_scaling_configuration_revision` among a
    ll configurations that share the same `auto_scaling_configuration_name`.
    """
    latest: bool | core.BoolOut = core.attr(bool, computed=True)

    """
    (Optional, Forces new resource) The maximal number of concurrent requests that you want an instance
    to process. When the number of concurrent requests goes over this limit, App Runner scales up your s
    ervice.
    """
    max_concurrency: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Forces new resource) The maximal number of instances that App Runner provisions for your
    service.
    """
    max_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional, Forces new resource) The minimal number of instances that App Runner provisions for your
    service.
    """
    min_size: int | core.IntOut | None = core.attr(int, default=None)

    """
    The current state of the auto scaling configuration. An INACTIVE configuration revision has been del
    eted and can't be used. It is permanently removed some time after deletion.
    """
    status: str | core.StringOut = core.attr(str, computed=True)

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
        auto_scaling_configuration_name: str | core.StringOut,
        max_concurrency: int | core.IntOut | None = None,
        max_size: int | core.IntOut | None = None,
        min_size: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=AutoScalingConfigurationVersion.Args(
                auto_scaling_configuration_name=auto_scaling_configuration_name,
                max_concurrency=max_concurrency,
                max_size=max_size,
                min_size=min_size,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_configuration_name: str | core.StringOut = core.arg()

        max_concurrency: int | core.IntOut | None = core.arg(default=None)

        max_size: int | core.IntOut | None = core.arg(default=None)

        min_size: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
