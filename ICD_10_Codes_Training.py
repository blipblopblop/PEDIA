from pyspark.sql import functions as F  # noqa: None: None
from pyspark.sql import DataFrame
from transforms.api import transform, Input, Output
from myproject.datasets import utils


def compute(source_df: DataFrame) -> DataFrame:
    return utils.identity(source_df)


# NOTE: Libraries must be manually imported through "Libraries" in the left-hand panel


from language_model_service_api.languagemodelservice_api_embeddings_v3 import (  # noqa: E402
    GenericEmbeddingsRequest,
)
from palantir_models.models import GenericEmbeddingModel  # noqa: E402
from palantir_models.transforms import GenericEmbeddingModelInput  # noqa: E402
from pyspark.sql.types import ArrayType, FloatType  # noqa: E402

@transform(
    output=Output("ri.foundry.main.dataset.2a07fb3b-6cee-42c7-a6eb-39bb98856f4d"),
    reviews=Input("ri.foundry.main.dataset.96ac7562-0f0d-4f2e-a870-bbd5b8eda7ff"),
    embedding_model=GenericEmbeddingModelInput(
        "ri.language-model-service..language-model.text-embedding-ada-002_azure"
    )
)
def compute_embeddings(ctx, reviews, embedding_model: GenericEmbeddingModel, output):
    def create_embeddings(val):
        return embedding_model.create_embeddings(
            GenericEmbeddingsRequest(inputs=[val])
        ).embeddings[0]

    create_embeddings_udf = F.udf(create_embeddings, ArrayType(FloatType()))

    out_df = reviews.dataframe().withColumn("embedding", create_embeddings_udf(F.col("description"))) 
    output.write_dataframe(out_df)
    return out_df