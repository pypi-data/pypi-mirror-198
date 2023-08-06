import terrascript.core as core


@core.resource(type="aws_cloudwatch_dashboard", namespace="cloudwatch")
class Dashboard(core.Resource):
    """
    The Amazon Resource Name (ARN) of the dashboard.
    """

    dashboard_arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The detailed information about the dashboard, including what widgets are included and the
    ir location on the dashboard. You can read more about the body structure in the [documentation](http
    s://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.htm
    l).
    """
    dashboard_body: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the dashboard.
    """
    dashboard_name: str | core.StringOut = core.attr(str)

    id: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        dashboard_body: str | core.StringOut,
        dashboard_name: str | core.StringOut,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Dashboard.Args(
                dashboard_body=dashboard_body,
                dashboard_name=dashboard_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        dashboard_body: str | core.StringOut = core.arg()

        dashboard_name: str | core.StringOut = core.arg()
