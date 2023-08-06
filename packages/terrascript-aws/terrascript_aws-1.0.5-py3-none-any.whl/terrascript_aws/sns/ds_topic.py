import terrascript.core as core


@core.data(type="aws_sns_topic", namespace="sns")
class DsTopic(core.Data):
    """
    Amazon Resource Name (ARN) of the found topic, suitable for referencing in other resources that supp
    ort SNS topics.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    Amazon Resource Name (ARN) of the found topic, suitable for referencing in other resources that supp
    ort SNS topics.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The friendly name of the topic to match.
    """
    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsTopic.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
