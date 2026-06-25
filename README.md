# Intelligent Complaint Analysis for Financial Services

## Project Overview

Financial institutions receive thousands of customer complaints every month through multiple channels such as mobile applications, email, and regulatory reporting systems. Analyzing these complaints manually is time-consuming and often prevents organizations from identifying emerging issues quickly.

This project develops a Retrieval-Augmented Generation (RAG) chatbot that transforms unstructured customer complaints into actionable business insights. Using complaint data from the Consumer Financial Protection Bureau (CFPB), the system enables stakeholders to ask natural language questions about customer issues and receive evidence-based answers generated from relevant complaint records.

The solution was developed for the fictional company **CrediTrust Financial**, a digital finance provider offering services including credit cards, personal loans, savings accounts, and money transfers.

---

## Business Problem

Product managers, compliance officers, and customer support teams often need to answer questions such as:

* Why are customers dissatisfied with credit card services?
* What fraud-related issues are being reported?
* What customer service problems appear most frequently?
* What trends are emerging in loan complaints?

Traditionally, answering these questions requires manually reviewing hundreds or thousands of complaint records. This project reduces that effort by combining semantic search and Large Language Models (LLMs) to provide fast, evidence-based summaries.

---

## Dataset

The project uses complaint data from the Consumer Financial Protection Bureau (CFPB), containing:

* Consumer complaint narratives
* Product categories
* Issue and sub-issue labels
* Company information
* State information
* Complaint submission dates

After preprocessing, only complaints related to the following financial products were retained:

* Credit Cards
* Personal Loans
* Savings Accounts
* Money Transfers

Records without complaint narratives were removed to ensure meaningful text analysis.

---

## Methodology

### 1. Exploratory Data Analysis (EDA)

The first stage involved exploring the complaint dataset to understand:

* Complaint distribution across financial products
* Narrative availability
* Narrative length distribution
* Data quality issues

This analysis revealed significant variation in complaint volumes across products and highlighted the importance of filtering records with missing narratives.

---

### 2. Data Preprocessing

Complaint narratives were cleaned and standardized by:

* Converting text to lowercase
* Removing special characters
* Removing unnecessary boilerplate language
* Handling missing values
* Filtering target financial products

The cleaned dataset was then saved for downstream processing.

---

### 3. Text Chunking

Long complaint narratives can exceed the context limitations of embedding models and language models.

To address this, complaint narratives were divided into smaller overlapping text chunks using a chunking strategy.

Chunking provides several benefits:

* Preserves semantic meaning
* Improves retrieval accuracy
* Reduces information loss
* Enables efficient vector search

Each chunk represents a smaller portion of a complaint while maintaining enough context for meaningful retrieval.

---

### 4. Embedding Generation

Each text chunk was converted into a dense numerical vector using:

**Sentence Transformers**

* Model: `all-MiniLM-L6-v2`

This model was selected because it:

* Produces high-quality semantic embeddings
* Is computationally efficient
* Is widely used in Retrieval-Augmented Generation systems
* Supports fast similarity search

The resulting embeddings capture semantic meaning rather than relying solely on keyword matching.

---

### 5. Vector Store Creation

To enable efficient retrieval, embeddings were indexed using **FAISS (Facebook AI Similarity Search)**.

The vector store contains:

* Chunk embeddings
* Complaint identifiers
* Product metadata
* Source information

This allows complaint chunks to be retrieved quickly based on semantic similarity to user questions.

---

### 6. Retrieval-Augmented Generation (RAG)

The RAG pipeline consists of three stages:

#### Retrieval

When a user submits a question:

1. The question is converted into an embedding.
2. FAISS performs similarity search.
3. The most relevant complaint chunks are retrieved.

#### Augmentation

Retrieved complaint excerpts are combined into a context block.

#### Generation

The context and question are passed to a Large Language Model (LLM), which generates an evidence-based response.

The project uses:

* Hugging Face Transformers
* FLAN-T5 Base

A prompt template guides the model to answer using only retrieved complaint evidence.

---

## Interactive Web Application

A Streamlit web application was developed to provide a user-friendly interface for non-technical stakeholders.

### Features

* Ask questions in natural language
* Generate complaint summaries
* View retrieved complaint sources
* Clear and reset interactions
* Simple and intuitive interface

The source display feature improves transparency by allowing users to verify the evidence used to generate responses.

---

## Technologies Used

### Data Processing

* Python
* Pandas
* NumPy

### NLP and Machine Learning

* Sentence Transformers
* Hugging Face Transformers
* FLAN-T5 Base

### Vector Search

* FAISS

### Application Development

* Streamlit

### Development Environment

* Jupyter Notebook

---


## Future Improvements

* Use larger instruction-tuned language models (Mistral, Llama, Gemini)
* Implement hybrid retrieval (keyword + semantic search)
* Add response streaming
* Improve prompt engineering
* Deploy the application to the cloud
* Add complaint trend visualization dashboards

