import terrascript.core as core


@core.schema
class SimpleCriterion(core.Schema):

    comparator: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: str | core.StringOut | None = None,
        key: str | core.StringOut | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=SimpleCriterion.Args(
                comparator=comparator,
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class TagValues(core.Schema):

    key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    value: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        key: str | core.StringOut | None = None,
        value: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=TagValues.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: str | core.StringOut | None = core.arg(default=None)

        value: str | core.StringOut | None = core.arg(default=None)


@core.schema
class TagCriterion(core.Schema):

    comparator: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.attr(
        TagValues, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: str | core.StringOut | None = None,
        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = None,
    ):
        super().__init__(
            args=TagCriterion.Args(
                comparator=comparator,
                tag_values=tag_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: str | core.StringOut | None = core.arg(default=None)

        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.arg(default=None)


@core.schema
class BucketCriteriaExcludesAnd(core.Schema):

    simple_criterion: SimpleCriterion | None = core.attr(
        SimpleCriterion, default=None, computed=True
    )

    tag_criterion: TagCriterion | None = core.attr(TagCriterion, default=None, computed=True)

    def __init__(
        self,
        *,
        simple_criterion: SimpleCriterion | None = None,
        tag_criterion: TagCriterion | None = None,
    ):
        super().__init__(
            args=BucketCriteriaExcludesAnd.Args(
                simple_criterion=simple_criterion,
                tag_criterion=tag_criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_criterion: SimpleCriterion | None = core.arg(default=None)

        tag_criterion: TagCriterion | None = core.arg(default=None)


@core.schema
class BucketCriteriaExcludes(core.Schema):

    and_: list[BucketCriteriaExcludesAnd] | core.ArrayOut[
        BucketCriteriaExcludesAnd
    ] | None = core.attr(
        BucketCriteriaExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: list[BucketCriteriaExcludesAnd]
        | core.ArrayOut[BucketCriteriaExcludesAnd]
        | None = None,
    ):
        super().__init__(
            args=BucketCriteriaExcludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: list[BucketCriteriaExcludesAnd] | core.ArrayOut[
            BucketCriteriaExcludesAnd
        ] | None = core.arg(default=None)


@core.schema
class BucketCriteriaIncludes(core.Schema):

    and_: list[BucketCriteriaExcludesAnd] | core.ArrayOut[
        BucketCriteriaExcludesAnd
    ] | None = core.attr(
        BucketCriteriaExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: list[BucketCriteriaExcludesAnd]
        | core.ArrayOut[BucketCriteriaExcludesAnd]
        | None = None,
    ):
        super().__init__(
            args=BucketCriteriaIncludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: list[BucketCriteriaExcludesAnd] | core.ArrayOut[
            BucketCriteriaExcludesAnd
        ] | None = core.arg(default=None)


@core.schema
class BucketCriteria(core.Schema):

    excludes: BucketCriteriaExcludes | None = core.attr(
        BucketCriteriaExcludes, default=None, computed=True
    )

    includes: BucketCriteriaIncludes | None = core.attr(
        BucketCriteriaIncludes, default=None, computed=True
    )

    def __init__(
        self,
        *,
        excludes: BucketCriteriaExcludes | None = None,
        includes: BucketCriteriaIncludes | None = None,
    ):
        super().__init__(
            args=BucketCriteria.Args(
                excludes=excludes,
                includes=includes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        excludes: BucketCriteriaExcludes | None = core.arg(default=None)

        includes: BucketCriteriaIncludes | None = core.arg(default=None)


@core.schema
class SimpleScopeTerm(core.Schema):

    comparator: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    values: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        comparator: str | core.StringOut | None = None,
        key: str | core.StringOut | None = None,
        values: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=SimpleScopeTerm.Args(
                comparator=comparator,
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        values: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class ScopingExcludesAndTagScopeTerm(core.Schema):

    comparator: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.attr(
        TagValues, default=None, computed=True, kind=core.Kind.array
    )

    target: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        comparator: str | core.StringOut | None = None,
        key: str | core.StringOut | None = None,
        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = None,
        target: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScopingExcludesAndTagScopeTerm.Args(
                comparator=comparator,
                key=key,
                tag_values=tag_values,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScopingExcludesAnd(core.Schema):

    simple_scope_term: SimpleScopeTerm | None = core.attr(
        SimpleScopeTerm, default=None, computed=True
    )

    tag_scope_term: ScopingExcludesAndTagScopeTerm | None = core.attr(
        ScopingExcludesAndTagScopeTerm, default=None, computed=True
    )

    def __init__(
        self,
        *,
        simple_scope_term: SimpleScopeTerm | None = None,
        tag_scope_term: ScopingExcludesAndTagScopeTerm | None = None,
    ):
        super().__init__(
            args=ScopingExcludesAnd.Args(
                simple_scope_term=simple_scope_term,
                tag_scope_term=tag_scope_term,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_scope_term: SimpleScopeTerm | None = core.arg(default=None)

        tag_scope_term: ScopingExcludesAndTagScopeTerm | None = core.arg(default=None)


@core.schema
class ScopingExcludes(core.Schema):

    and_: list[ScopingExcludesAnd] | core.ArrayOut[ScopingExcludesAnd] | None = core.attr(
        ScopingExcludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: list[ScopingExcludesAnd] | core.ArrayOut[ScopingExcludesAnd] | None = None,
    ):
        super().__init__(
            args=ScopingExcludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: list[ScopingExcludesAnd] | core.ArrayOut[ScopingExcludesAnd] | None = core.arg(
            default=None
        )


@core.schema
class ScopingIncludesAndTagScopeTerm(core.Schema):

    comparator: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    key: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.attr(
        TagValues, default=None, kind=core.Kind.array
    )

    target: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        comparator: str | core.StringOut | None = None,
        key: str | core.StringOut | None = None,
        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = None,
        target: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScopingIncludesAndTagScopeTerm.Args(
                comparator=comparator,
                key=key,
                tag_values=tag_values,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparator: str | core.StringOut | None = core.arg(default=None)

        key: str | core.StringOut | None = core.arg(default=None)

        tag_values: list[TagValues] | core.ArrayOut[TagValues] | None = core.arg(default=None)

        target: str | core.StringOut | None = core.arg(default=None)


@core.schema
class ScopingIncludesAnd(core.Schema):

    simple_scope_term: SimpleScopeTerm | None = core.attr(
        SimpleScopeTerm, default=None, computed=True
    )

    tag_scope_term: ScopingIncludesAndTagScopeTerm | None = core.attr(
        ScopingIncludesAndTagScopeTerm, default=None, computed=True
    )

    def __init__(
        self,
        *,
        simple_scope_term: SimpleScopeTerm | None = None,
        tag_scope_term: ScopingIncludesAndTagScopeTerm | None = None,
    ):
        super().__init__(
            args=ScopingIncludesAnd.Args(
                simple_scope_term=simple_scope_term,
                tag_scope_term=tag_scope_term,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        simple_scope_term: SimpleScopeTerm | None = core.arg(default=None)

        tag_scope_term: ScopingIncludesAndTagScopeTerm | None = core.arg(default=None)


@core.schema
class ScopingIncludes(core.Schema):

    and_: list[ScopingIncludesAnd] | core.ArrayOut[ScopingIncludesAnd] | None = core.attr(
        ScopingIncludesAnd, default=None, computed=True, kind=core.Kind.array, alias="and"
    )

    def __init__(
        self,
        *,
        and_: list[ScopingIncludesAnd] | core.ArrayOut[ScopingIncludesAnd] | None = None,
    ):
        super().__init__(
            args=ScopingIncludes.Args(
                and_=and_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: list[ScopingIncludesAnd] | core.ArrayOut[ScopingIncludesAnd] | None = core.arg(
            default=None
        )


@core.schema
class Scoping(core.Schema):

    excludes: ScopingExcludes | None = core.attr(ScopingExcludes, default=None, computed=True)

    includes: ScopingIncludes | None = core.attr(ScopingIncludes, default=None, computed=True)

    def __init__(
        self,
        *,
        excludes: ScopingExcludes | None = None,
        includes: ScopingIncludes | None = None,
    ):
        super().__init__(
            args=Scoping.Args(
                excludes=excludes,
                includes=includes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        excludes: ScopingExcludes | None = core.arg(default=None)

        includes: ScopingIncludes | None = core.arg(default=None)


@core.schema
class BucketDefinitions(core.Schema):

    account_id: str | core.StringOut = core.attr(str)

    buckets: list[str] | core.ArrayOut[core.StringOut] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        account_id: str | core.StringOut,
        buckets: list[str] | core.ArrayOut[core.StringOut],
    ):
        super().__init__(
            args=BucketDefinitions.Args(
                account_id=account_id,
                buckets=buckets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: str | core.StringOut = core.arg()

        buckets: list[str] | core.ArrayOut[core.StringOut] = core.arg()


@core.schema
class S3JobDefinition(core.Schema):

    bucket_criteria: BucketCriteria | None = core.attr(BucketCriteria, default=None, computed=True)

    bucket_definitions: list[BucketDefinitions] | core.ArrayOut[
        BucketDefinitions
    ] | None = core.attr(BucketDefinitions, default=None, kind=core.Kind.array)

    scoping: Scoping | None = core.attr(Scoping, default=None, computed=True)

    def __init__(
        self,
        *,
        bucket_criteria: BucketCriteria | None = None,
        bucket_definitions: list[BucketDefinitions]
        | core.ArrayOut[BucketDefinitions]
        | None = None,
        scoping: Scoping | None = None,
    ):
        super().__init__(
            args=S3JobDefinition.Args(
                bucket_criteria=bucket_criteria,
                bucket_definitions=bucket_definitions,
                scoping=scoping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_criteria: BucketCriteria | None = core.arg(default=None)

        bucket_definitions: list[BucketDefinitions] | core.ArrayOut[
            BucketDefinitions
        ] | None = core.arg(default=None)

        scoping: Scoping | None = core.arg(default=None)


@core.schema
class UserPausedDetails(core.Schema):

    job_expires_at: str | core.StringOut = core.attr(str, computed=True)

    job_imminent_expiration_health_event_arn: str | core.StringOut = core.attr(str, computed=True)

    job_paused_at: str | core.StringOut = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        job_expires_at: str | core.StringOut,
        job_imminent_expiration_health_event_arn: str | core.StringOut,
        job_paused_at: str | core.StringOut,
    ):
        super().__init__(
            args=UserPausedDetails.Args(
                job_expires_at=job_expires_at,
                job_imminent_expiration_health_event_arn=job_imminent_expiration_health_event_arn,
                job_paused_at=job_paused_at,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        job_expires_at: str | core.StringOut = core.arg()

        job_imminent_expiration_health_event_arn: str | core.StringOut = core.arg()

        job_paused_at: str | core.StringOut = core.arg()


@core.schema
class ScheduleFrequency(core.Schema):

    daily_schedule: bool | core.BoolOut | None = core.attr(bool, default=None)

    monthly_schedule: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    weekly_schedule: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        daily_schedule: bool | core.BoolOut | None = None,
        monthly_schedule: int | core.IntOut | None = None,
        weekly_schedule: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=ScheduleFrequency.Args(
                daily_schedule=daily_schedule,
                monthly_schedule=monthly_schedule,
                weekly_schedule=weekly_schedule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        daily_schedule: bool | core.BoolOut | None = core.arg(default=None)

        monthly_schedule: int | core.IntOut | None = core.arg(default=None)

        weekly_schedule: str | core.StringOut | None = core.arg(default=None)


@core.resource(type="aws_macie2_classification_job", namespace="macie2")
class ClassificationJob(core.Resource):
    """
    The date and time, in UTC and extended RFC 3339 format, when the job was created.
    """

    created_at: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The custom data identifiers to use for data analysis and classification.
    """
    custom_data_identifier_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) A custom description of the job. The description can contain as many as 200 characters.
    """
    description: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    The unique identifier (ID) of the macie classification job.
    """
    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) Specifies whether to analyze all existing, eligible objects immediately after the job is
    created.
    """
    initial_run: bool | core.BoolOut | None = core.attr(bool, default=None)

    job_arn: str | core.StringOut = core.attr(str, computed=True)

    job_id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The status for the job. Valid values are: `CANCELLED`, `RUNNING` and `USER_PAUSED`
    """
    job_status: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Required) The schedule for running the job. Valid values are: `ONE_TIME` - Run the job only once.
    If you specify this value, don't specify a value for the `schedule_frequency` property. `SCHEDULED`
    Run the job on a daily, weekly, or monthly basis. If you specify this value, use the `schedule_fre
    quency` property to define the recurrence pattern for the job.
    """
    job_type: str | core.StringOut = core.attr(str)

    """
    (Optional) A custom name for the job. The name can contain as many as 500 characters. If omitted, T
    erraform will assign a random, unique name. Conflicts with `name_prefix`.
    """
    name: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    name_prefix: str | core.StringOut | None = core.attr(str, default=None, computed=True)

    """
    (Optional) The S3 buckets that contain the objects to analyze, and the scope of that analysis. (doc
    umented below)
    """
    s3_job_definition: S3JobDefinition = core.attr(S3JobDefinition)

    """
    (Optional) The sampling depth, as a percentage, to apply when processing objects. This value determ
    ines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazo
    n Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all t
    he data in those objects.
    """
    sampling_percentage: int | core.IntOut | None = core.attr(int, default=None, computed=True)

    """
    (Optional) The recurrence pattern for running the job. To run the job only once, don't specify a va
    lue for this property and set the value for the `job_type` property to `ONE_TIME`. (documented below
    )
    """
    schedule_frequency: ScheduleFrequency | None = core.attr(
        ScheduleFrequency, default=None, computed=True
    )

    """
    (Optional) A map of key-value pairs that specifies the tags to associate with the job. A job can ha
    ve a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum len
    gth of a tag key is 128 characters. The maximum length of a tag value is 256 characters.
    """
    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    If the current status of the job is `USER_PAUSED`, specifies when the job was paused and when the jo
    b or job run will expire and be cancelled if it isn't resumed. This value is present only if the val
    ue for `job-status` is `USER_PAUSED`.
    """
    user_paused_details: list[UserPausedDetails] | core.ArrayOut[UserPausedDetails] = core.attr(
        UserPausedDetails, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        job_type: str | core.StringOut,
        s3_job_definition: S3JobDefinition,
        custom_data_identifier_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        description: str | core.StringOut | None = None,
        initial_run: bool | core.BoolOut | None = None,
        job_status: str | core.StringOut | None = None,
        name: str | core.StringOut | None = None,
        name_prefix: str | core.StringOut | None = None,
        sampling_percentage: int | core.IntOut | None = None,
        schedule_frequency: ScheduleFrequency | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        depends_on: list[str] | core.ArrayOut[core.StringOut] | None = None,
        provider: str | core.StringOut | None = None,
        lifecycle: core.Lifecycle | None = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClassificationJob.Args(
                job_type=job_type,
                s3_job_definition=s3_job_definition,
                custom_data_identifier_ids=custom_data_identifier_ids,
                description=description,
                initial_run=initial_run,
                job_status=job_status,
                name=name,
                name_prefix=name_prefix,
                sampling_percentage=sampling_percentage,
                schedule_frequency=schedule_frequency,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        custom_data_identifier_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        description: str | core.StringOut | None = core.arg(default=None)

        initial_run: bool | core.BoolOut | None = core.arg(default=None)

        job_status: str | core.StringOut | None = core.arg(default=None)

        job_type: str | core.StringOut = core.arg()

        name: str | core.StringOut | None = core.arg(default=None)

        name_prefix: str | core.StringOut | None = core.arg(default=None)

        s3_job_definition: S3JobDefinition = core.arg()

        sampling_percentage: int | core.IntOut | None = core.arg(default=None)

        schedule_frequency: ScheduleFrequency | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        tags_all: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)
