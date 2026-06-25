import faiss
import pandas as pd
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

_embedding_model = None
_generator = None
_index = None
_emb_df = None

PROMPT_TEMPLATE = """
Answer the question using only the provided complaint excerpts.

Complaint Excerpts:
{context}

Question:
{question}
"""


def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    return _embedding_model


def get_generator():
    global _generator
    if _generator is None:
        _generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-mini",
            device_map="auto",
            torch_dtype="auto"
        )
    return _generator


def get_index():
    global _index
    if _index is None:
        _index_path = DATA_DIR / "vector_store" / "faiss_index.bin"
        _index = faiss.read_index(str(_index_path))
    return _index


def get_emb_df():
    global _emb_df
    if _emb_df is None:
        _emb_df = pd.read_parquet(
            str(DATA_DIR / "complaint_embeddings.parquet")
        )
    return _emb_df


def retrieve_chunks(question, k=3):
    embedding_model = get_embedding_model()
    index = get_index()
    emb_df = get_emb_df()

    query_embedding = embedding_model.encode([question]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    retrieved_docs = []
    for idx in indices[0]:
        retrieved_docs.append(emb_df.iloc[idx])

    return retrieved_docs


def generate_answer(question):
    retrieved_docs = retrieve_chunks(question, k=3)

    context = "\n\n".join(
        [doc["document"][:300] for doc in retrieved_docs]
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    generator = get_generator()
    response = generator(prompt, max_new_tokens=100)

    answer = response[0]["generated_text"]
    return answer, retrieved_docs