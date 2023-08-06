import terrascript.core as core


@core.resource(type="aws_imagebuilder_component", namespace="imagebuilder")
class Component(core.Resource):
    """
    (Required) Amazon Resource Name (ARN) of the component.
    """

    arn: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Change description of the component.
    """
    change_description: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Inline YAML string with data of the component. Exactly one of `data` and `uri` can be spe
    cified. Terraform will only perform drift detection of its value when present in a configuration.
    """
    data: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    Date the component was created.
    """
    date_created: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Description of the component.
    """
    description: str | core.StringOut | None = core.attr(str, default=None)

    """
    Encryption status of the component.
    """
    encrypted: bool | core.BoolOut = core.attr(bool, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Amazon Resource Name (ARN) of the Key Management Service (KMS) Key used to encrypt the co
    mponent.
    """
    kms_key_id: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Name of the component.
    """
    name: str | core.StringOut = core.attr(str)

    """
    Owner of the component.
    """
    owner: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) Platform of the component.
    """
    platform: str | core.StringOut = core.attr(str)

    """
    (Optional) Set of Operating Systems (OS) supported by the component.
    """
    supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Key-value map of resource tags for the component. If configured with a provider [`default
    _tags` configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#defaul
    t_tags-configuration-block) present, tags with matching keys will overwrite those defined at the pro
    vider-level.
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
    Type of the component.
    """
    type: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) S3 URI with data of the component. Exactly one of `data` and `uri` can be specified.
    """
    uri: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Required) Version of the component.
    """
    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: str | core.StringOut,
        platform: str | core.StringOut,
        version: str | core.StringOut,
        change_description: str | core.StringOut | None = None,
        data: str | core.StringOut | None = None,
        description: str | core.StringOut | None = None,
        kms_key_id: str | core.StringOut | None = None,
        supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        uri: str | core.StringOut | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Component.Args(
                name=name,
                platform=platform,
                version=version,
                change_description=change_description,
                data=data,
                description=description,
                kms_key_id=kms_key_id,
                supported_os_versions=supported_os_versions,
                tags=tags,
                tags_all=tags_all,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        change_description: str | core.StringOut | None = core.arg(default=None)

        data: str | core.StringOut | None = core.arg(default=None)

        description: str | core.StringOut | None = core.arg(default=None)

        kms_key_id: str | core.StringOut | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        platform: str | core.StringOut = core.arg()

        supported_os_versions: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        uri: str | core.StringOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()
