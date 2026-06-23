# Intelligent Complaint Analysis for Financial Services

## Overview

This project develops a Retrieval-Augmented Generation (RAG) chatbot for CrediTrust Financial to transform large volumes of customer complaints into actionable insights. The system enables business stakeholders to ask natural-language questions and receive evidence-based answers derived from historical complaint data.

## Business Objective

The solution aims to:

* Reduce the time required to identify complaint trends.
* Enable non-technical teams to analyze customer feedback independently.
* Support proactive issue identification using customer complaint data.

## Dataset

The project uses the Consumer Financial Protection Bureau (CFPB) complaint dataset, containing:

* Consumer complaint narratives
* Product information
* Issue and sub-issue categories
* Company metadata
* Submission dates

For this project, complaints were filtered to the following product categories:

* Credit Cards
* Personal Loans
* Savings Accounts
* Money Transfers

## Task 1: EDA and Preprocessing

Completed:

* Loaded and explored the CFPB complaint dataset.
* Analyzed complaint distribution across financial products.
* Examined narrative length distribution.
* Identified and removed records with missing complaint narratives.
* Filtered complaints to business-relevant product categories.
* Applied text normalization and cleaning.
* Saved the cleaned dataset as:

```text
data/filtered_complaints.csv
```

### Key Findings

* Original dataset size: ~9.6 million complaints
* Complaints with narratives: ~2.98 million
* Filtered complaints (target products): 463,933
* Median complaint length: 136 words
* Maximum complaint length: 6,469 words

These findings justify the use of text chunking and embeddings in the subsequent RAG pipeline.

## Next Steps

### Task 2

* Create a stratified sample.
* Implement text chunking.
* Generate embeddings using all-MiniLM-L6-v2.
* Build a vector database using FAISS or ChromaDB.

### Task 3

* Develop the retrieval and generation pipeline.
* Evaluate system performance using representative business questions.

### Task 4

* Build an interactive interface using Streamlit or Gradio.
* Display generated answers and supporting source chunks.

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Sentence Transformers
* FAISS / ChromaDB
* LangChain
* Streamlit / Gradio
