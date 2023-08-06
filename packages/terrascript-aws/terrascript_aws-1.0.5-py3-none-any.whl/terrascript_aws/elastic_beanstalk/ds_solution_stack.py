import terrascript.core as core


@core.data(type="aws_elastic_beanstalk_solution_stack", namespace="elastic_beanstalk")
class DsSolutionStack(core.Data):

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) If more than one result is returned, use the most
    """
    most_recent: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    The name of the solution stack.
    """
    name: str | core.StringOut = core.attr(str, computed=True)

    """
    A regex string to apply to the solution stack list returned
    """
    name_regex: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name_regex: str | core.StringOut,
        most_recent: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSolutionStack.Args(
                name_regex=name_regex,
                most_recent=most_recent,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        most_recent: bool | core.BoolOut | None = core.arg(default=None)

        name_regex: str | core.StringOut = core.arg()
