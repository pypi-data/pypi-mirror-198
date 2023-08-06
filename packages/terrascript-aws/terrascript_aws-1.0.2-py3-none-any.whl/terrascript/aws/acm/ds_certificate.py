import terrascript.core as core


@core.data(type="aws_acm_certificate", namespace="aws_acm")
class DsCertificate(core.Data):

    arn: str | core.StringOut = core.attr(str, computed=True)

    certificate: str | core.StringOut = core.attr(str, computed=True)

    certificate_chain: str | core.StringOut = core.attr(str, computed=True)

    domain: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    key_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    status: str | core.StringOut = core.attr(str, computed=True)

    statuses: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain: str | core.StringOut,
        key_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        most_recent: bool | core.BoolOut | None = None,
        statuses: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        types: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificate.Args(
                domain=domain,
                key_types=key_types,
                most_recent=most_recent,
                statuses=statuses,
                tags=tags,
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: str | core.StringOut = core.arg()

        key_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        statuses: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)
