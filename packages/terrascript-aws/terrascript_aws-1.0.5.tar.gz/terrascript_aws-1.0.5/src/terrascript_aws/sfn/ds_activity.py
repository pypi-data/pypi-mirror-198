import terrascript.core as core


@core.data(type="aws_sfn_activity", namespace="sfn")
class DsActivity(core.Data):
    """
    (Optional) The Amazon Resource Name (ARN) that identifies the activity.
    """

    arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The date the activity was created.
    """
    creation_date: str | core.StringOut = core.attr(str, computed=True)

    """
    The Amazon Resource Name (ARN) that identifies the activity.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The name that identifies the activity.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsActivity.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut | None = core.arg(default=None)
