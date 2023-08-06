import terrascript.core as core


@core.resource(type="aws_cloud9_environment_ec2", namespace="cloud9")
class EnvironmentEc2(core.Resource):
    """
    The ARN of the environment.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The number of minutes until the running instance is shut down after the environment has l
    ast been used.
    """
    automatic_stop_time_minutes: int | core.IntOut | None = core.attr(int, default=None)

    """
    (Optional) The connection type used for connecting to an Amazon EC2 environment. Valid values are `C
    ONNECT_SSH` and `CONNECT_SSM`. For more information please refer [AWS documentation for Cloud9](http
    s://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html).
    """
    connection_type: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) The description of the environment.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    The ID of the environment.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance.
    Valid values are
    """
    image_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) The type of instance to connect to the environment, e.g., `t2.micro`.
    """
    instance_type: str | core.StringOut = core.attr(str)

    """
    (Required) The name of the environment.
    """
    name: str | core.StringOut = core.attr(str)

    """
    (Optional) The ARN of the environment owner. This can be ARN of any AWS IAM principal. Defaults to t
    he environment's creator.
    """
    owner_arn: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The ID of the subnet in Amazon VPC that AWS Cloud9 will use to communicate with the Amazo
    n EC2 instance.
    """
    subnet_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
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

    """
    The type of the environment (e.g., `ssh` or `ec2`)
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: str | core.StringOut,
        name: str | core.StringOut,
        automatic_stop_time_minutes: int | core.IntOut | None = None,
        connection_type: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        image_id: str | core.StringOut | None = None,
        owner_arn: str | core.StringOut | None = None,
        subnet_id: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=EnvironmentEc2.Args(
                instance_type=instance_type,
                name=name,
                automatic_stop_time_minutes=automatic_stop_time_minutes,
                connection_type=connection_type,
                description=description,
                image_id=image_id,
                owner_arn=owner_arn,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic_stop_time_minutes: int | core.IntOut | None = core.arg(default=None)

        connection_type: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        image_id: str | core.StringOut | None = core.arg(default=None)

        instance_type: str | core.StringOut = core.arg()

        name: str | core.StringOut = core.arg()

        owner_arn: str | core.StringOut | None = core.arg(default=None)

        subnet_id: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
