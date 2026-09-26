import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq

load_dotenv()

DB_FOLDER = "chroma_db"

# 1. Load vector DB
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=DB_FOLDER, embedding_function=embeddings)

# 2. Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    # Find relevant chunks
    results = vectordb.similarity_search(question, k=4)
    context = "\n\n".join([doc.page_content for doc in results])

    # Send context + question to LLM
    prompt = f"""You are an expert assistant for Razorpay documentation. Answer the question based on the context below. If the answer is not in the context, say "I could not find this information in the docs."

Context:
{context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (type 'exit' to quit): ")
        if q.lower() == "exit":
            break
        answer = ask(q)
        print("\nAnswer:", answer)