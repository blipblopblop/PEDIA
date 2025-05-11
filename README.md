**🧠 Overview**

PEDIA utilizes the text-embedding-ada-002 model via the Azure OpenAI Service to generate vector representations (embeddings) of both:
  - Pediatric patient notes (ages 0–10)
  - ICD-10 medical diagnostic codes (first 10,000 rows)

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
  - Compute cosine similarity between Pediatric Patient note embeddings and ICD-10 embeddings.
  - Rank ICD-10 codes by similarity score for each patient note, refer to Simlariity_ICDCode_PateintDescp.csv

**🔍 Key Features**
- Early Diagnostic Aid: Helps nurses identify likely conditions before a doctor is available.
- NLP-Powered: Uses state-of-the-art vector embeddings for natural language understanding, refer to Ped_Patient_Notes_Embdng.csv and ICD_10_Codes_Embdng.csv
- Similarity Scoring: Ranks ICD-10 codes based on relevance to patient note,s refer to Similarity_ICDCode_PatientDescp.csv
- Custom Dataset: Works with the Ped_Patient_Notes_Embdng.csv dataset extracted from PMC_Patients_clean.csv

**Download dataset:** 
[Pediatric Notes CSV] https://drive.google.com/file/d/11ln9ZuUO8wOkAJ_6lXNqP51TT5iRqu6m/view?usp=sharing
[ICD-10 codes CSV] https://drive.google.com/file/d/1_NrCswMwpPTCiQREX4i5wihExSu-SgK4/view?usp=sharing
[Similarity Score CSV] https://drive.google.com/file/d/1SYrMtjYFQEbHRJPWa9Apzd2i7_Mp4388/view?usp=sharing
  
<img width="377" alt="Screenshot 2025-05-11 at 3 21 16 PM" src="https://github.com/user-attachments/assets/56e423ad-4466-4fca-ae5c-97221cf6fcb1" />
