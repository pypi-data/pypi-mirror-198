import terrascript.core as core


@core.schema
class DefaultTags(core.Schema):

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=DefaultTags.Args(
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class Endpoints(core.Schema):

    accessanalyzer: str | core.StringOut | None = core.attr(str, default=None)

    account: str | core.StringOut | None = core.attr(str, default=None)

    acm: str | core.StringOut | None = core.attr(str, default=None)

    acmpca: str | core.StringOut | None = core.attr(str, default=None)

    alexaforbusiness: str | core.StringOut | None = core.attr(str, default=None)

    amg: str | core.StringOut | None = core.attr(str, default=None)

    amp: str | core.StringOut | None = core.attr(str, default=None)

    amplify: str | core.StringOut | None = core.attr(str, default=None)

    amplifybackend: str | core.StringOut | None = core.attr(str, default=None)

    amplifyuibuilder: str | core.StringOut | None = core.attr(str, default=None)

    apigateway: str | core.StringOut | None = core.attr(str, default=None)

    apigatewaymanagementapi: str | core.StringOut | None = core.attr(str, default=None)

    apigatewayv2: str | core.StringOut | None = core.attr(str, default=None)

    appautoscaling: str | core.StringOut | None = core.attr(str, default=None)

    appconfig: str | core.StringOut | None = core.attr(str, default=None)

    appconfigdata: str | core.StringOut | None = core.attr(str, default=None)

    appflow: str | core.StringOut | None = core.attr(str, default=None)

    appintegrations: str | core.StringOut | None = core.attr(str, default=None)

    appintegrationsservice: str | core.StringOut | None = core.attr(str, default=None)

    applicationautoscaling: str | core.StringOut | None = core.attr(str, default=None)

    applicationcostprofiler: str | core.StringOut | None = core.attr(str, default=None)

    applicationdiscovery: str | core.StringOut | None = core.attr(str, default=None)

    applicationdiscoveryservice: str | core.StringOut | None = core.attr(str, default=None)

    applicationinsights: str | core.StringOut | None = core.attr(str, default=None)

    appmesh: str | core.StringOut | None = core.attr(str, default=None)

    appregistry: str | core.StringOut | None = core.attr(str, default=None)

    apprunner: str | core.StringOut | None = core.attr(str, default=None)

    appstream: str | core.StringOut | None = core.attr(str, default=None)

    appsync: str | core.StringOut | None = core.attr(str, default=None)

    athena: str | core.StringOut | None = core.attr(str, default=None)

    auditmanager: str | core.StringOut | None = core.attr(str, default=None)

    augmentedairuntime: str | core.StringOut | None = core.attr(str, default=None)

    autoscaling: str | core.StringOut | None = core.attr(str, default=None)

    autoscalingplans: str | core.StringOut | None = core.attr(str, default=None)

    backup: str | core.StringOut | None = core.attr(str, default=None)

    backupgateway: str | core.StringOut | None = core.attr(str, default=None)

    batch: str | core.StringOut | None = core.attr(str, default=None)

    beanstalk: str | core.StringOut | None = core.attr(str, default=None)

    billingconductor: str | core.StringOut | None = core.attr(str, default=None)

    braket: str | core.StringOut | None = core.attr(str, default=None)

    budgets: str | core.StringOut | None = core.attr(str, default=None)

    ce: str | core.StringOut | None = core.attr(str, default=None)

    chime: str | core.StringOut | None = core.attr(str, default=None)

    chimesdkidentity: str | core.StringOut | None = core.attr(str, default=None)

    chimesdkmeetings: str | core.StringOut | None = core.attr(str, default=None)

    chimesdkmessaging: str | core.StringOut | None = core.attr(str, default=None)

    cloud9: str | core.StringOut | None = core.attr(str, default=None)

    cloudcontrol: str | core.StringOut | None = core.attr(str, default=None)

    cloudcontrolapi: str | core.StringOut | None = core.attr(str, default=None)

    clouddirectory: str | core.StringOut | None = core.attr(str, default=None)

    cloudformation: str | core.StringOut | None = core.attr(str, default=None)

    cloudfront: str | core.StringOut | None = core.attr(str, default=None)

    cloudhsm: str | core.StringOut | None = core.attr(str, default=None)

    cloudhsmv2: str | core.StringOut | None = core.attr(str, default=None)

    cloudsearch: str | core.StringOut | None = core.attr(str, default=None)

    cloudsearchdomain: str | core.StringOut | None = core.attr(str, default=None)

    cloudtrail: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatch: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatchevents: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatchevidently: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatchlog: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatchlogs: str | core.StringOut | None = core.attr(str, default=None)

    cloudwatchrum: str | core.StringOut | None = core.attr(str, default=None)

    codeartifact: str | core.StringOut | None = core.attr(str, default=None)

    codebuild: str | core.StringOut | None = core.attr(str, default=None)

    codecommit: str | core.StringOut | None = core.attr(str, default=None)

    codedeploy: str | core.StringOut | None = core.attr(str, default=None)

    codeguruprofiler: str | core.StringOut | None = core.attr(str, default=None)

    codegurureviewer: str | core.StringOut | None = core.attr(str, default=None)

    codepipeline: str | core.StringOut | None = core.attr(str, default=None)

    codestar: str | core.StringOut | None = core.attr(str, default=None)

    codestarconnections: str | core.StringOut | None = core.attr(str, default=None)

    codestarnotifications: str | core.StringOut | None = core.attr(str, default=None)

    cognitoidentity: str | core.StringOut | None = core.attr(str, default=None)

    cognitoidentityprovider: str | core.StringOut | None = core.attr(str, default=None)

    cognitoidp: str | core.StringOut | None = core.attr(str, default=None)

    cognitosync: str | core.StringOut | None = core.attr(str, default=None)

    comprehend: str | core.StringOut | None = core.attr(str, default=None)

    comprehendmedical: str | core.StringOut | None = core.attr(str, default=None)

    computeoptimizer: str | core.StringOut | None = core.attr(str, default=None)

    config: str | core.StringOut | None = core.attr(str, default=None)

    configservice: str | core.StringOut | None = core.attr(str, default=None)

    connect: str | core.StringOut | None = core.attr(str, default=None)

    connectcontactlens: str | core.StringOut | None = core.attr(str, default=None)

    connectparticipant: str | core.StringOut | None = core.attr(str, default=None)

    connectwisdomservice: str | core.StringOut | None = core.attr(str, default=None)

    costandusagereportservice: str | core.StringOut | None = core.attr(str, default=None)

    costexplorer: str | core.StringOut | None = core.attr(str, default=None)

    cur: str | core.StringOut | None = core.attr(str, default=None)

    customerprofiles: str | core.StringOut | None = core.attr(str, default=None)

    databasemigration: str | core.StringOut | None = core.attr(str, default=None)

    databasemigrationservice: str | core.StringOut | None = core.attr(str, default=None)

    databrew: str | core.StringOut | None = core.attr(str, default=None)

    dataexchange: str | core.StringOut | None = core.attr(str, default=None)

    datapipeline: str | core.StringOut | None = core.attr(str, default=None)

    datasync: str | core.StringOut | None = core.attr(str, default=None)

    dax: str | core.StringOut | None = core.attr(str, default=None)

    deploy: str | core.StringOut | None = core.attr(str, default=None)

    detective: str | core.StringOut | None = core.attr(str, default=None)

    devicefarm: str | core.StringOut | None = core.attr(str, default=None)

    devopsguru: str | core.StringOut | None = core.attr(str, default=None)

    directconnect: str | core.StringOut | None = core.attr(str, default=None)

    directoryservice: str | core.StringOut | None = core.attr(str, default=None)

    discovery: str | core.StringOut | None = core.attr(str, default=None)

    dlm: str | core.StringOut | None = core.attr(str, default=None)

    dms: str | core.StringOut | None = core.attr(str, default=None)

    docdb: str | core.StringOut | None = core.attr(str, default=None)

    drs: str | core.StringOut | None = core.attr(str, default=None)

    ds: str | core.StringOut | None = core.attr(str, default=None)

    dynamodb: str | core.StringOut | None = core.attr(str, default=None)

    dynamodbstreams: str | core.StringOut | None = core.attr(str, default=None)

    ebs: str | core.StringOut | None = core.attr(str, default=None)

    ec2: str | core.StringOut | None = core.attr(str, default=None)

    ec2instanceconnect: str | core.StringOut | None = core.attr(str, default=None)

    ecr: str | core.StringOut | None = core.attr(str, default=None)

    ecrpublic: str | core.StringOut | None = core.attr(str, default=None)

    ecs: str | core.StringOut | None = core.attr(str, default=None)

    efs: str | core.StringOut | None = core.attr(str, default=None)

    eks: str | core.StringOut | None = core.attr(str, default=None)

    elasticache: str | core.StringOut | None = core.attr(str, default=None)

    elasticbeanstalk: str | core.StringOut | None = core.attr(str, default=None)

    elasticinference: str | core.StringOut | None = core.attr(str, default=None)

    elasticloadbalancing: str | core.StringOut | None = core.attr(str, default=None)

    elasticloadbalancingv2: str | core.StringOut | None = core.attr(str, default=None)

    elasticsearch: str | core.StringOut | None = core.attr(str, default=None)

    elasticsearchservice: str | core.StringOut | None = core.attr(str, default=None)

    elastictranscoder: str | core.StringOut | None = core.attr(str, default=None)

    elb: str | core.StringOut | None = core.attr(str, default=None)

    elbv2: str | core.StringOut | None = core.attr(str, default=None)

    emr: str | core.StringOut | None = core.attr(str, default=None)

    emrcontainers: str | core.StringOut | None = core.attr(str, default=None)

    emrserverless: str | core.StringOut | None = core.attr(str, default=None)

    es: str | core.StringOut | None = core.attr(str, default=None)

    eventbridge: str | core.StringOut | None = core.attr(str, default=None)

    events: str | core.StringOut | None = core.attr(str, default=None)

    evidently: str | core.StringOut | None = core.attr(str, default=None)

    finspace: str | core.StringOut | None = core.attr(str, default=None)

    finspacedata: str | core.StringOut | None = core.attr(str, default=None)

    firehose: str | core.StringOut | None = core.attr(str, default=None)

    fis: str | core.StringOut | None = core.attr(str, default=None)

    fms: str | core.StringOut | None = core.attr(str, default=None)

    forecast: str | core.StringOut | None = core.attr(str, default=None)

    forecastquery: str | core.StringOut | None = core.attr(str, default=None)

    forecastqueryservice: str | core.StringOut | None = core.attr(str, default=None)

    forecastservice: str | core.StringOut | None = core.attr(str, default=None)

    frauddetector: str | core.StringOut | None = core.attr(str, default=None)

    fsx: str | core.StringOut | None = core.attr(str, default=None)

    gamelift: str | core.StringOut | None = core.attr(str, default=None)

    glacier: str | core.StringOut | None = core.attr(str, default=None)

    globalaccelerator: str | core.StringOut | None = core.attr(str, default=None)

    glue: str | core.StringOut | None = core.attr(str, default=None)

    gluedatabrew: str | core.StringOut | None = core.attr(str, default=None)

    grafana: str | core.StringOut | None = core.attr(str, default=None)

    greengrass: str | core.StringOut | None = core.attr(str, default=None)

    greengrassv2: str | core.StringOut | None = core.attr(str, default=None)

    groundstation: str | core.StringOut | None = core.attr(str, default=None)

    guardduty: str | core.StringOut | None = core.attr(str, default=None)

    health: str | core.StringOut | None = core.attr(str, default=None)

    healthlake: str | core.StringOut | None = core.attr(str, default=None)

    honeycode: str | core.StringOut | None = core.attr(str, default=None)

    iam: str | core.StringOut | None = core.attr(str, default=None)

    identitystore: str | core.StringOut | None = core.attr(str, default=None)

    imagebuilder: str | core.StringOut | None = core.attr(str, default=None)

    inspector: str | core.StringOut | None = core.attr(str, default=None)

    inspector2: str | core.StringOut | None = core.attr(str, default=None)

    iot: str | core.StringOut | None = core.attr(str, default=None)

    iot1clickdevices: str | core.StringOut | None = core.attr(str, default=None)

    iot1clickdevicesservice: str | core.StringOut | None = core.attr(str, default=None)

    iot1clickprojects: str | core.StringOut | None = core.attr(str, default=None)

    iotanalytics: str | core.StringOut | None = core.attr(str, default=None)

    iotdata: str | core.StringOut | None = core.attr(str, default=None)

    iotdataplane: str | core.StringOut | None = core.attr(str, default=None)

    iotdeviceadvisor: str | core.StringOut | None = core.attr(str, default=None)

    iotevents: str | core.StringOut | None = core.attr(str, default=None)

    ioteventsdata: str | core.StringOut | None = core.attr(str, default=None)

    iotfleethub: str | core.StringOut | None = core.attr(str, default=None)

    iotjobsdata: str | core.StringOut | None = core.attr(str, default=None)

    iotjobsdataplane: str | core.StringOut | None = core.attr(str, default=None)

    iotsecuretunneling: str | core.StringOut | None = core.attr(str, default=None)

    iotsitewise: str | core.StringOut | None = core.attr(str, default=None)

    iotthingsgraph: str | core.StringOut | None = core.attr(str, default=None)

    iottwinmaker: str | core.StringOut | None = core.attr(str, default=None)

    iotwireless: str | core.StringOut | None = core.attr(str, default=None)

    ivs: str | core.StringOut | None = core.attr(str, default=None)

    kafka: str | core.StringOut | None = core.attr(str, default=None)

    kafkaconnect: str | core.StringOut | None = core.attr(str, default=None)

    kendra: str | core.StringOut | None = core.attr(str, default=None)

    keyspaces: str | core.StringOut | None = core.attr(str, default=None)

    kinesis: str | core.StringOut | None = core.attr(str, default=None)

    kinesisanalytics: str | core.StringOut | None = core.attr(str, default=None)

    kinesisanalyticsv2: str | core.StringOut | None = core.attr(str, default=None)

    kinesisvideo: str | core.StringOut | None = core.attr(str, default=None)

    kinesisvideoarchivedmedia: str | core.StringOut | None = core.attr(str, default=None)

    kinesisvideomedia: str | core.StringOut | None = core.attr(str, default=None)

    kinesisvideosignaling: str | core.StringOut | None = core.attr(str, default=None)

    kinesisvideosignalingchannels: str | core.StringOut | None = core.attr(str, default=None)

    kms: str | core.StringOut | None = core.attr(str, default=None)

    lakeformation: str | core.StringOut | None = core.attr(str, default=None)

    lambda_: str | core.StringOut | None = core.attr(str, default=None, alias="lambda")

    lex: str | core.StringOut | None = core.attr(str, default=None)

    lexmodelbuilding: str | core.StringOut | None = core.attr(str, default=None)

    lexmodelbuildingservice: str | core.StringOut | None = core.attr(str, default=None)

    lexmodels: str | core.StringOut | None = core.attr(str, default=None)

    lexmodelsv2: str | core.StringOut | None = core.attr(str, default=None)

    lexruntime: str | core.StringOut | None = core.attr(str, default=None)

    lexruntimeservice: str | core.StringOut | None = core.attr(str, default=None)

    lexruntimev2: str | core.StringOut | None = core.attr(str, default=None)

    lexv2models: str | core.StringOut | None = core.attr(str, default=None)

    lexv2runtime: str | core.StringOut | None = core.attr(str, default=None)

    licensemanager: str | core.StringOut | None = core.attr(str, default=None)

    lightsail: str | core.StringOut | None = core.attr(str, default=None)

    location: str | core.StringOut | None = core.attr(str, default=None)

    locationservice: str | core.StringOut | None = core.attr(str, default=None)

    logs: str | core.StringOut | None = core.attr(str, default=None)

    lookoutequipment: str | core.StringOut | None = core.attr(str, default=None)

    lookoutforvision: str | core.StringOut | None = core.attr(str, default=None)

    lookoutmetrics: str | core.StringOut | None = core.attr(str, default=None)

    lookoutvision: str | core.StringOut | None = core.attr(str, default=None)

    machinelearning: str | core.StringOut | None = core.attr(str, default=None)

    macie: str | core.StringOut | None = core.attr(str, default=None)

    macie2: str | core.StringOut | None = core.attr(str, default=None)

    managedblockchain: str | core.StringOut | None = core.attr(str, default=None)

    managedgrafana: str | core.StringOut | None = core.attr(str, default=None)

    marketplacecatalog: str | core.StringOut | None = core.attr(str, default=None)

    marketplacecommerceanalytics: str | core.StringOut | None = core.attr(str, default=None)

    marketplaceentitlement: str | core.StringOut | None = core.attr(str, default=None)

    marketplaceentitlementservice: str | core.StringOut | None = core.attr(str, default=None)

    marketplacemetering: str | core.StringOut | None = core.attr(str, default=None)

    mediaconnect: str | core.StringOut | None = core.attr(str, default=None)

    mediaconvert: str | core.StringOut | None = core.attr(str, default=None)

    medialive: str | core.StringOut | None = core.attr(str, default=None)

    mediapackage: str | core.StringOut | None = core.attr(str, default=None)

    mediapackagevod: str | core.StringOut | None = core.attr(str, default=None)

    mediastore: str | core.StringOut | None = core.attr(str, default=None)

    mediastoredata: str | core.StringOut | None = core.attr(str, default=None)

    mediatailor: str | core.StringOut | None = core.attr(str, default=None)

    memorydb: str | core.StringOut | None = core.attr(str, default=None)

    meteringmarketplace: str | core.StringOut | None = core.attr(str, default=None)

    mgh: str | core.StringOut | None = core.attr(str, default=None)

    mgn: str | core.StringOut | None = core.attr(str, default=None)

    migrationhub: str | core.StringOut | None = core.attr(str, default=None)

    migrationhubconfig: str | core.StringOut | None = core.attr(str, default=None)

    migrationhubrefactorspaces: str | core.StringOut | None = core.attr(str, default=None)

    migrationhubstrategy: str | core.StringOut | None = core.attr(str, default=None)

    migrationhubstrategyrecommendations: str | core.StringOut | None = core.attr(str, default=None)

    mobile: str | core.StringOut | None = core.attr(str, default=None)

    mq: str | core.StringOut | None = core.attr(str, default=None)

    msk: str | core.StringOut | None = core.attr(str, default=None)

    mturk: str | core.StringOut | None = core.attr(str, default=None)

    mwaa: str | core.StringOut | None = core.attr(str, default=None)

    neptune: str | core.StringOut | None = core.attr(str, default=None)

    networkfirewall: str | core.StringOut | None = core.attr(str, default=None)

    networkmanager: str | core.StringOut | None = core.attr(str, default=None)

    nimble: str | core.StringOut | None = core.attr(str, default=None)

    nimblestudio: str | core.StringOut | None = core.attr(str, default=None)

    opensearch: str | core.StringOut | None = core.attr(str, default=None)

    opensearchservice: str | core.StringOut | None = core.attr(str, default=None)

    opsworks: str | core.StringOut | None = core.attr(str, default=None)

    opsworkscm: str | core.StringOut | None = core.attr(str, default=None)

    organizations: str | core.StringOut | None = core.attr(str, default=None)

    outposts: str | core.StringOut | None = core.attr(str, default=None)

    panorama: str | core.StringOut | None = core.attr(str, default=None)

    personalize: str | core.StringOut | None = core.attr(str, default=None)

    personalizeevents: str | core.StringOut | None = core.attr(str, default=None)

    personalizeruntime: str | core.StringOut | None = core.attr(str, default=None)

    pi: str | core.StringOut | None = core.attr(str, default=None)

    pinpoint: str | core.StringOut | None = core.attr(str, default=None)

    pinpointemail: str | core.StringOut | None = core.attr(str, default=None)

    pinpointsmsvoice: str | core.StringOut | None = core.attr(str, default=None)

    polly: str | core.StringOut | None = core.attr(str, default=None)

    pricing: str | core.StringOut | None = core.attr(str, default=None)

    prometheus: str | core.StringOut | None = core.attr(str, default=None)

    prometheusservice: str | core.StringOut | None = core.attr(str, default=None)

    proton: str | core.StringOut | None = core.attr(str, default=None)

    qldb: str | core.StringOut | None = core.attr(str, default=None)

    qldbsession: str | core.StringOut | None = core.attr(str, default=None)

    quicksight: str | core.StringOut | None = core.attr(str, default=None)

    ram: str | core.StringOut | None = core.attr(str, default=None)

    rbin: str | core.StringOut | None = core.attr(str, default=None)

    rds: str | core.StringOut | None = core.attr(str, default=None)

    rdsdata: str | core.StringOut | None = core.attr(str, default=None)

    rdsdataservice: str | core.StringOut | None = core.attr(str, default=None)

    recyclebin: str | core.StringOut | None = core.attr(str, default=None)

    redshift: str | core.StringOut | None = core.attr(str, default=None)

    redshiftdata: str | core.StringOut | None = core.attr(str, default=None)

    redshiftdataapiservice: str | core.StringOut | None = core.attr(str, default=None)

    redshiftserverless: str | core.StringOut | None = core.attr(str, default=None)

    rekognition: str | core.StringOut | None = core.attr(str, default=None)

    resiliencehub: str | core.StringOut | None = core.attr(str, default=None)

    resourcegroups: str | core.StringOut | None = core.attr(str, default=None)

    resourcegroupstagging: str | core.StringOut | None = core.attr(str, default=None)

    resourcegroupstaggingapi: str | core.StringOut | None = core.attr(str, default=None)

    robomaker: str | core.StringOut | None = core.attr(str, default=None)

    rolesanywhere: str | core.StringOut | None = core.attr(str, default=None)

    route53: str | core.StringOut | None = core.attr(str, default=None)

    route53domains: str | core.StringOut | None = core.attr(str, default=None)

    route53recoverycluster: str | core.StringOut | None = core.attr(str, default=None)

    route53recoverycontrolconfig: str | core.StringOut | None = core.attr(str, default=None)

    route53recoveryreadiness: str | core.StringOut | None = core.attr(str, default=None)

    route53resolver: str | core.StringOut | None = core.attr(str, default=None)

    rum: str | core.StringOut | None = core.attr(str, default=None)

    s3: str | core.StringOut | None = core.attr(str, default=None)

    s3api: str | core.StringOut | None = core.attr(str, default=None)

    s3control: str | core.StringOut | None = core.attr(str, default=None)

    s3outposts: str | core.StringOut | None = core.attr(str, default=None)

    sagemaker: str | core.StringOut | None = core.attr(str, default=None)

    sagemakera2iruntime: str | core.StringOut | None = core.attr(str, default=None)

    sagemakeredge: str | core.StringOut | None = core.attr(str, default=None)

    sagemakeredgemanager: str | core.StringOut | None = core.attr(str, default=None)

    sagemakerfeaturestoreruntime: str | core.StringOut | None = core.attr(str, default=None)

    sagemakerruntime: str | core.StringOut | None = core.attr(str, default=None)

    savingsplans: str | core.StringOut | None = core.attr(str, default=None)

    schemas: str | core.StringOut | None = core.attr(str, default=None)

    sdb: str | core.StringOut | None = core.attr(str, default=None)

    secretsmanager: str | core.StringOut | None = core.attr(str, default=None)

    securityhub: str | core.StringOut | None = core.attr(str, default=None)

    serverlessapplicationrepository: str | core.StringOut | None = core.attr(str, default=None)

    serverlessapprepo: str | core.StringOut | None = core.attr(str, default=None)

    serverlessrepo: str | core.StringOut | None = core.attr(str, default=None)

    servicecatalog: str | core.StringOut | None = core.attr(str, default=None)

    servicecatalogappregistry: str | core.StringOut | None = core.attr(str, default=None)

    servicediscovery: str | core.StringOut | None = core.attr(str, default=None)

    servicequotas: str | core.StringOut | None = core.attr(str, default=None)

    ses: str | core.StringOut | None = core.attr(str, default=None)

    sesv2: str | core.StringOut | None = core.attr(str, default=None)

    sfn: str | core.StringOut | None = core.attr(str, default=None)

    shield: str | core.StringOut | None = core.attr(str, default=None)

    signer: str | core.StringOut | None = core.attr(str, default=None)

    simpledb: str | core.StringOut | None = core.attr(str, default=None)

    sms: str | core.StringOut | None = core.attr(str, default=None)

    snowball: str | core.StringOut | None = core.attr(str, default=None)

    snowdevicemanagement: str | core.StringOut | None = core.attr(str, default=None)

    sns: str | core.StringOut | None = core.attr(str, default=None)

    sqs: str | core.StringOut | None = core.attr(str, default=None)

    ssm: str | core.StringOut | None = core.attr(str, default=None)

    ssmcontacts: str | core.StringOut | None = core.attr(str, default=None)

    ssmincidents: str | core.StringOut | None = core.attr(str, default=None)

    sso: str | core.StringOut | None = core.attr(str, default=None)

    ssoadmin: str | core.StringOut | None = core.attr(str, default=None)

    ssooidc: str | core.StringOut | None = core.attr(str, default=None)

    stepfunctions: str | core.StringOut | None = core.attr(str, default=None)

    storagegateway: str | core.StringOut | None = core.attr(str, default=None)

    sts: str | core.StringOut | None = core.attr(str, default=None)

    support: str | core.StringOut | None = core.attr(str, default=None)

    swf: str | core.StringOut | None = core.attr(str, default=None)

    synthetics: str | core.StringOut | None = core.attr(str, default=None)

    textract: str | core.StringOut | None = core.attr(str, default=None)

    timestreamquery: str | core.StringOut | None = core.attr(str, default=None)

    timestreamwrite: str | core.StringOut | None = core.attr(str, default=None)

    transcribe: str | core.StringOut | None = core.attr(str, default=None)

    transcribeservice: str | core.StringOut | None = core.attr(str, default=None)

    transcribestreaming: str | core.StringOut | None = core.attr(str, default=None)

    transcribestreamingservice: str | core.StringOut | None = core.attr(str, default=None)

    transfer: str | core.StringOut | None = core.attr(str, default=None)

    translate: str | core.StringOut | None = core.attr(str, default=None)

    voiceid: str | core.StringOut | None = core.attr(str, default=None)

    waf: str | core.StringOut | None = core.attr(str, default=None)

    wafregional: str | core.StringOut | None = core.attr(str, default=None)

    wafv2: str | core.StringOut | None = core.attr(str, default=None)

    wellarchitected: str | core.StringOut | None = core.attr(str, default=None)

    wisdom: str | core.StringOut | None = core.attr(str, default=None)

    workdocs: str | core.StringOut | None = core.attr(str, default=None)

    worklink: str | core.StringOut | None = core.attr(str, default=None)

    workmail: str | core.StringOut | None = core.attr(str, default=None)

    workmailmessageflow: str | core.StringOut | None = core.attr(str, default=None)

    workspaces: str | core.StringOut | None = core.attr(str, default=None)

    workspacesweb: str | core.StringOut | None = core.attr(str, default=None)

    xray: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        accessanalyzer: str | core.StringOut | None = None,
        account: str | core.StringOut | None = None,
        acm: str | core.StringOut | None = None,
        acmpca: str | core.StringOut | None = None,
        alexaforbusiness: str | core.StringOut | None = None,
        amg: str | core.StringOut | None = None,
        amp: str | core.StringOut | None = None,
        amplify: str | core.StringOut | None = None,
        amplifybackend: str | core.StringOut | None = None,
        amplifyuibuilder: str | core.StringOut | None = None,
        apigateway: str | core.StringOut | None = None,
        apigatewaymanagementapi: str | core.StringOut | None = None,
        apigatewayv2: str | core.StringOut | None = None,
        appautoscaling: str | core.StringOut | None = None,
        appconfig: str | core.StringOut | None = None,
        appconfigdata: str | core.StringOut | None = None,
        appflow: str | core.StringOut | None = None,
        appintegrations: str | core.StringOut | None = None,
        appintegrationsservice: str | core.StringOut | None = None,
        applicationautoscaling: str | core.StringOut | None = None,
        applicationcostprofiler: str | core.StringOut | None = None,
        applicationdiscovery: str | core.StringOut | None = None,
        applicationdiscoveryservice: str | core.StringOut | None = None,
        applicationinsights: str | core.StringOut | None = None,
        appmesh: str | core.StringOut | None = None,
        appregistry: str | core.StringOut | None = None,
        apprunner: str | core.StringOut | None = None,
        appstream: str | core.StringOut | None = None,
        appsync: str | core.StringOut | None = None,
        athena: str | core.StringOut | None = None,
        auditmanager: str | core.StringOut | None = None,
        augmentedairuntime: str | core.StringOut | None = None,
        autoscaling: str | core.StringOut | None = None,
        autoscalingplans: str | core.StringOut | None = None,
        backup: str | core.StringOut | None = None,
        backupgateway: str | core.StringOut | None = None,
        batch: str | core.StringOut | None = None,
        beanstalk: str | core.StringOut | None = None,
        billingconductor: str | core.StringOut | None = None,
        braket: str | core.StringOut | None = None,
        budgets: str | core.StringOut | None = None,
        ce: str | core.StringOut | None = None,
        chime: str | core.StringOut | None = None,
        chimesdkidentity: str | core.StringOut | None = None,
        chimesdkmeetings: str | core.StringOut | None = None,
        chimesdkmessaging: str | core.StringOut | None = None,
        cloud9: str | core.StringOut | None = None,
        cloudcontrol: str | core.StringOut | None = None,
        cloudcontrolapi: str | core.StringOut | None = None,
        clouddirectory: str | core.StringOut | None = None,
        cloudformation: str | core.StringOut | None = None,
        cloudfront: str | core.StringOut | None = None,
        cloudhsm: str | core.StringOut | None = None,
        cloudhsmv2: str | core.StringOut | None = None,
        cloudsearch: str | core.StringOut | None = None,
        cloudsearchdomain: str | core.StringOut | None = None,
        cloudtrail: str | core.StringOut | None = None,
        cloudwatch: str | core.StringOut | None = None,
        cloudwatchevents: str | core.StringOut | None = None,
        cloudwatchevidently: str | core.StringOut | None = None,
        cloudwatchlog: str | core.StringOut | None = None,
        cloudwatchlogs: str | core.StringOut | None = None,
        cloudwatchrum: str | core.StringOut | None = None,
        codeartifact: str | core.StringOut | None = None,
        codebuild: str | core.StringOut | None = None,
        codecommit: str | core.StringOut | None = None,
        codedeploy: str | core.StringOut | None = None,
        codeguruprofiler: str | core.StringOut | None = None,
        codegurureviewer: str | core.StringOut | None = None,
        codepipeline: str | core.StringOut | None = None,
        codestar: str | core.StringOut | None = None,
        codestarconnections: str | core.StringOut | None = None,
        codestarnotifications: str | core.StringOut | None = None,
        cognitoidentity: str | core.StringOut | None = None,
        cognitoidentityprovider: str | core.StringOut | None = None,
        cognitoidp: str | core.StringOut | None = None,
        cognitosync: str | core.StringOut | None = None,
        comprehend: str | core.StringOut | None = None,
        comprehendmedical: str | core.StringOut | None = None,
        computeoptimizer: str | core.StringOut | None = None,
        config: str | core.StringOut | None = None,
        configservice: str | core.StringOut | None = None,
        connect: str | core.StringOut | None = None,
        connectcontactlens: str | core.StringOut | None = None,
        connectparticipant: str | core.StringOut | None = None,
        connectwisdomservice: str | core.StringOut | None = None,
        costandusagereportservice: str | core.StringOut | None = None,
        costexplorer: str | core.StringOut | None = None,
        cur: str | core.StringOut | None = None,
        customerprofiles: str | core.StringOut | None = None,
        databasemigration: str | core.StringOut | None = None,
        databasemigrationservice: str | core.StringOut | None = None,
        databrew: str | core.StringOut | None = None,
        dataexchange: str | core.StringOut | None = None,
        datapipeline: str | core.StringOut | None = None,
        datasync: str | core.StringOut | None = None,
        dax: str | core.StringOut | None = None,
        deploy: str | core.StringOut | None = None,
        detective: str | core.StringOut | None = None,
        devicefarm: str | core.StringOut | None = None,
        devopsguru: str | core.StringOut | None = None,
        directconnect: str | core.StringOut | None = None,
        directoryservice: str | core.StringOut | None = None,
        discovery: str | core.StringOut | None = None,
        dlm: str | core.StringOut | None = None,
        dms: str | core.StringOut | None = None,
        docdb: str | core.StringOut | None = None,
        drs: str | core.StringOut | None = None,
        ds: str | core.StringOut | None = None,
        dynamodb: str | core.StringOut | None = None,
        dynamodbstreams: str | core.StringOut | None = None,
        ebs: str | core.StringOut | None = None,
        ec2: str | core.StringOut | None = None,
        ec2instanceconnect: str | core.StringOut | None = None,
        ecr: str | core.StringOut | None = None,
        ecrpublic: str | core.StringOut | None = None,
        ecs: str | core.StringOut | None = None,
        efs: str | core.StringOut | None = None,
        eks: str | core.StringOut | None = None,
        elasticache: str | core.StringOut | None = None,
        elasticbeanstalk: str | core.StringOut | None = None,
        elasticinference: str | core.StringOut | None = None,
        elasticloadbalancing: str | core.StringOut | None = None,
        elasticloadbalancingv2: str | core.StringOut | None = None,
        elasticsearch: str | core.StringOut | None = None,
        elasticsearchservice: str | core.StringOut | None = None,
        elastictranscoder: str | core.StringOut | None = None,
        elb: str | core.StringOut | None = None,
        elbv2: str | core.StringOut | None = None,
        emr: str | core.StringOut | None = None,
        emrcontainers: str | core.StringOut | None = None,
        emrserverless: str | core.StringOut | None = None,
        es: str | core.StringOut | None = None,
        eventbridge: str | core.StringOut | None = None,
        events: str | core.StringOut | None = None,
        evidently: str | core.StringOut | None = None,
        finspace: str | core.StringOut | None = None,
        finspacedata: str | core.StringOut | None = None,
        firehose: str | core.StringOut | None = None,
        fis: str | core.StringOut | None = None,
        fms: str | core.StringOut | None = None,
        forecast: str | core.StringOut | None = None,
        forecastquery: str | core.StringOut | None = None,
        forecastqueryservice: str | core.StringOut | None = None,
        forecastservice: str | core.StringOut | None = None,
        frauddetector: str | core.StringOut | None = None,
        fsx: str | core.StringOut | None = None,
        gamelift: str | core.StringOut | None = None,
        glacier: str | core.StringOut | None = None,
        globalaccelerator: str | core.StringOut | None = None,
        glue: str | core.StringOut | None = None,
        gluedatabrew: str | core.StringOut | None = None,
        grafana: str | core.StringOut | None = None,
        greengrass: str | core.StringOut | None = None,
        greengrassv2: str | core.StringOut | None = None,
        groundstation: str | core.StringOut | None = None,
        guardduty: str | core.StringOut | None = None,
        health: str | core.StringOut | None = None,
        healthlake: str | core.StringOut | None = None,
        honeycode: str | core.StringOut | None = None,
        iam: str | core.StringOut | None = None,
        identitystore: str | core.StringOut | None = None,
        imagebuilder: str | core.StringOut | None = None,
        inspector: str | core.StringOut | None = None,
        inspector2: str | core.StringOut | None = None,
        iot: str | core.StringOut | None = None,
        iot1clickdevices: str | core.StringOut | None = None,
        iot1clickdevicesservice: str | core.StringOut | None = None,
        iot1clickprojects: str | core.StringOut | None = None,
        iotanalytics: str | core.StringOut | None = None,
        iotdata: str | core.StringOut | None = None,
        iotdataplane: str | core.StringOut | None = None,
        iotdeviceadvisor: str | core.StringOut | None = None,
        iotevents: str | core.StringOut | None = None,
        ioteventsdata: str | core.StringOut | None = None,
        iotfleethub: str | core.StringOut | None = None,
        iotjobsdata: str | core.StringOut | None = None,
        iotjobsdataplane: str | core.StringOut | None = None,
        iotsecuretunneling: str | core.StringOut | None = None,
        iotsitewise: str | core.StringOut | None = None,
        iotthingsgraph: str | core.StringOut | None = None,
        iottwinmaker: str | core.StringOut | None = None,
        iotwireless: str | core.StringOut | None = None,
        ivs: str | core.StringOut | None = None,
        kafka: str | core.StringOut | None = None,
        kafkaconnect: str | core.StringOut | None = None,
        kendra: str | core.StringOut | None = None,
        keyspaces: str | core.StringOut | None = None,
        kinesis: str | core.StringOut | None = None,
        kinesisanalytics: str | core.StringOut | None = None,
        kinesisanalyticsv2: str | core.StringOut | None = None,
        kinesisvideo: str | core.StringOut | None = None,
        kinesisvideoarchivedmedia: str | core.StringOut | None = None,
        kinesisvideomedia: str | core.StringOut | None = None,
        kinesisvideosignaling: str | core.StringOut | None = None,
        kinesisvideosignalingchannels: str | core.StringOut | None = None,
        kms: str | core.StringOut | None = None,
        lakeformation: str | core.StringOut | None = None,
        lambda_: str | core.StringOut | None = None,
        lex: str | core.StringOut | None = None,
        lexmodelbuilding: str | core.StringOut | None = None,
        lexmodelbuildingservice: str | core.StringOut | None = None,
        lexmodels: str | core.StringOut | None = None,
        lexmodelsv2: str | core.StringOut | None = None,
        lexruntime: str | core.StringOut | None = None,
        lexruntimeservice: str | core.StringOut | None = None,
        lexruntimev2: str | core.StringOut | None = None,
        lexv2models: str | core.StringOut | None = None,
        lexv2runtime: str | core.StringOut | None = None,
        licensemanager: str | core.StringOut | None = None,
        lightsail: str | core.StringOut | None = None,
        location: str | core.StringOut | None = None,
        locationservice: str | core.StringOut | None = None,
        logs: str | core.StringOut | None = None,
        lookoutequipment: str | core.StringOut | None = None,
        lookoutforvision: str | core.StringOut | None = None,
        lookoutmetrics: str | core.StringOut | None = None,
        lookoutvision: str | core.StringOut | None = None,
        machinelearning: str | core.StringOut | None = None,
        macie: str | core.StringOut | None = None,
        macie2: str | core.StringOut | None = None,
        managedblockchain: str | core.StringOut | None = None,
        managedgrafana: str | core.StringOut | None = None,
        marketplacecatalog: str | core.StringOut | None = None,
        marketplacecommerceanalytics: str | core.StringOut | None = None,
        marketplaceentitlement: str | core.StringOut | None = None,
        marketplaceentitlementservice: str | core.StringOut | None = None,
        marketplacemetering: str | core.StringOut | None = None,
        mediaconnect: str | core.StringOut | None = None,
        mediaconvert: str | core.StringOut | None = None,
        medialive: str | core.StringOut | None = None,
        mediapackage: str | core.StringOut | None = None,
        mediapackagevod: str | core.StringOut | None = None,
        mediastore: str | core.StringOut | None = None,
        mediastoredata: str | core.StringOut | None = None,
        mediatailor: str | core.StringOut | None = None,
        memorydb: str | core.StringOut | None = None,
        meteringmarketplace: str | core.StringOut | None = None,
        mgh: str | core.StringOut | None = None,
        mgn: str | core.StringOut | None = None,
        migrationhub: str | core.StringOut | None = None,
        migrationhubconfig: str | core.StringOut | None = None,
        migrationhubrefactorspaces: str | core.StringOut | None = None,
        migrationhubstrategy: str | core.StringOut | None = None,
        migrationhubstrategyrecommendations: str | core.StringOut | None = None,
        mobile: str | core.StringOut | None = None,
        mq: str | core.StringOut | None = None,
        msk: str | core.StringOut | None = None,
        mturk: str | core.StringOut | None = None,
        mwaa: str | core.StringOut | None = None,
        neptune: str | core.StringOut | None = None,
        networkfirewall: str | core.StringOut | None = None,
        networkmanager: str | core.StringOut | None = None,
        nimble: str | core.StringOut | None = None,
        nimblestudio: str | core.StringOut | None = None,
        opensearch: str | core.StringOut | None = None,
        opensearchservice: str | core.StringOut | None = None,
        opsworks: str | core.StringOut | None = None,
        opsworkscm: str | core.StringOut | None = None,
        organizations: str | core.StringOut | None = None,
        outposts: str | core.StringOut | None = None,
        panorama: str | core.StringOut | None = None,
        personalize: str | core.StringOut | None = None,
        personalizeevents: str | core.StringOut | None = None,
        personalizeruntime: str | core.StringOut | None = None,
        pi: str | core.StringOut | None = None,
        pinpoint: str | core.StringOut | None = None,
        pinpointemail: str | core.StringOut | None = None,
        pinpointsmsvoice: str | core.StringOut | None = None,
        polly: str | core.StringOut | None = None,
        pricing: str | core.StringOut | None = None,
        prometheus: str | core.StringOut | None = None,
        prometheusservice: str | core.StringOut | None = None,
        proton: str | core.StringOut | None = None,
        qldb: str | core.StringOut | None = None,
        qldbsession: str | core.StringOut | None = None,
        quicksight: str | core.StringOut | None = None,
        ram: str | core.StringOut | None = None,
        rbin: str | core.StringOut | None = None,
        rds: str | core.StringOut | None = None,
        rdsdata: str | core.StringOut | None = None,
        rdsdataservice: str | core.StringOut | None = None,
        recyclebin: str | core.StringOut | None = None,
        redshift: str | core.StringOut | None = None,
        redshiftdata: str | core.StringOut | None = None,
        redshiftdataapiservice: str | core.StringOut | None = None,
        redshiftserverless: str | core.StringOut | None = None,
        rekognition: str | core.StringOut | None = None,
        resiliencehub: str | core.StringOut | None = None,
        resourcegroups: str | core.StringOut | None = None,
        resourcegroupstagging: str | core.StringOut | None = None,
        resourcegroupstaggingapi: str | core.StringOut | None = None,
        robomaker: str | core.StringOut | None = None,
        rolesanywhere: str | core.StringOut | None = None,
        route53: str | core.StringOut | None = None,
        route53domains: str | core.StringOut | None = None,
        route53recoverycluster: str | core.StringOut | None = None,
        route53recoverycontrolconfig: str | core.StringOut | None = None,
        route53recoveryreadiness: str | core.StringOut | None = None,
        route53resolver: str | core.StringOut | None = None,
        rum: str | core.StringOut | None = None,
        s3: str | core.StringOut | None = None,
        s3api: str | core.StringOut | None = None,
        s3control: str | core.StringOut | None = None,
        s3outposts: str | core.StringOut | None = None,
        sagemaker: str | core.StringOut | None = None,
        sagemakera2iruntime: str | core.StringOut | None = None,
        sagemakeredge: str | core.StringOut | None = None,
        sagemakeredgemanager: str | core.StringOut | None = None,
        sagemakerfeaturestoreruntime: str | core.StringOut | None = None,
        sagemakerruntime: str | core.StringOut | None = None,
        savingsplans: str | core.StringOut | None = None,
        schemas: str | core.StringOut | None = None,
        sdb: str | core.StringOut | None = None,
        secretsmanager: str | core.StringOut | None = None,
        securityhub: str | core.StringOut | None = None,
        serverlessapplicationrepository: str | core.StringOut | None = None,
        serverlessapprepo: str | core.StringOut | None = None,
        serverlessrepo: str | core.StringOut | None = None,
        servicecatalog: str | core.StringOut | None = None,
        servicecatalogappregistry: str | core.StringOut | None = None,
        servicediscovery: str | core.StringOut | None = None,
        servicequotas: str | core.StringOut | None = None,
        ses: str | core.StringOut | None = None,
        sesv2: str | core.StringOut | None = None,
        sfn: str | core.StringOut | None = None,
        shield: str | core.StringOut | None = None,
        signer: str | core.StringOut | None = None,
        simpledb: str | core.StringOut | None = None,
        sms: str | core.StringOut | None = None,
        snowball: str | core.StringOut | None = None,
        snowdevicemanagement: str | core.StringOut | None = None,
        sns: str | core.StringOut | None = None,
        sqs: str | core.StringOut | None = None,
        ssm: str | core.StringOut | None = None,
        ssmcontacts: str | core.StringOut | None = None,
        ssmincidents: str | core.StringOut | None = None,
        sso: str | core.StringOut | None = None,
        ssoadmin: str | core.StringOut | None = None,
        ssooidc: str | core.StringOut | None = None,
        stepfunctions: str | core.StringOut | None = None,
        storagegateway: str | core.StringOut | None = None,
        sts: str | core.StringOut | None = None,
        support: str | core.StringOut | None = None,
        swf: str | core.StringOut | None = None,
        synthetics: str | core.StringOut | None = None,
        textract: str | core.StringOut | None = None,
        timestreamquery: str | core.StringOut | None = None,
        timestreamwrite: str | core.StringOut | None = None,
        transcribe: str | core.StringOut | None = None,
        transcribeservice: str | core.StringOut | None = None,
        transcribestreaming: str | core.StringOut | None = None,
        transcribestreamingservice: str | core.StringOut | None = None,
        transfer: str | core.StringOut | None = None,
        translate: str | core.StringOut | None = None,
        voiceid: str | core.StringOut | None = None,
        waf: str | core.StringOut | None = None,
        wafregional: str | core.StringOut | None = None,
        wafv2: str | core.StringOut | None = None,
        wellarchitected: str | core.StringOut | None = None,
        wisdom: str | core.StringOut | None = None,
        workdocs: str | core.StringOut | None = None,
        worklink: str | core.StringOut | None = None,
        workmail: str | core.StringOut | None = None,
        workmailmessageflow: str | core.StringOut | None = None,
        workspaces: str | core.StringOut | None = None,
        workspacesweb: str | core.StringOut | None = None,
        xray: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Endpoints.Args(
                accessanalyzer=accessanalyzer,
                account=account,
                acm=acm,
                acmpca=acmpca,
                alexaforbusiness=alexaforbusiness,
                amg=amg,
                amp=amp,
                amplify=amplify,
                amplifybackend=amplifybackend,
                amplifyuibuilder=amplifyuibuilder,
                apigateway=apigateway,
                apigatewaymanagementapi=apigatewaymanagementapi,
                apigatewayv2=apigatewayv2,
                appautoscaling=appautoscaling,
                appconfig=appconfig,
                appconfigdata=appconfigdata,
                appflow=appflow,
                appintegrations=appintegrations,
                appintegrationsservice=appintegrationsservice,
                applicationautoscaling=applicationautoscaling,
                applicationcostprofiler=applicationcostprofiler,
                applicationdiscovery=applicationdiscovery,
                applicationdiscoveryservice=applicationdiscoveryservice,
                applicationinsights=applicationinsights,
                appmesh=appmesh,
                appregistry=appregistry,
                apprunner=apprunner,
                appstream=appstream,
                appsync=appsync,
                athena=athena,
                auditmanager=auditmanager,
                augmentedairuntime=augmentedairuntime,
                autoscaling=autoscaling,
                autoscalingplans=autoscalingplans,
                backup=backup,
                backupgateway=backupgateway,
                batch=batch,
                beanstalk=beanstalk,
                billingconductor=billingconductor,
                braket=braket,
                budgets=budgets,
                ce=ce,
                chime=chime,
                chimesdkidentity=chimesdkidentity,
                chimesdkmeetings=chimesdkmeetings,
                chimesdkmessaging=chimesdkmessaging,
                cloud9=cloud9,
                cloudcontrol=cloudcontrol,
                cloudcontrolapi=cloudcontrolapi,
                clouddirectory=clouddirectory,
                cloudformation=cloudformation,
                cloudfront=cloudfront,
                cloudhsm=cloudhsm,
                cloudhsmv2=cloudhsmv2,
                cloudsearch=cloudsearch,
                cloudsearchdomain=cloudsearchdomain,
                cloudtrail=cloudtrail,
                cloudwatch=cloudwatch,
                cloudwatchevents=cloudwatchevents,
                cloudwatchevidently=cloudwatchevidently,
                cloudwatchlog=cloudwatchlog,
                cloudwatchlogs=cloudwatchlogs,
                cloudwatchrum=cloudwatchrum,
                codeartifact=codeartifact,
                codebuild=codebuild,
                codecommit=codecommit,
                codedeploy=codedeploy,
                codeguruprofiler=codeguruprofiler,
                codegurureviewer=codegurureviewer,
                codepipeline=codepipeline,
                codestar=codestar,
                codestarconnections=codestarconnections,
                codestarnotifications=codestarnotifications,
                cognitoidentity=cognitoidentity,
                cognitoidentityprovider=cognitoidentityprovider,
                cognitoidp=cognitoidp,
                cognitosync=cognitosync,
                comprehend=comprehend,
                comprehendmedical=comprehendmedical,
                computeoptimizer=computeoptimizer,
                config=config,
                configservice=configservice,
                connect=connect,
                connectcontactlens=connectcontactlens,
                connectparticipant=connectparticipant,
                connectwisdomservice=connectwisdomservice,
                costandusagereportservice=costandusagereportservice,
                costexplorer=costexplorer,
                cur=cur,
                customerprofiles=customerprofiles,
                databasemigration=databasemigration,
                databasemigrationservice=databasemigrationservice,
                databrew=databrew,
                dataexchange=dataexchange,
                datapipeline=datapipeline,
                datasync=datasync,
                dax=dax,
                deploy=deploy,
                detective=detective,
                devicefarm=devicefarm,
                devopsguru=devopsguru,
                directconnect=directconnect,
                directoryservice=directoryservice,
                discovery=discovery,
                dlm=dlm,
                dms=dms,
                docdb=docdb,
                drs=drs,
                ds=ds,
                dynamodb=dynamodb,
                dynamodbstreams=dynamodbstreams,
                ebs=ebs,
                ec2=ec2,
                ec2instanceconnect=ec2instanceconnect,
                ecr=ecr,
                ecrpublic=ecrpublic,
                ecs=ecs,
                efs=efs,
                eks=eks,
                elasticache=elasticache,
                elasticbeanstalk=elasticbeanstalk,
                elasticinference=elasticinference,
                elasticloadbalancing=elasticloadbalancing,
                elasticloadbalancingv2=elasticloadbalancingv2,
                elasticsearch=elasticsearch,
                elasticsearchservice=elasticsearchservice,
                elastictranscoder=elastictranscoder,
                elb=elb,
                elbv2=elbv2,
                emr=emr,
                emrcontainers=emrcontainers,
                emrserverless=emrserverless,
                es=es,
                eventbridge=eventbridge,
                events=events,
                evidently=evidently,
                finspace=finspace,
                finspacedata=finspacedata,
                firehose=firehose,
                fis=fis,
                fms=fms,
                forecast=forecast,
                forecastquery=forecastquery,
                forecastqueryservice=forecastqueryservice,
                forecastservice=forecastservice,
                frauddetector=frauddetector,
                fsx=fsx,
                gamelift=gamelift,
                glacier=glacier,
                globalaccelerator=globalaccelerator,
                glue=glue,
                gluedatabrew=gluedatabrew,
                grafana=grafana,
                greengrass=greengrass,
                greengrassv2=greengrassv2,
                groundstation=groundstation,
                guardduty=guardduty,
                health=health,
                healthlake=healthlake,
                honeycode=honeycode,
                iam=iam,
                identitystore=identitystore,
                imagebuilder=imagebuilder,
                inspector=inspector,
                inspector2=inspector2,
                iot=iot,
                iot1clickdevices=iot1clickdevices,
                iot1clickdevicesservice=iot1clickdevicesservice,
                iot1clickprojects=iot1clickprojects,
                iotanalytics=iotanalytics,
                iotdata=iotdata,
                iotdataplane=iotdataplane,
                iotdeviceadvisor=iotdeviceadvisor,
                iotevents=iotevents,
                ioteventsdata=ioteventsdata,
                iotfleethub=iotfleethub,
                iotjobsdata=iotjobsdata,
                iotjobsdataplane=iotjobsdataplane,
                iotsecuretunneling=iotsecuretunneling,
                iotsitewise=iotsitewise,
                iotthingsgraph=iotthingsgraph,
                iottwinmaker=iottwinmaker,
                iotwireless=iotwireless,
                ivs=ivs,
                kafka=kafka,
                kafkaconnect=kafkaconnect,
                kendra=kendra,
                keyspaces=keyspaces,
                kinesis=kinesis,
                kinesisanalytics=kinesisanalytics,
                kinesisanalyticsv2=kinesisanalyticsv2,
                kinesisvideo=kinesisvideo,
                kinesisvideoarchivedmedia=kinesisvideoarchivedmedia,
                kinesisvideomedia=kinesisvideomedia,
                kinesisvideosignaling=kinesisvideosignaling,
                kinesisvideosignalingchannels=kinesisvideosignalingchannels,
                kms=kms,
                lakeformation=lakeformation,
                lambda_=lambda_,
                lex=lex,
                lexmodelbuilding=lexmodelbuilding,
                lexmodelbuildingservice=lexmodelbuildingservice,
                lexmodels=lexmodels,
                lexmodelsv2=lexmodelsv2,
                lexruntime=lexruntime,
                lexruntimeservice=lexruntimeservice,
                lexruntimev2=lexruntimev2,
                lexv2models=lexv2models,
                lexv2runtime=lexv2runtime,
                licensemanager=licensemanager,
                lightsail=lightsail,
                location=location,
                locationservice=locationservice,
                logs=logs,
                lookoutequipment=lookoutequipment,
                lookoutforvision=lookoutforvision,
                lookoutmetrics=lookoutmetrics,
                lookoutvision=lookoutvision,
                machinelearning=machinelearning,
                macie=macie,
                macie2=macie2,
                managedblockchain=managedblockchain,
                managedgrafana=managedgrafana,
                marketplacecatalog=marketplacecatalog,
                marketplacecommerceanalytics=marketplacecommerceanalytics,
                marketplaceentitlement=marketplaceentitlement,
                marketplaceentitlementservice=marketplaceentitlementservice,
                marketplacemetering=marketplacemetering,
                mediaconnect=mediaconnect,
                mediaconvert=mediaconvert,
                medialive=medialive,
                mediapackage=mediapackage,
                mediapackagevod=mediapackagevod,
                mediastore=mediastore,
                mediastoredata=mediastoredata,
                mediatailor=mediatailor,
                memorydb=memorydb,
                meteringmarketplace=meteringmarketplace,
                mgh=mgh,
                mgn=mgn,
                migrationhub=migrationhub,
                migrationhubconfig=migrationhubconfig,
                migrationhubrefactorspaces=migrationhubrefactorspaces,
                migrationhubstrategy=migrationhubstrategy,
                migrationhubstrategyrecommendations=migrationhubstrategyrecommendations,
                mobile=mobile,
                mq=mq,
                msk=msk,
                mturk=mturk,
                mwaa=mwaa,
                neptune=neptune,
                networkfirewall=networkfirewall,
                networkmanager=networkmanager,
                nimble=nimble,
                nimblestudio=nimblestudio,
                opensearch=opensearch,
                opensearchservice=opensearchservice,
                opsworks=opsworks,
                opsworkscm=opsworkscm,
                organizations=organizations,
                outposts=outposts,
                panorama=panorama,
                personalize=personalize,
                personalizeevents=personalizeevents,
                personalizeruntime=personalizeruntime,
                pi=pi,
                pinpoint=pinpoint,
                pinpointemail=pinpointemail,
                pinpointsmsvoice=pinpointsmsvoice,
                polly=polly,
                pricing=pricing,
                prometheus=prometheus,
                prometheusservice=prometheusservice,
                proton=proton,
                qldb=qldb,
                qldbsession=qldbsession,
                quicksight=quicksight,
                ram=ram,
                rbin=rbin,
                rds=rds,
                rdsdata=rdsdata,
                rdsdataservice=rdsdataservice,
                recyclebin=recyclebin,
                redshift=redshift,
                redshiftdata=redshiftdata,
                redshiftdataapiservice=redshiftdataapiservice,
                redshiftserverless=redshiftserverless,
                rekognition=rekognition,
                resiliencehub=resiliencehub,
                resourcegroups=resourcegroups,
                resourcegroupstagging=resourcegroupstagging,
                resourcegroupstaggingapi=resourcegroupstaggingapi,
                robomaker=robomaker,
                rolesanywhere=rolesanywhere,
                route53=route53,
                route53domains=route53domains,
                route53recoverycluster=route53recoverycluster,
                route53recoverycontrolconfig=route53recoverycontrolconfig,
                route53recoveryreadiness=route53recoveryreadiness,
                route53resolver=route53resolver,
                rum=rum,
                s3=s3,
                s3api=s3api,
                s3control=s3control,
                s3outposts=s3outposts,
                sagemaker=sagemaker,
                sagemakera2iruntime=sagemakera2iruntime,
                sagemakeredge=sagemakeredge,
                sagemakeredgemanager=sagemakeredgemanager,
                sagemakerfeaturestoreruntime=sagemakerfeaturestoreruntime,
                sagemakerruntime=sagemakerruntime,
                savingsplans=savingsplans,
                schemas=schemas,
                sdb=sdb,
                secretsmanager=secretsmanager,
                securityhub=securityhub,
                serverlessapplicationrepository=serverlessapplicationrepository,
                serverlessapprepo=serverlessapprepo,
                serverlessrepo=serverlessrepo,
                servicecatalog=servicecatalog,
                servicecatalogappregistry=servicecatalogappregistry,
                servicediscovery=servicediscovery,
                servicequotas=servicequotas,
                ses=ses,
                sesv2=sesv2,
                sfn=sfn,
                shield=shield,
                signer=signer,
                simpledb=simpledb,
                sms=sms,
                snowball=snowball,
                snowdevicemanagement=snowdevicemanagement,
                sns=sns,
                sqs=sqs,
                ssm=ssm,
                ssmcontacts=ssmcontacts,
                ssmincidents=ssmincidents,
                sso=sso,
                ssoadmin=ssoadmin,
                ssooidc=ssooidc,
                stepfunctions=stepfunctions,
                storagegateway=storagegateway,
                sts=sts,
                support=support,
                swf=swf,
                synthetics=synthetics,
                textract=textract,
                timestreamquery=timestreamquery,
                timestreamwrite=timestreamwrite,
                transcribe=transcribe,
                transcribeservice=transcribeservice,
                transcribestreaming=transcribestreaming,
                transcribestreamingservice=transcribestreamingservice,
                transfer=transfer,
                translate=translate,
                voiceid=voiceid,
                waf=waf,
                wafregional=wafregional,
                wafv2=wafv2,
                wellarchitected=wellarchitected,
                wisdom=wisdom,
                workdocs=workdocs,
                worklink=worklink,
                workmail=workmail,
                workmailmessageflow=workmailmessageflow,
                workspaces=workspaces,
                workspacesweb=workspacesweb,
                xray=xray,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accessanalyzer: str | core.StringOut | None = core.arg(default=None)

        account: str | core.StringOut | None = core.arg(default=None)

        acm: str | core.StringOut | None = core.arg(default=None)

        acmpca: str | core.StringOut | None = core.arg(default=None)

        alexaforbusiness: str | core.StringOut | None = core.arg(default=None)

        amg: str | core.StringOut | None = core.arg(default=None)

        amp: str | core.StringOut | None = core.arg(default=None)

        amplify: str | core.StringOut | None = core.arg(default=None)

        amplifybackend: str | core.StringOut | None = core.arg(default=None)

        amplifyuibuilder: str | core.StringOut | None = core.arg(default=None)

        apigateway: str | core.StringOut | None = core.arg(default=None)

        apigatewaymanagementapi: str | core.StringOut | None = core.arg(default=None)

        apigatewayv2: str | core.StringOut | None = core.arg(default=None)

        appautoscaling: str | core.StringOut | None = core.arg(default=None)

        appconfig: str | core.StringOut | None = core.arg(default=None)

        appconfigdata: str | core.StringOut | None = core.arg(default=None)

        appflow: str | core.StringOut | None = core.arg(default=None)

        appintegrations: str | core.StringOut | None = core.arg(default=None)

        appintegrationsservice: str | core.StringOut | None = core.arg(default=None)

        applicationautoscaling: str | core.StringOut | None = core.arg(default=None)

        applicationcostprofiler: str | core.StringOut | None = core.arg(default=None)

        applicationdiscovery: str | core.StringOut | None = core.arg(default=None)

        applicationdiscoveryservice: str | core.StringOut | None = core.arg(default=None)

        applicationinsights: str | core.StringOut | None = core.arg(default=None)

        appmesh: str | core.StringOut | None = core.arg(default=None)

        appregistry: str | core.StringOut | None = core.arg(default=None)

        apprunner: str | core.StringOut | None = core.arg(default=None)

        appstream: str | core.StringOut | None = core.arg(default=None)

        appsync: str | core.StringOut | None = core.arg(default=None)

        athena: str | core.StringOut | None = core.arg(default=None)

        auditmanager: str | core.StringOut | None = core.arg(default=None)

        augmentedairuntime: str | core.StringOut | None = core.arg(default=None)

        autoscaling: str | core.StringOut | None = core.arg(default=None)

        autoscalingplans: str | core.StringOut | None = core.arg(default=None)

        backup: str | core.StringOut | None = core.arg(default=None)

        backupgateway: str | core.StringOut | None = core.arg(default=None)

        batch: str | core.StringOut | None = core.arg(default=None)

        beanstalk: str | core.StringOut | None = core.arg(default=None)

        billingconductor: str | core.StringOut | None = core.arg(default=None)

        braket: str | core.StringOut | None = core.arg(default=None)

        budgets: str | core.StringOut | None = core.arg(default=None)

        ce: str | core.StringOut | None = core.arg(default=None)

        chime: str | core.StringOut | None = core.arg(default=None)

        chimesdkidentity: str | core.StringOut | None = core.arg(default=None)

        chimesdkmeetings: str | core.StringOut | None = core.arg(default=None)

        chimesdkmessaging: str | core.StringOut | None = core.arg(default=None)

        cloud9: str | core.StringOut | None = core.arg(default=None)

        cloudcontrol: str | core.StringOut | None = core.arg(default=None)

        cloudcontrolapi: str | core.StringOut | None = core.arg(default=None)

        clouddirectory: str | core.StringOut | None = core.arg(default=None)

        cloudformation: str | core.StringOut | None = core.arg(default=None)

        cloudfront: str | core.StringOut | None = core.arg(default=None)

        cloudhsm: str | core.StringOut | None = core.arg(default=None)

        cloudhsmv2: str | core.StringOut | None = core.arg(default=None)

        cloudsearch: str | core.StringOut | None = core.arg(default=None)

        cloudsearchdomain: str | core.StringOut | None = core.arg(default=None)

        cloudtrail: str | core.StringOut | None = core.arg(default=None)

        cloudwatch: str | core.StringOut | None = core.arg(default=None)

        cloudwatchevents: str | core.StringOut | None = core.arg(default=None)

        cloudwatchevidently: str | core.StringOut | None = core.arg(default=None)

        cloudwatchlog: str | core.StringOut | None = core.arg(default=None)

        cloudwatchlogs: str | core.StringOut | None = core.arg(default=None)

        cloudwatchrum: str | core.StringOut | None = core.arg(default=None)

        codeartifact: str | core.StringOut | None = core.arg(default=None)

        codebuild: str | core.StringOut | None = core.arg(default=None)

        codecommit: str | core.StringOut | None = core.arg(default=None)

        codedeploy: str | core.StringOut | None = core.arg(default=None)

        codeguruprofiler: str | core.StringOut | None = core.arg(default=None)

        codegurureviewer: str | core.StringOut | None = core.arg(default=None)

        codepipeline: str | core.StringOut | None = core.arg(default=None)

        codestar: str | core.StringOut | None = core.arg(default=None)

        codestarconnections: str | core.StringOut | None = core.arg(default=None)

        codestarnotifications: str | core.StringOut | None = core.arg(default=None)

        cognitoidentity: str | core.StringOut | None = core.arg(default=None)

        cognitoidentityprovider: str | core.StringOut | None = core.arg(default=None)

        cognitoidp: str | core.StringOut | None = core.arg(default=None)

        cognitosync: str | core.StringOut | None = core.arg(default=None)

        comprehend: str | core.StringOut | None = core.arg(default=None)

        comprehendmedical: str | core.StringOut | None = core.arg(default=None)

        computeoptimizer: str | core.StringOut | None = core.arg(default=None)

        config: str | core.StringOut | None = core.arg(default=None)

        configservice: str | core.StringOut | None = core.arg(default=None)

        connect: str | core.StringOut | None = core.arg(default=None)

        connectcontactlens: str | core.StringOut | None = core.arg(default=None)

        connectparticipant: str | core.StringOut | None = core.arg(default=None)

        connectwisdomservice: str | core.StringOut | None = core.arg(default=None)

        costandusagereportservice: str | core.StringOut | None = core.arg(default=None)

        costexplorer: str | core.StringOut | None = core.arg(default=None)

        cur: str | core.StringOut | None = core.arg(default=None)

        customerprofiles: str | core.StringOut | None = core.arg(default=None)

        databasemigration: str | core.StringOut | None = core.arg(default=None)

        databasemigrationservice: str | core.StringOut | None = core.arg(default=None)

        databrew: str | core.StringOut | None = core.arg(default=None)

        dataexchange: str | core.StringOut | None = core.arg(default=None)

        datapipeline: str | core.StringOut | None = core.arg(default=None)

        datasync: str | core.StringOut | None = core.arg(default=None)

        dax: str | core.StringOut | None = core.arg(default=None)

        deploy: str | core.StringOut | None = core.arg(default=None)

        detective: str | core.StringOut | None = core.arg(default=None)

        devicefarm: str | core.StringOut | None = core.arg(default=None)

        devopsguru: str | core.StringOut | None = core.arg(default=None)

        directconnect: str | core.StringOut | None = core.arg(default=None)

        directoryservice: str | core.StringOut | None = core.arg(default=None)

        discovery: str | core.StringOut | None = core.arg(default=None)

        dlm: str | core.StringOut | None = core.arg(default=None)

        dms: str | core.StringOut | None = core.arg(default=None)

        docdb: str | core.StringOut | None = core.arg(default=None)

        drs: str | core.StringOut | None = core.arg(default=None)

        ds: str | core.StringOut | None = core.arg(default=None)

        dynamodb: str | core.StringOut | None = core.arg(default=None)

        dynamodbstreams: str | core.StringOut | None = core.arg(default=None)

        ebs: str | core.StringOut | None = core.arg(default=None)

        ec2: str | core.StringOut | None = core.arg(default=None)

        ec2instanceconnect: str | core.StringOut | None = core.arg(default=None)

        ecr: str | core.StringOut | None = core.arg(default=None)

        ecrpublic: str | core.StringOut | None = core.arg(default=None)

        ecs: str | core.StringOut | None = core.arg(default=None)

        efs: str | core.StringOut | None = core.arg(default=None)

        eks: str | core.StringOut | None = core.arg(default=None)

        elasticache: str | core.StringOut | None = core.arg(default=None)

        elasticbeanstalk: str | core.StringOut | None = core.arg(default=None)

        elasticinference: str | core.StringOut | None = core.arg(default=None)

        elasticloadbalancing: str | core.StringOut | None = core.arg(default=None)

        elasticloadbalancingv2: str | core.StringOut | None = core.arg(default=None)

        elasticsearch: str | core.StringOut | None = core.arg(default=None)

        elasticsearchservice: str | core.StringOut | None = core.arg(default=None)

        elastictranscoder: str | core.StringOut | None = core.arg(default=None)

        elb: str | core.StringOut | None = core.arg(default=None)

        elbv2: str | core.StringOut | None = core.arg(default=None)

        emr: str | core.StringOut | None = core.arg(default=None)

        emrcontainers: str | core.StringOut | None = core.arg(default=None)

        emrserverless: str | core.StringOut | None = core.arg(default=None)

        es: str | core.StringOut | None = core.arg(default=None)

        eventbridge: str | core.StringOut | None = core.arg(default=None)

        events: str | core.StringOut | None = core.arg(default=None)

        evidently: str | core.StringOut | None = core.arg(default=None)

        finspace: str | core.StringOut | None = core.arg(default=None)

        finspacedata: str | core.StringOut | None = core.arg(default=None)

        firehose: str | core.StringOut | None = core.arg(default=None)

        fis: str | core.StringOut | None = core.arg(default=None)

        fms: str | core.StringOut | None = core.arg(default=None)

        forecast: str | core.StringOut | None = core.arg(default=None)

        forecastquery: str | core.StringOut | None = core.arg(default=None)

        forecastqueryservice: str | core.StringOut | None = core.arg(default=None)

        forecastservice: str | core.StringOut | None = core.arg(default=None)

        frauddetector: str | core.StringOut | None = core.arg(default=None)

        fsx: str | core.StringOut | None = core.arg(default=None)

        gamelift: str | core.StringOut | None = core.arg(default=None)

        glacier: str | core.StringOut | None = core.arg(default=None)

        globalaccelerator: str | core.StringOut | None = core.arg(default=None)

        glue: str | core.StringOut | None = core.arg(default=None)

        gluedatabrew: str | core.StringOut | None = core.arg(default=None)

        grafana: str | core.StringOut | None = core.arg(default=None)

        greengrass: str | core.StringOut | None = core.arg(default=None)

        greengrassv2: str | core.StringOut | None = core.arg(default=None)

        groundstation: str | core.StringOut | None = core.arg(default=None)

        guardduty: str | core.StringOut | None = core.arg(default=None)

        health: str | core.StringOut | None = core.arg(default=None)

        healthlake: str | core.StringOut | None = core.arg(default=None)

        honeycode: str | core.StringOut | None = core.arg(default=None)

        iam: str | core.StringOut | None = core.arg(default=None)

        identitystore: str | core.StringOut | None = core.arg(default=None)

        imagebuilder: str | core.StringOut | None = core.arg(default=None)

        inspector: str | core.StringOut | None = core.arg(default=None)

        inspector2: str | core.StringOut | None = core.arg(default=None)

        iot: str | core.StringOut | None = core.arg(default=None)

        iot1clickdevices: str | core.StringOut | None = core.arg(default=None)

        iot1clickdevicesservice: str | core.StringOut | None = core.arg(default=None)

        iot1clickprojects: str | core.StringOut | None = core.arg(default=None)

        iotanalytics: str | core.StringOut | None = core.arg(default=None)

        iotdata: str | core.StringOut | None = core.arg(default=None)

        iotdataplane: str | core.StringOut | None = core.arg(default=None)

        iotdeviceadvisor: str | core.StringOut | None = core.arg(default=None)

        iotevents: str | core.StringOut | None = core.arg(default=None)

        ioteventsdata: str | core.StringOut | None = core.arg(default=None)

        iotfleethub: str | core.StringOut | None = core.arg(default=None)

        iotjobsdata: str | core.StringOut | None = core.arg(default=None)

        iotjobsdataplane: str | core.StringOut | None = core.arg(default=None)

        iotsecuretunneling: str | core.StringOut | None = core.arg(default=None)

        iotsitewise: str | core.StringOut | None = core.arg(default=None)

        iotthingsgraph: str | core.StringOut | None = core.arg(default=None)

        iottwinmaker: str | core.StringOut | None = core.arg(default=None)

        iotwireless: str | core.StringOut | None = core.arg(default=None)

        ivs: str | core.StringOut | None = core.arg(default=None)

        kafka: str | core.StringOut | None = core.arg(default=None)

        kafkaconnect: str | core.StringOut | None = core.arg(default=None)

        kendra: str | core.StringOut | None = core.arg(default=None)

        keyspaces: str | core.StringOut | None = core.arg(default=None)

        kinesis: str | core.StringOut | None = core.arg(default=None)

        kinesisanalytics: str | core.StringOut | None = core.arg(default=None)

        kinesisanalyticsv2: str | core.StringOut | None = core.arg(default=None)

        kinesisvideo: str | core.StringOut | None = core.arg(default=None)

        kinesisvideoarchivedmedia: str | core.StringOut | None = core.arg(default=None)

        kinesisvideomedia: str | core.StringOut | None = core.arg(default=None)

        kinesisvideosignaling: str | core.StringOut | None = core.arg(default=None)

        kinesisvideosignalingchannels: str | core.StringOut | None = core.arg(default=None)

        kms: str | core.StringOut | None = core.arg(default=None)

        lakeformation: str | core.StringOut | None = core.arg(default=None)

        lambda_: str | core.StringOut | None = core.arg(default=None)

        lex: str | core.StringOut | None = core.arg(default=None)

        lexmodelbuilding: str | core.StringOut | None = core.arg(default=None)

        lexmodelbuildingservice: str | core.StringOut | None = core.arg(default=None)

        lexmodels: str | core.StringOut | None = core.arg(default=None)

        lexmodelsv2: str | core.StringOut | None = core.arg(default=None)

        lexruntime: str | core.StringOut | None = core.arg(default=None)

        lexruntimeservice: str | core.StringOut | None = core.arg(default=None)

        lexruntimev2: str | core.StringOut | None = core.arg(default=None)

        lexv2models: str | core.StringOut | None = core.arg(default=None)

        lexv2runtime: str | core.StringOut | None = core.arg(default=None)

        licensemanager: str | core.StringOut | None = core.arg(default=None)

        lightsail: str | core.StringOut | None = core.arg(default=None)

        location: str | core.StringOut | None = core.arg(default=None)

        locationservice: str | core.StringOut | None = core.arg(default=None)

        logs: str | core.StringOut | None = core.arg(default=None)

        lookoutequipment: str | core.StringOut | None = core.arg(default=None)

        lookoutforvision: str | core.StringOut | None = core.arg(default=None)

        lookoutmetrics: str | core.StringOut | None = core.arg(default=None)

        lookoutvision: str | core.StringOut | None = core.arg(default=None)

        machinelearning: str | core.StringOut | None = core.arg(default=None)

        macie: str | core.StringOut | None = core.arg(default=None)

        macie2: str | core.StringOut | None = core.arg(default=None)

        managedblockchain: str | core.StringOut | None = core.arg(default=None)

        managedgrafana: str | core.StringOut | None = core.arg(default=None)

        marketplacecatalog: str | core.StringOut | None = core.arg(default=None)

        marketplacecommerceanalytics: str | core.StringOut | None = core.arg(default=None)

        marketplaceentitlement: str | core.StringOut | None = core.arg(default=None)

        marketplaceentitlementservice: str | core.StringOut | None = core.arg(default=None)

        marketplacemetering: str | core.StringOut | None = core.arg(default=None)

        mediaconnect: str | core.StringOut | None = core.arg(default=None)

        mediaconvert: str | core.StringOut | None = core.arg(default=None)

        medialive: str | core.StringOut | None = core.arg(default=None)

        mediapackage: str | core.StringOut | None = core.arg(default=None)

        mediapackagevod: str | core.StringOut | None = core.arg(default=None)

        mediastore: str | core.StringOut | None = core.arg(default=None)

        mediastoredata: str | core.StringOut | None = core.arg(default=None)

        mediatailor: str | core.StringOut | None = core.arg(default=None)

        memorydb: str | core.StringOut | None = core.arg(default=None)

        meteringmarketplace: str | core.StringOut | None = core.arg(default=None)

        mgh: str | core.StringOut | None = core.arg(default=None)

        mgn: str | core.StringOut | None = core.arg(default=None)

        migrationhub: str | core.StringOut | None = core.arg(default=None)

        migrationhubconfig: str | core.StringOut | None = core.arg(default=None)

        migrationhubrefactorspaces: str | core.StringOut | None = core.arg(default=None)

        migrationhubstrategy: str | core.StringOut | None = core.arg(default=None)

        migrationhubstrategyrecommendations: str | core.StringOut | None = core.arg(default=None)

        mobile: str | core.StringOut | None = core.arg(default=None)

        mq: str | core.StringOut | None = core.arg(default=None)

        msk: str | core.StringOut | None = core.arg(default=None)

        mturk: str | core.StringOut | None = core.arg(default=None)

        mwaa: str | core.StringOut | None = core.arg(default=None)

        neptune: str | core.StringOut | None = core.arg(default=None)

        networkfirewall: str | core.StringOut | None = core.arg(default=None)

        networkmanager: str | core.StringOut | None = core.arg(default=None)

        nimble: str | core.StringOut | None = core.arg(default=None)

        nimblestudio: str | core.StringOut | None = core.arg(default=None)

        opensearch: str | core.StringOut | None = core.arg(default=None)

        opensearchservice: str | core.StringOut | None = core.arg(default=None)

        opsworks: str | core.StringOut | None = core.arg(default=None)

        opsworkscm: str | core.StringOut | None = core.arg(default=None)

        organizations: str | core.StringOut | None = core.arg(default=None)

        outposts: str | core.StringOut | None = core.arg(default=None)

        panorama: str | core.StringOut | None = core.arg(default=None)

        personalize: str | core.StringOut | None = core.arg(default=None)

        personalizeevents: str | core.StringOut | None = core.arg(default=None)

        personalizeruntime: str | core.StringOut | None = core.arg(default=None)

        pi: str | core.StringOut | None = core.arg(default=None)

        pinpoint: str | core.StringOut | None = core.arg(default=None)

        pinpointemail: str | core.StringOut | None = core.arg(default=None)

        pinpointsmsvoice: str | core.StringOut | None = core.arg(default=None)

        polly: str | core.StringOut | None = core.arg(default=None)

        pricing: str | core.StringOut | None = core.arg(default=None)

        prometheus: str | core.StringOut | None = core.arg(default=None)

        prometheusservice: str | core.StringOut | None = core.arg(default=None)

        proton: str | core.StringOut | None = core.arg(default=None)

        qldb: str | core.StringOut | None = core.arg(default=None)

        qldbsession: str | core.StringOut | None = core.arg(default=None)

        quicksight: str | core.StringOut | None = core.arg(default=None)

        ram: str | core.StringOut | None = core.arg(default=None)

        rbin: str | core.StringOut | None = core.arg(default=None)

        rds: str | core.StringOut | None = core.arg(default=None)

        rdsdata: str | core.StringOut | None = core.arg(default=None)

        rdsdataservice: str | core.StringOut | None = core.arg(default=None)

        recyclebin: str | core.StringOut | None = core.arg(default=None)

        redshift: str | core.StringOut | None = core.arg(default=None)

        redshiftdata: str | core.StringOut | None = core.arg(default=None)

        redshiftdataapiservice: str | core.StringOut | None = core.arg(default=None)

        redshiftserverless: str | core.StringOut | None = core.arg(default=None)

        rekognition: str | core.StringOut | None = core.arg(default=None)

        resiliencehub: str | core.StringOut | None = core.arg(default=None)

        resourcegroups: str | core.StringOut | None = core.arg(default=None)

        resourcegroupstagging: str | core.StringOut | None = core.arg(default=None)

        resourcegroupstaggingapi: str | core.StringOut | None = core.arg(default=None)

        robomaker: str | core.StringOut | None = core.arg(default=None)

        rolesanywhere: str | core.StringOut | None = core.arg(default=None)

        route53: str | core.StringOut | None = core.arg(default=None)

        route53domains: str | core.StringOut | None = core.arg(default=None)

        route53recoverycluster: str | core.StringOut | None = core.arg(default=None)

        route53recoverycontrolconfig: str | core.StringOut | None = core.arg(default=None)

        route53recoveryreadiness: str | core.StringOut | None = core.arg(default=None)

        route53resolver: str | core.StringOut | None = core.arg(default=None)

        rum: str | core.StringOut | None = core.arg(default=None)

        s3: str | core.StringOut | None = core.arg(default=None)

        s3api: str | core.StringOut | None = core.arg(default=None)

        s3control: str | core.StringOut | None = core.arg(default=None)

        s3outposts: str | core.StringOut | None = core.arg(default=None)

        sagemaker: str | core.StringOut | None = core.arg(default=None)

        sagemakera2iruntime: str | core.StringOut | None = core.arg(default=None)

        sagemakeredge: str | core.StringOut | None = core.arg(default=None)

        sagemakeredgemanager: str | core.StringOut | None = core.arg(default=None)

        sagemakerfeaturestoreruntime: str | core.StringOut | None = core.arg(default=None)

        sagemakerruntime: str | core.StringOut | None = core.arg(default=None)

        savingsplans: str | core.StringOut | None = core.arg(default=None)

        schemas: str | core.StringOut | None = core.arg(default=None)

        sdb: str | core.StringOut | None = core.arg(default=None)

        secretsmanager: str | core.StringOut | None = core.arg(default=None)

        securityhub: str | core.StringOut | None = core.arg(default=None)

        serverlessapplicationrepository: str | core.StringOut | None = core.arg(default=None)

        serverlessapprepo: str | core.StringOut | None = core.arg(default=None)

        serverlessrepo: str | core.StringOut | None = core.arg(default=None)

        servicecatalog: str | core.StringOut | None = core.arg(default=None)

        servicecatalogappregistry: str | core.StringOut | None = core.arg(default=None)

        servicediscovery: str | core.StringOut | None = core.arg(default=None)

        servicequotas: str | core.StringOut | None = core.arg(default=None)

        ses: str | core.StringOut | None = core.arg(default=None)

        sesv2: str | core.StringOut | None = core.arg(default=None)

        sfn: str | core.StringOut | None = core.arg(default=None)

        shield: str | core.StringOut | None = core.arg(default=None)

        signer: str | core.StringOut | None = core.arg(default=None)

        simpledb: str | core.StringOut | None = core.arg(default=None)

        sms: str | core.StringOut | None = core.arg(default=None)

        snowball: str | core.StringOut | None = core.arg(default=None)

        snowdevicemanagement: str | core.StringOut | None = core.arg(default=None)

        sns: str | core.StringOut | None = core.arg(default=None)

        sqs: str | core.StringOut | None = core.arg(default=None)

        ssm: str | core.StringOut | None = core.arg(default=None)

        ssmcontacts: str | core.StringOut | None = core.arg(default=None)

        ssmincidents: str | core.StringOut | None = core.arg(default=None)

        sso: str | core.StringOut | None = core.arg(default=None)

        ssoadmin: str | core.StringOut | None = core.arg(default=None)

        ssooidc: str | core.StringOut | None = core.arg(default=None)

        stepfunctions: str | core.StringOut | None = core.arg(default=None)

        storagegateway: str | core.StringOut | None = core.arg(default=None)

        sts: str | core.StringOut | None = core.arg(default=None)

        support: str | core.StringOut | None = core.arg(default=None)

        swf: str | core.StringOut | None = core.arg(default=None)

        synthetics: str | core.StringOut | None = core.arg(default=None)

        textract: str | core.StringOut | None = core.arg(default=None)

        timestreamquery: str | core.StringOut | None = core.arg(default=None)

        timestreamwrite: str | core.StringOut | None = core.arg(default=None)

        transcribe: str | core.StringOut | None = core.arg(default=None)

        transcribeservice: str | core.StringOut | None = core.arg(default=None)

        transcribestreaming: str | core.StringOut | None = core.arg(default=None)

        transcribestreamingservice: str | core.StringOut | None = core.arg(default=None)

        transfer: str | core.StringOut | None = core.arg(default=None)

        translate: str | core.StringOut | None = core.arg(default=None)

        voiceid: str | core.StringOut | None = core.arg(default=None)

        waf: str | core.StringOut | None = core.arg(default=None)

        wafregional: str | core.StringOut | None = core.arg(default=None)

        wafv2: str | core.StringOut | None = core.arg(default=None)

        wellarchitected: str | core.StringOut | None = core.arg(default=None)

        wisdom: str | core.StringOut | None = core.arg(default=None)

        workdocs: str | core.StringOut | None = core.arg(default=None)

        worklink: str | core.StringOut | None = core.arg(default=None)

        workmail: str | core.StringOut | None = core.arg(default=None)

        workmailmessageflow: str | core.StringOut | None = core.arg(default=None)

        workspaces: str | core.StringOut | None = core.arg(default=None)

        workspacesweb: str | core.StringOut | None = core.arg(default=None)

        xray: str | core.StringOut | None = core.arg(default=None)


@core.schema
class IgnoreTags(core.Schema):

    key_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = None,
        keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=IgnoreTags.Args(
                key_prefixes=key_prefixes,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_prefixes: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)


@core.schema
class AssumeRoleWithWebIdentity(core.Schema):

    duration: str | core.StringOut | None = core.attr(str, default=None)

    policy: str | core.StringOut | None = core.attr(str, default=None)

    policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    session_name: str | core.StringOut | None = core.attr(str, default=None)

    web_identity_token: str | core.StringOut | None = core.attr(str, default=None)

    web_identity_token_file: str | core.StringOut | None = core.attr(str, default=None)

    def __init__(
        self,
        *,
        duration: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        role_arn: str | core.StringOut | None = None,
        session_name: str | core.StringOut | None = None,
        web_identity_token: str | core.StringOut | None = None,
        web_identity_token_file: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=AssumeRoleWithWebIdentity.Args(
                duration=duration,
                policy=policy,
                policy_arns=policy_arns,
                role_arn=role_arn,
                session_name=session_name,
                web_identity_token=web_identity_token,
                web_identity_token_file=web_identity_token_file,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        session_name: str | core.StringOut | None = core.arg(default=None)

        web_identity_token: str | core.StringOut | None = core.arg(default=None)

        web_identity_token_file: str | core.StringOut | None = core.arg(default=None)


@core.schema
class AssumeRole(core.Schema):

    duration: str | core.StringOut | None = core.attr(str, default=None)

    duration_seconds: int | core.IntOut | None = core.attr(int, default=None)

    external_id: str | core.StringOut | None = core.attr(str, default=None)

    policy: str | core.StringOut | None = core.attr(str, default=None)

    policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    role_arn: str | core.StringOut | None = core.attr(str, default=None)

    session_name: str | core.StringOut | None = core.attr(str, default=None)

    tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.map
    )

    transitive_tag_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        duration: str | core.StringOut | None = None,
        duration_seconds: int | core.IntOut | None = None,
        external_id: str | core.StringOut | None = None,
        policy: str | core.StringOut | None = None,
        policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = None,
        role_arn: str | core.StringOut | None = None,
        session_name: str | core.StringOut | None = None,
        tags: dict[str, str] | core.MapOut[core.StringOut] | None = None,
        transitive_tag_keys: list[str] | core.ArrayOut[core.StringOut] | None = None,
    ):
        super().__init__(
            args=AssumeRole.Args(
                duration=duration,
                duration_seconds=duration_seconds,
                external_id=external_id,
                policy=policy,
                policy_arns=policy_arns,
                role_arn=role_arn,
                session_name=session_name,
                tags=tags,
                transitive_tag_keys=transitive_tag_keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration: str | core.StringOut | None = core.arg(default=None)

        duration_seconds: int | core.IntOut | None = core.arg(default=None)

        external_id: str | core.StringOut | None = core.arg(default=None)

        policy: str | core.StringOut | None = core.arg(default=None)

        policy_arns: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(default=None)

        role_arn: str | core.StringOut | None = core.arg(default=None)

        session_name: str | core.StringOut | None = core.arg(default=None)

        tags: dict[str, str] | core.MapOut[core.StringOut] | None = core.arg(default=None)

        transitive_tag_keys: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )


@core.provider(name="aws")
class Provider(core.Provider):

    access_key: str | core.StringOut | None = core.attr(str, default=None)

    allowed_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    assume_role: AssumeRole | None = core.attr(AssumeRole, default=None)

    assume_role_with_web_identity: AssumeRoleWithWebIdentity | None = core.attr(
        AssumeRoleWithWebIdentity, default=None
    )

    custom_ca_bundle: str | core.StringOut | None = core.attr(str, default=None)

    default_tags: DefaultTags | None = core.attr(DefaultTags, default=None)

    ec2_metadata_service_endpoint: str | core.StringOut | None = core.attr(str, default=None)

    ec2_metadata_service_endpoint_mode: str | core.StringOut | None = core.attr(str, default=None)

    endpoints: list[Endpoints] | core.ArrayOut[Endpoints] | None = core.attr(
        Endpoints, default=None, kind=core.Kind.array
    )

    forbidden_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    http_proxy: str | core.StringOut | None = core.attr(str, default=None)

    ignore_tags: IgnoreTags | None = core.attr(IgnoreTags, default=None)

    insecure: bool | core.BoolOut | None = core.attr(bool, default=None)

    max_retries: int | core.IntOut | None = core.attr(int, default=None)

    profile: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    s3_force_path_style: bool | core.BoolOut | None = core.attr(bool, default=None)

    s3_use_path_style: bool | core.BoolOut | None = core.attr(bool, default=None)

    secret_key: str | core.StringOut | None = core.attr(str, default=None)

    shared_config_files: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    shared_credentials_file: str | core.StringOut | None = core.attr(str, default=None)

    shared_credentials_files: list[str] | core.ArrayOut[core.StringOut] | None = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skip_credentials_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    skip_get_ec2_platforms: bool | core.BoolOut | None = core.attr(bool, default=None)

    skip_metadata_api_check: str | core.StringOut | None = core.attr(str, default=None)

    skip_region_validation: bool | core.BoolOut | None = core.attr(bool, default=None)

    skip_requesting_account_id: bool | core.BoolOut | None = core.attr(bool, default=None)

    sts_region: str | core.StringOut | None = core.attr(str, default=None)

    token: str | core.StringOut | None = core.attr(str, default=None)

    use_dualstack_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    use_fips_endpoint: bool | core.BoolOut | None = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        access_key: str | core.StringOut | None = None,
        allowed_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        assume_role: AssumeRole | None = None,
        assume_role_with_web_identity: AssumeRoleWithWebIdentity | None = None,
        custom_ca_bundle: str | core.StringOut | None = None,
        default_tags: DefaultTags | None = None,
        ec2_metadata_service_endpoint: str | core.StringOut | None = None,
        ec2_metadata_service_endpoint_mode: str | core.StringOut | None = None,
        endpoints: list[Endpoints] | core.ArrayOut[Endpoints] | None = None,
        forbidden_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = None,
        http_proxy: str | core.StringOut | None = None,
        ignore_tags: IgnoreTags | None = None,
        insecure: bool | core.BoolOut | None = None,
        max_retries: int | core.IntOut | None = None,
        profile: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
        s3_force_path_style: bool | core.BoolOut | None = None,
        s3_use_path_style: bool | core.BoolOut | None = None,
        secret_key: str | core.StringOut | None = None,
        shared_config_files: list[str] | core.ArrayOut[core.StringOut] | None = None,
        shared_credentials_file: str | core.StringOut | None = None,
        shared_credentials_files: list[str] | core.ArrayOut[core.StringOut] | None = None,
        skip_credentials_validation: bool | core.BoolOut | None = None,
        skip_get_ec2_platforms: bool | core.BoolOut | None = None,
        skip_metadata_api_check: str | core.StringOut | None = None,
        skip_region_validation: bool | core.BoolOut | None = None,
        skip_requesting_account_id: bool | core.BoolOut | None = None,
        sts_region: str | core.StringOut | None = None,
        token: str | core.StringOut | None = None,
        use_dualstack_endpoint: bool | core.BoolOut | None = None,
        use_fips_endpoint: bool | core.BoolOut | None = None,
        alias: str | core.StringOut | None = None,
        version: str | core.StringOut | None = None,
    ):
        super().__init__(
            args=Provider.Args(
                access_key=access_key,
                allowed_account_ids=allowed_account_ids,
                assume_role=assume_role,
                assume_role_with_web_identity=assume_role_with_web_identity,
                custom_ca_bundle=custom_ca_bundle,
                default_tags=default_tags,
                ec2_metadata_service_endpoint=ec2_metadata_service_endpoint,
                ec2_metadata_service_endpoint_mode=ec2_metadata_service_endpoint_mode,
                endpoints=endpoints,
                forbidden_account_ids=forbidden_account_ids,
                http_proxy=http_proxy,
                ignore_tags=ignore_tags,
                insecure=insecure,
                max_retries=max_retries,
                profile=profile,
                region=region,
                s3_force_path_style=s3_force_path_style,
                s3_use_path_style=s3_use_path_style,
                secret_key=secret_key,
                shared_config_files=shared_config_files,
                shared_credentials_file=shared_credentials_file,
                shared_credentials_files=shared_credentials_files,
                skip_credentials_validation=skip_credentials_validation,
                skip_get_ec2_platforms=skip_get_ec2_platforms,
                skip_metadata_api_check=skip_metadata_api_check,
                skip_region_validation=skip_region_validation,
                skip_requesting_account_id=skip_requesting_account_id,
                sts_region=sts_region,
                token=token,
                use_dualstack_endpoint=use_dualstack_endpoint,
                use_fips_endpoint=use_fips_endpoint,
                alias=alias,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.Provider.Args):
        access_key: str | core.StringOut | None = core.arg(default=None)

        allowed_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        assume_role: AssumeRole | None = core.arg(default=None)

        assume_role_with_web_identity: AssumeRoleWithWebIdentity | None = core.arg(default=None)

        custom_ca_bundle: str | core.StringOut | None = core.arg(default=None)

        default_tags: DefaultTags | None = core.arg(default=None)

        ec2_metadata_service_endpoint: str | core.StringOut | None = core.arg(default=None)

        ec2_metadata_service_endpoint_mode: str | core.StringOut | None = core.arg(default=None)

        endpoints: list[Endpoints] | core.ArrayOut[Endpoints] | None = core.arg(default=None)

        forbidden_account_ids: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        http_proxy: str | core.StringOut | None = core.arg(default=None)

        ignore_tags: IgnoreTags | None = core.arg(default=None)

        insecure: bool | core.BoolOut | None = core.arg(default=None)

        max_retries: int | core.IntOut | None = core.arg(default=None)

        profile: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        s3_force_path_style: bool | core.BoolOut | None = core.arg(default=None)

        s3_use_path_style: bool | core.BoolOut | None = core.arg(default=None)

        secret_key: str | core.StringOut | None = core.arg(default=None)

        shared_config_files: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        shared_credentials_file: str | core.StringOut | None = core.arg(default=None)

        shared_credentials_files: list[str] | core.ArrayOut[core.StringOut] | None = core.arg(
            default=None
        )

        skip_credentials_validation: bool | core.BoolOut | None = core.arg(default=None)

        skip_get_ec2_platforms: bool | core.BoolOut | None = core.arg(default=None)

        skip_metadata_api_check: str | core.StringOut | None = core.arg(default=None)

        skip_region_validation: bool | core.BoolOut | None = core.arg(default=None)

        skip_requesting_account_id: bool | core.BoolOut | None = core.arg(default=None)

        sts_region: str | core.StringOut | None = core.arg(default=None)

        token: str | core.StringOut | None = core.arg(default=None)

        use_dualstack_endpoint: bool | core.BoolOut | None = core.arg(default=None)

        use_fips_endpoint: bool | core.BoolOut | None = core.arg(default=None)
