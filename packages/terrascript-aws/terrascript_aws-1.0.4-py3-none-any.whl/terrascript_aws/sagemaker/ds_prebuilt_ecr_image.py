import terrascript.core as core


@core.data(type="aws_sagemaker_prebuilt_ecr_image", namespace="sagemaker")
class DsPrebuiltEcrImage(core.Data):
    """
    (Optional) The DNS suffix to use in the registry path. If not specified, the AWS provider sets it to
    the DNS suffix for the current region.
    """

    dns_suffix: str | core.StringOut | None = core.attr(str, default=None)

    id: str | core.StringOut = core.attr(str, computed=True)

    """
    (Optional) The image tag for the Docker image. If not specified, the AWS provider sets the value to
    1`, which for many repositories indicates the latest version. Some repositories, such as XGBoost, d
    o not support `1` or `latest` and specific version must be used.
    """
    image_tag: str | core.StringOut | None = core.attr(str, default=None)

    region: str | core.StringOut | None = core.attr(str, default=None)

    """
    The account ID containing the image. For example, `469771592824`.
    """
    registry_id: str | core.StringOut = core.attr(str, computed=True)

    """
    The Docker image URL. For example, `341280168497.dkr.ecr.ca-central-1.amazonaws.com/sagemaker-sparkm
    l-serving:2.4`.
    """
    registry_path: str | core.StringOut = core.attr(str, computed=True)

    """
    (Required) The name of the repository, which is generally the algorithm or library. Values include `
    blazingtext`, `factorization-machines`, `forecasting-deepar`, `image-classification`, `ipinsights`,
    kmeans`, `knn`, `lda`, `linear-learner`, `mxnet-inference-eia`, `mxnet-inference`, `mxnet-training`
    , `ntm`, `object-detection`, `object2vec`, `pca`, `pytorch-inference-eia`, `pytorch-inference`, `pyt
    orch-training`, `randomcutforest`, `sagemaker-scikit-learn`, `sagemaker-sparkml-serving`, `sagemaker
    xgboost`, `semantic-segmentation`, `seq2seq`, `tensorflow-inference-eia`, `tensorflow-inference`, `
    tensorflow-training`, `huggingface-tensorflow-training`, `huggingface-tensorflow-inference`, `huggin
    gface-pytorch-training`, and `huggingface-pytorch-inference`.
    """
    repository_name: str | core.StringOut = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        repository_name: str | core.StringOut,
        dns_suffix: str | core.StringOut | None = None,
        image_tag: str | core.StringOut | None = None,
        region: str | core.StringOut | None = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPrebuiltEcrImage.Args(
                repository_name=repository_name,
                dns_suffix=dns_suffix,
                image_tag=image_tag,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_suffix: str | core.StringOut | None = core.arg(default=None)

        image_tag: str | core.StringOut | None = core.arg(default=None)

        region: str | core.StringOut | None = core.arg(default=None)

        repository_name: str | core.StringOut = core.arg()
