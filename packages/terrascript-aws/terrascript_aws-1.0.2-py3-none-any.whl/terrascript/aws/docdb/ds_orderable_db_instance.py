import terrascript.core as core


@core.data(type="aws_docdb_orderable_db_instance", namespace="aws_docdb")
class DsOrderableDbInstance(core.Data):
    """
    Availability zones where the instance is available.
    """

    availability_zones: list[str] | core.ArrayOut[core.StringOut] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    (Optional) DB engine. Default: `docdb`
    """
    engine: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Version of the DB engine.
    """
    engine_version: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) DB instance class. Examples of classes are `db.r5.12xlarge`, `db.r5.24xlarge`, `db.r5.2xl
    arge`, `db.r5.4xlarge`, `db.r5.large`, `db.r5.xlarge`, and `db.t3.medium`. (Conflicts with `preferre
    d_instance_classes`.)
    """
    instance_class: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) License model. Default: `na`
    """
    license_model: str | core.StringOut | None = core.attr(str, default=None)

    """
    (Optional) Ordered list of preferred DocumentDB DB instance classes. The first match in this list wi
    ll be returned. If no preferred matches are found and the original search returned more than one res
    ult, an error is returned. (Conflicts with `instance_class`.)
    """
    preferred_instance_classes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    (Optional) Enable to show only VPC.
    """
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
