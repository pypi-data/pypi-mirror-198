import terrascript.core as core


@core.schema
class Tag(core.Schema):

    key: str | core.StringOut = core.attr(str)

    propagate_at_launch: bool | core.BoolOut = core.attr(bool)

    value: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        key: str | core.StringOut,
        propagate_at_launch: bool | core.BoolOut,
        value: str | core.StringOut,
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                propagate_at_launch=propagate_at_launch,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut = core.arg()

        propagate_at_launch: bool | core.BoolOut = core.arg()

        value: str | core.StringOut = core.arg()


@core.resource(type="aws_autoscaling_group_tag", namespace="aws_autoscaling")
class GroupTag(core.Resource):

    autoscaling_group_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    tag: Tag = core.attr(Tag)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: str | core.StringOut,
        tag: Tag,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupTag.Args(
                autoscaling_group_name=autoscaling_group_name,
                tag=tag,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: str | core.StringOut = core.arg()

        tag: Tag = core.arg()
