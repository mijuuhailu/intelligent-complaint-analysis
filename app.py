import streamlit as st
from src.rag_pipeline import generate_answer

st.set_page_config(
    page_title="CrediTrust Complaint Analysis Assistant",
    layout="centered"
)

st.title("CrediTrust Complaint Analysis Assistant")
st.write("Ask questions about customer complaints.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question before asking.")
    else:
        with st.spinner("Generating answer..."):
            try:
                answer, docs = generate_answer(question)
            except Exception as e:
                st.error(f"Error generating answer: {e}")
            else:
                st.subheader("Answer")
                st.write(answer)

                st.subheader("Sources")
                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"**Source {i}**")
                    st.write(doc["document"])

if st.button("Clear"):
    st.experimental_rerun()