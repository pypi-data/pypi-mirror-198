import terrascript.core as core


@core.resource(type="aws_key_pair", namespace="aws_ec2")
class KeyPair(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    fingerprint: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key_name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key_pair_id: str | core.StringOut = core.attr(str, computed=True)

    key_type: str | core.StringOut = core.attr(str, computed=True)

    public_key: str | core.StringOut = core.attr(str)

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
        public_key: str | core.StringOut,
        key_name: str | core.StringOut | None = None,
        key_name_prefix: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=KeyPair.Args(
                public_key=public_key,
                key_name=key_name,
                key_name_prefix=key_name_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_name: str | core.StringOut | None = core.arg(default=None)

        key_name_prefix: str | core.StringOut | None = core.arg(default=None)

        public_key: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
