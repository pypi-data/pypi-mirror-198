import terrascript.core as core


@core.schema
class EncryptionKey(core.Schema):

    id: str | core.StringOut = core.attr(str)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        id: str | core.StringOut,
        type: str | core.StringOut,
    ):
        super().__init__(
            args=EncryptionKey.Args(
                id=id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: str | core.StringOut = core.arg()

        type: str | core.StringOut = core.arg()


@core.schema
class ArtifactStore(core.Schema):

    encryption_key: EncryptionKey | None = core.attr(EncryptionKey, default=None)

    location: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    type: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        location: str | core.StringOut,
        type: str | core.StringOut,
        encryption_key: EncryptionKey | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ArtifactStore.Args(
                location=location,
                type=type,
                encryption_key=encryption_key,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_key: EncryptionKey | None = core.arg(default=None)

        location: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)

        type: str | core.StringOut = core.arg()


@core.schema
class Action(core.Schema):

    category: str | core.StringOut = core.attr(str)

    configuration: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    input_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: str | core.StringOut = core.attr(str)

    namespace: str | core.StringOut | None = core.attr(str, default=None)

    output_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    owner: str | core.StringOut = core.attr(str)

    provider: str | core.StringOut = core.attr(str)

    region: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    run_order: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    version: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        category: str | core.StringOut,
        name: str | core.StringOut,
        owner: str | core.StringOut,
        provider: str | core.StringOut,
        version: str | core.StringOut,
        configuration: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        input_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        namespace: str | core.StringOut | None = None,
        output_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = None,
        region: str | core.StringOut | None = None,
        role_arn: str | core.StringOut | None = None,
        run_order: int | core.IntOut | None = None,
    ):
        super().__init__(
            args=Action.Args(
                category=category,
                name=name,
                owner=owner,
                provider=provider,
                version=version,
                configuration=configuration,
                input_artifacts=input_artifacts,
                namespace=namespace,
                output_artifacts=output_artifacts,
                region=region,
                role_arn=role_arn,
                run_order=run_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        category: str | core.StringOut = core.arg()

        configuration: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        input_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        name: str | core.StringOut = core.arg()

        namespace: str | core.StringOut | None = core.arg(default=None)

        output_artifacts: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        owner: str | core.StringOut = core.arg()

        provider: str | core.StringOut = core.arg()

        region: str | core.StringOut | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        run_order: int | core.IntOut | None = core.arg(default=None)

        version: str | core.StringOut = core.arg()


@core.schema
class Stage(core.Schema):

    action: list[Action] | core.ArrayOut[Action] = core.attr(Action, kind=core.Kind.array)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        *,
        action: list[Action] | core.ArrayOut[Action],
        name: str | core.StringOut,
    ):
        super().__init__(
            args=Stage.Args(
                action=action,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: list[Action] | core.ArrayOut[Action] = core.arg()

        name: str | core.StringOut = core.arg()


@core.resource(type="aws_codepipeline", namespace="codepipeline")
class Main(core.Resource):

    arn: str | core.StringOut = core.attr(str, computed=True)

    artifact_store: list[ArtifactStore] | core.ArrayOut[ArtifactStore] = core.attr(
        ArtifactStore, kind=core.Kind.array
    )

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    role_arn: str | core.StringOut = core.attr(str)

    stage: list[Stage] | core.ArrayOut[Stage] = core.attr(Stage, kind=core.Kind.array)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        artifact_store: list[ArtifactStore] | core.ArrayOut[ArtifactStore],
        name: str | core.StringOut,
        role_arn: str | core.StringOut,
        stage: list[Stage] | core.ArrayOut[Stage],
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                artifact_store=artifact_store,
                name=name,
                role_arn=role_arn,
                stage=stage,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifact_store: list[ArtifactStore] | core.ArrayOut[ArtifactStore] = core.arg()

        name: str | core.StringOut = core.arg()

        role_arn: str | core.StringOut = core.arg()

        stage: list[Stage] | core.ArrayOut[Stage] = core.arg()

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
