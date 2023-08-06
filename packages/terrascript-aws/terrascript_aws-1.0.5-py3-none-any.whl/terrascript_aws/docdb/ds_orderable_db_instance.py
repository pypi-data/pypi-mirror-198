import terrascript.core as core


@core.data(type="aws_docdb_orderable_db_instance", namespace="docdb")
class DsOrderableDbInstance(core.Data):

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    engine: str | core.StringOut | None = core.attr(str, default=None)

    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    instance_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    license_model: str | core.StringOut | None = core.attr(str, default=None)

    preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc: bool | core.BoolOut | None = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        engine: str | core.StringOut | None = None,
        engine_version: str | core.StringOut | None = None,
        instance_class: str | core.StringOut | None = None,
        license_model: str | core.StringOut | None = None,
        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        vpc: bool | core.BoolOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOrderableDbInstance.Args(
                engine=engine,
                engine_version=engine_version,
                instance_class=instance_class,
                license_model=license_model,
                preferred_instance_classes=preferred_instance_classes,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        engine: str | core.StringOut | None = core.arg(default=None)

        engine_version: str | core.StringOut | None = core.arg(default=None)

        instance_class: str | core.StringOut | None = core.arg(default=None)

        license_model: str | core.StringOut | None = core.arg(default=None)

        preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        vpc: bool | core.BoolOut | None = core.arg(default=None)
