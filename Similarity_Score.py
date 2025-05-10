from transforms.api import transform_df, Input, Output
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, FloatType

# This transform calculates the similarity score between the patient notes and the ICD-10 codes
# using the cosine similarity score
# for easy computing of the similarity score, only the first 10 patient notes are used

@transform_df(
    Output("ri.foundry.main.dataset.5cf4d52f-704f-4075-b5bb-b33f65d88626"),
    dataset1=Input("ri.foundry.main.dataset.e92e3fae-8d8e-4ac6-a7c0-e112b1a998fa"),
    dataset2=Input("ri.foundry.main.dataset.2a07fb3b-6cee-42c7-a6eb-39bb98856f4d"),
)
def compute(dataset1, dataset2):

    # Convert Spark DataFrames to Pandas DataFrames
    df1 = dataset1.toPandas()
    df1_first_ten = df1.head(10)    # Only using the first 10 patient notes for testing purposes
    df2 = dataset2.toPandas()

    # Extract embeddings
    embeddings1 = np.array(df1_first_ten["embedding"].tolist())
    embeddings2 = np.array(df2["embedding"].tolist())

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(embeddings1, embeddings2)

    # Create a DataFrame with similarity scores
    similarity_scores = []
    for i, row1 in enumerate(df1_first_ten.itertuples()):
        for j, row2 in enumerate(df2.itertuples()):
            similarity_scores.append(
                {
                    "patient_id1": row1.patient_id,
                    "patient_id2": row2.icd_10_code,
                    "similarity_score": float(similarity_matrix[i, j]),
                }
            )

    # Convert results to a Pandas DataFrame
    result_df = pd.DataFrame(similarity_scores)

    # Convert back to a Spark DataFrame
    return dataset1.sparkSession.createDataFrame(result_df)
