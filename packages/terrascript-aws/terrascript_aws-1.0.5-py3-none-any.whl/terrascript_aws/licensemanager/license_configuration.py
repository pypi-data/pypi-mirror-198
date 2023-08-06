import terrascript.core as core


@core.resource(type="aws_licensemanager_license_configuration", namespace="licensemanager")
class LicenseConfiguration(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    license_count: int | core.IntOut | None = core.attr(int, default=None)

    license_count_hard_limit: bool | core.BoolOut | None = core.attr(bool, default=None)

    license_counting_type: str | core.StringOut = core.attr(str)

    license_rules: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    owner_account_id: str | core.StringOut = core.attr(str, computed=True)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        license_counting_type: str | core.StringOut,
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        license_count: int | core.IntOut | None = None,
        license_count_hard_limit: bool | core.BoolOut | None = None,
        license_rules: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=LicenseConfiguration.Args(
                license_counting_type=license_counting_type,
                name=name,
                description=description,
                license_count=license_count,
                license_count_hard_limit=license_count_hard_limit,
                license_rules=license_rules,
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

        license_count: int | core.IntOut | None = core.arg(default=None)

        license_count_hard_limit: bool | core.BoolOut | None = core.arg(default=None)

        license_counting_type: str | core.StringOut = core.arg()

        license_rules: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
