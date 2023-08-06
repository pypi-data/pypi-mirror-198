import terrascript.core as core


@core.resource(type="aws_iot_thing_group_membership", namespace="iot")
class ThingGroupMembership(core.Resource):
    """
    The membership ID.
    """

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Override dynamic thing groups with static thing groups when 10-group limit is reached. If
    a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, addin
    g a thing to a static group removes the thing from the last dynamic group.
    """
    override_dynamic_group: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Required) The name of the group to which you are adding a thing.
    """
    thing_group_name: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the thing to add to a group.
    """
    thing_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        thing_group_name: str | core.StringOut,
        thing_name: str | core.StringOut,
        override_dynamic_group: bool | core.BoolOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingGroupMembership.Args(
                thing_group_name=thing_group_name,
                thing_name=thing_name,
                override_dynamic_group=override_dynamic_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        override_dynamic_group: bool | core.BoolOut | None = core.arg(default=None)

        thing_group_name: str | core.StringOut = core.arg()

        thing_name: str | core.StringOut = core.arg()
