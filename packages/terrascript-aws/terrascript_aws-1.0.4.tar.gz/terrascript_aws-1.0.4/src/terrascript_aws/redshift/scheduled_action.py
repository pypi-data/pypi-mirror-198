import terrascript.core as core


@core.schema
class ResumeCluster(core.Schema):

    cluster_identifier: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cluster_identifier: str | core.StringOut,
    ):
        super().__init__(
            args=ResumeCluster.Args(
                cluster_identifier=cluster_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: str | core.StringOut = core.arg()


@core.schema
class PauseCluster(core.Schema):

    cluster_identifier: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        cluster_identifier: str | core.StringOut,
    ):
        super().__init__(
            args=PauseCluster.Args(
                cluster_identifier=cluster_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: str | core.StringOut = core.arg()


@core.schema
class ResizeCluster(core.Schema):

    classic: bool | core.BoolOut | None = core.attr(bool, default=None)

    cluster_identifier: str | core.StringOut = core.attr(str)

    cluster_type: str | core.StringOut | None = core.attr(str, default=None)

    node_type: str | core.StringOut | None = core.attr(str, default=None)

    number_of_nodes: int | core.IntOut | None = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cluster_identifier: str | core.StringOut,
        classic: bool | core.BoolOut | None = None,
        cluster_type: str | core.StringOut | None = None,
        node_type: str | core.StringOut | None = None,
        number_of_nodes: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=ResizeCluster.Args(
                cluster_identifier=cluster_identifier,
                classic=classic,
                cluster_type=cluster_type,
                node_type=node_type,
                number_of_nodes=number_of_nodes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classic: bool | core.BoolOut | None = core.arg(default=None)

        cluster_identifier: str | core.StringOut = core.arg()

        cluster_type: str | core.StringOut | None = core.arg(default=None)

        node_type: str | core.StringOut | None = core.arg(default=None)

        number_of_nodes: int | core.IntOut | None = core.arg(default=None)


@core.schema
class TargetAction(core.Schema):

    pause_cluster: PauseCluster | None = core.attr(PauseCluster, default=None)

    resize_cluster: ResizeCluster | None = core.attr(ResizeCluster, default=None)

    resume_cluster: ResumeCluster | None = core.attr(ResumeCluster, default=None)

    def __init__(
        self,
        *,
        pause_cluster: PauseCluster | None = None,
        resize_cluster: ResizeCluster | None = None,
        resume_cluster: ResumeCluster | None = None,
    ):
        super().__init__(
            args=TargetAction.Args(
                pause_cluster=pause_cluster,
                resize_cluster=resize_cluster,
                resume_cluster=resume_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pause_cluster: PauseCluster | None = core.arg(default=None)

        resize_cluster: ResizeCluster | None = core.arg(default=None)

        resume_cluster: ResumeCluster | None = core.arg(default=None)


@core.resource(type="aws_redshift_scheduled_action", namespace="redshift")
class ScheduledAction(core.Resource):
    """
    (Optional) The description of the scheduled action.
    """

    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Whether to enable the scheduled action. Default is `true` .
    """
    enable: bool | core.BoolOut | None = core.attr(bool, default=None)

    """
    (Optional) The end time in UTC when the schedule is active, in UTC RFC3339 format(for example, YYYY-
    MM-DDTHH:MM:SSZ).
    """
    end_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The IAM role to assume to run the scheduled action.
    """
    iam_role: str | core.StringOut = core.attr(str)

    """
    The Redshift Scheduled Action name.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The scheduled action name.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Required) The schedule of action. The schedule is defined format of "at expression" or "cron expres
    sion", for example `at(2016-03-04T17:27:00)` or `cron(0 10 ? * MON *)`. See [Scheduled Action](https
    ://docs.aws.amazon.com/redshift/latest/APIReference/API_ScheduledAction.html) for more information.
    """
    schedule: str | core.StringOut = core.attr(str)

    """
    (Optional) The start time in UTC when the schedule is active, in UTC RFC3339 format(for example, YYY
    Y-MM-DDTHH:MM:SSZ).
    """
    start_time: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Target action. Documented below.
    """
    target_action: TargetAction = core.attr(TargetAction)

    def __init__(
        self,
        resource_name: str,
        *,
        iam_role: str | core.StringOut,
        name: str | core.StringOut,
        schedule: str | core.StringOut,
        target_action: TargetAction,
        description: str | core.StringOut | None = None,
        enable: bool | core.BoolOut | None = None,
        end_time: str | core.StringOut | None = None,
        start_time: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ScheduledAction.Args(
                iam_role=iam_role,
                name=name,
                schedule=schedule,
                target_action=target_action,
                description=description,
                enable=enable,
                end_time=end_time,
                start_time=start_time,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: str | core.StringOut | None = core.arg(default=None)

        enable: bool | core.BoolOut | None = core.arg(default=None)

        end_time: str | core.StringOut | None = core.arg(default=None)

        iam_role: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        schedule: str | core.StringOut = core.arg()

        start_time: str | core.StringOut | None = core.arg(default=None)

        target_action: TargetAction = core.arg()
