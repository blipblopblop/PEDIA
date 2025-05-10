from pyspark.sql import functions as F  # noqa: None: None
from pyspark.sql import DataFrame
from transforms.api import transform, Input, Output
from myproject.datasets import utils

# Using the text-embedding-ada-002 model to create embeddings for the pediatric patient notes 
# using the Azure OpenAI service and the language-model-service   
# The patient notes are from the Pediatric_Notes dataset that is extracted from the PMC_Patients_cleaned.csv file with patients from the age of 0 to 10

def compute(source_df: DataFrame) -> DataFrame:
    return utils.identity(source_df)


from language_model_service_api.languagemodelservice_api_embeddings_v3 import (  # noqa: E402
    GenericEmbeddingsRequest,
)
from palantir_models.models import GenericEmbeddingModel  # noqa: E402
from palantir_models.transforms import GenericEmbeddingModelInput  # noqa: E402
from pyspark.sql.types import ArrayType, FloatType  # noqa: E402


@transform(
    reviews=Input("ri.foundry.main.dataset.24120a72-a994-4958-9767-a41cbc74f733"),
    embedding_model=GenericEmbeddingModelInput(
        "ri.language-model-service..language-model.text-embedding-ada-002_azure"
    ),
    output=Output("ri.foundry.main.dataset.e92e3fae-8d8e-4ac6-a7c0-e112b1a998fa"),
)
def compute_embeddings(ctx, reviews, embedding_model: GenericEmbeddingModel, output):
    def internal_create_embeddings(val: str):
        return embedding_model.create_embeddings(
            GenericEmbeddingsRequest(inputs=[val])
        ).embeddings[0]

    reviews_df = reviews.pandas()
    reviews_df["embedding"] = reviews_df["patient_note"].apply(
        internal_create_embeddings
    )
    spark_df = ctx.spark_session.createDataFrame(reviews_df)
    out_df = spark_df.withColumn(
        "embedding", spark_df["embedding"].cast(ArrayType(FloatType()))
    )
    return output.write_dataframe(out_df)
