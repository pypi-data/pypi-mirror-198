import terrascript.core as core


@core.data(type="aws_canonical_user_id", namespace="aws_s3")
class DsCanonicalUserId(core.Data):

    display_name: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsCanonicalUserId.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
