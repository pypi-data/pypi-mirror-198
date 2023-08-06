import terrascript.core as core


@core.schema
class InputParameter(core.Schema):

    name: str | core.StringOut | None = core.attr(str, default=None)

    value: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=InputParameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class Scope(core.Schema):

    compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=Scope.Args(
                compliance_resource_ids=compliance_resource_ids,
                compliance_resource_types=compliance_resource_types,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compliance_resource_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        compliance_resource_types: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Control(core.Schema):

    input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.attr(
        InputParameter, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    scope: Scope | None = core.attr(Scope, default=None)

    def __init__(
        self,
        *,
        name: str | core.StringOut,
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = None,
        scope: Scope | None = None,
    ):
        super().__init__(
            args=Control.Args(
                name=name,
                input_parameter=input_parameter,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_parameter: list[InputParameter] | core.ArrayOut[InputParameter] | None = core.arg(
            default=None
        )

        name: str | core.StringOut = core.arg()

        scope: Scope | None = core.arg(default=None)


@core.resource(type="aws_backup_framework", namespace="backup")
class Framework(core.Resource):
    """
    The ARN of the backup framework.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) One or more control blocks that make up the framework. Each control in the list has a nam
    e, input parameters, and scope. Detailed below.
    """
    control: list[Control] | core.ArrayOut[Control] = core.attr(Control, kind=core.Kind.array)

    """
    The date and time that a framework is created, in Unix format and Coordinated Universal Time (UTC).
    """
    creation_time: str | core.StringOut = core.attr(str, computed=True)

    """
    The deployment status of a framework. The statuses are: `CREATE_IN_PROGRESS` | `UPDATE_IN_PROGRESS`
    | `DELETE_IN_PROGRESS` | `COMPLETED` | `FAILED`.
    """
    deployment_status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The description of the framework with a maximum of 1,024 characters
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The id of the backup framework.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The unique name of the framework. The name must be between 1 and 256 characters, starting
    with a letter, and consisting of letters, numbers, and underscores.
    """
    name: str | core.StringOut = core.attr(str)

    """
    A framework consists of one or more controls. Each control governs a resource, such as backup plans,
    backup selections, backup vaults, or recovery points. You can also turn AWS Config recording on or
    off for each resource. For more information refer to the [AWS documentation for Framework Status](ht
    tps://docs.aws.amazon.com/aws-backup/latest/devguide/API_DescribeFramework.html#Backup-DescribeFrame
    work-response-FrameworkStatus)
    """
    status: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Metadata that you can assign to help organize the frameworks you create. If configured wi
    th a provider [`default_tags` configuration block](https://registry.terraform.io/providers/hashicorp
    /aws/latest/docs#default_tags-configuration-block) present, tags with matching keys will overwrite t
    hose defined at the provider-level.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        control: list[Control] | core.ArrayOut[Control],
        name: str | core.StringOut,
        description: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Framework.Args(
                control=control,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        control: list[Control] | core.ArrayOut[Control] = core.arg()

        description: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
