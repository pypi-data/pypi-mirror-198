import terrascript.core as core


@core.resource(type="aws_ssm_activation", namespace="aws_ssm")
class Activation(core.Resource):

    activation_code: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut | None = core.attr(str, default=None)

    expiration_date: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    expired: bool | core.BoolOut = core.attr(bool, computed=True)

    iam_role: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut | None = core.attr(str, default=None)

    registration_count: int | core.IntOut = core.attr(int, computed=True)

    registration_limit: int | core.IntOut | None = core.attr(int, default=None)

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
        iam_role: str | core.StringOut,
        description: str | core.StringOut | None = None,
        expiration_date: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        registration_limit: int | core.IntOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Activation.Args(
                iam_role=iam_role,
                description=description,
                expiration_date=expiration_date,
                name=name,
                registration_limit=registration_limit,
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

        expiration_date: str | core.StringOut | None = core.arg(default=None)

        iam_role: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        registration_limit: int | core.IntOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
