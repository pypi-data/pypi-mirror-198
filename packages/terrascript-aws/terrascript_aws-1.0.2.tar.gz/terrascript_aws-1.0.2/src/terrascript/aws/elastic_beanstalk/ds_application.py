import terrascript.core as core


@core.schema
class AppversionLifecycle(core.Schema):

    delete_source_from_s3: bool | core.BoolOut = core.attr(bool, computed=True)

    max_age_in_days: int | core.IntOut = core.attr(int, computed=True)

    max_count: int | core.IntOut = core.attr(int, computed=True)

    service_role: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_source_from_s3: bool | core.BoolOut,
        max_age_in_days: int | core.IntOut,
        max_count: int | core.IntOut,
        service_role: str | core.StringOut,
    ):
        super().__init__(
            args=AppversionLifecycle.Args(
                delete_source_from_s3=delete_source_from_s3,
                max_age_in_days=max_age_in_days,
                max_count=max_count,
                service_role=service_role,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_source_from_s3: bool | core.BoolOut = core.arg()

        max_age_in_days: int | core.IntOut = core.arg()

        max_count: int | core.IntOut = core.arg()

        service_role: str | core.StringOut = core.arg()


@core.data(type="aws_elastic_beanstalk_application", namespace="aws_elastic_beanstalk")
class DsApplication(core.Data):

    appversion_lifecycle: list[AppversionLifecycle] | core.ArrayOut[
        AppversionLifecycle
    ] = core.attr(AppversionLifecycle, computed=True, kind=core.Kind.array)

    arn: str | core.StringOut = core.attr(str, computed=True)

    description: str | core.StringOut = core.attr(str, computed=True)

    id: str | core.StringOut = core.attr(str, computed=True)

    name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: str | core.StringOut,
    ):
        super().__init__(
            name=data_name,
            args=DsApplication.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: str | core.StringOut = core.arg()
