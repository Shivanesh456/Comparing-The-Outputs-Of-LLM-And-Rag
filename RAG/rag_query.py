import warnings
warnings.filterwarnings("ignore")

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import pipeline

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Correct pipeline for FLAN-T5
hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=150
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Custom prompt (prevents context echo)
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Answer the question clearly and concisely using the context below.

Context:
{context}

Question:
{question}

Answer:
"""
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type_kwargs={"prompt": prompt}
)

print("\n✅ RAG system is ready.")
print("Type your question and press Enter.")
print("Type 'exit' to stop.\n")

# 🔁 MULTIPLE QUESTIONS LOOP
while True:
    query = input("Ask a question: ").strip()

    if query.lower() in ["exit", "quit"]:
        print("\nExiting RAG system.")
        break

    response = qa.invoke({"query": query})

    print("\nAnswer:")
    print(response["result"].strip())
    print("-" * 60)
