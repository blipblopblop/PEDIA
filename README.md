**🧠 Overview**

PEDIA utilizes the text-embedding-ada-002 model via the Azure OpenAI Service to generate vector representations (embeddings) of both:

Pediatric patient notes (ages 0–10)

ICD-10 medical diagnostic codes (top 10,000)

It then computes similarity scores between patient notes and ICD-10 codes using cosine similarity, helping suggest potential diagnoses based on text input.

**⚙️ How It Works**
Data Preparation
  - Extract pediatric notes (ages 0–10) from PMC_Patients_cleaned.csv.
  - Limit to the first 10 patient notes for performance testing.

Embedding Generation
  - Use text-embedding-ada-002 via Azure OpenAI to embed, refer to Child_Patients_Notes_Training.py and ICD_10_Codes_Training.py:
    - Pediatric Patient notes Ped_Patient_Notes_Embdng.csv 
    - First 10,000 ICD-10 codes ICD_10_Codes_Embdng.csv

Similarity Matching
  - Compute cosine similarity between note embeddings and ICD-10 embeddings.
  - Rank ICD-10 codes by similarity score for each patient note refer to Simlariity_ICDCode_PateintDescp.csv

**🔍 Key Features**
- Early Diagnostic Aid: Helps nurses identify likely conditions before a doctor is available.
- NLP-Powered: Uses state-of-the-art vector embeddings for natural language understanding, refer to Ped_Patient_Notes_Embdng.csv and ICD_10_Codes_Embdng.csv
- Similarity Scoring: Ranks ICD-10 codes based on relevance to patient note,s refer to Simlariity_ICDCode_PateintDescp.csv
- Custom Dataset: Works with the Pediatric_Notes dataset extracted from PMC_Patients_clean.csv
  
<img width="559" alt="Screenshot 2025-05-10 at 5 58 17 PM" src="https://github.com/user-attachments/assets/2f7bc414-5182-4c14-bc8e-ec2f42339e0f" />
