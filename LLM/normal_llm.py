from transformers import pipeline

# Load normal LLM (NO RAG, NO RETRIEVAL)
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=150
)

print("\n✅ Normal LLM is ready (NO RAG).")
print("Type your question and press Enter.")
print("Type 'exit' to stop.\n")

# 🔁 User input loop
while True:
    query = input("Ask a question: ").strip()

    if query.lower() in ["exit", "quit"]:
        print("\nExiting Normal LLM.")
        break

    result = llm(query)[0]["generated_text"]

    print("\nAnswer:")
    print(result.strip())
    print("-" * 60)

