import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from mock_api import process_refund, check_payment_status, create_support_ticket

load_dotenv()

# 1. Load the vector DB (used for RAG)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# 2. Define the tools

@tool
def search_docs(query: str) -> str:
    """Searches Razorpay documentation for relevant information. Use this for any general question (how-to, policy, process)."""
    results = vectordb.similarity_search(query, k=4)
    return "\n\n".join([doc.page_content for doc in results])

@tool
def refund_payment(payment_id: str, amount: int) -> str:
    """Processes a refund for a payment. Use this when the user asks to refund a specific payment ID."""
    result = process_refund(payment_id, amount)
    return f"Refund successful. Refund ID: {result['id']}, Status: {result['status']}"

@tool
def payment_status(payment_id: str) -> str:
    """Checks the current status of a payment (captured, failed, or pending). Use this when the user asks about their payment status."""
    result = check_payment_status(payment_id)
    return f"Payment {result['payment_id']} status: {result['status']}, Amount: {result['amount']}"

@tool
def raise_ticket(issue: str, customer_email: str) -> str:
    """Creates a support ticket when the issue is complex or the agent cannot solve it directly. Needs the user's email and issue description."""
    result = create_support_ticket(issue, customer_email)
    return f"Support ticket created: {result['ticket_id']}. Our team will reach out soon."

tools = [search_docs, refund_payment, payment_status, raise_ticket]

# 3. Set up the LLM
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))

# 4. Create the agent
agent_executor = create_react_agent(llm, tools)

if __name__ == "__main__":
    conversation_history = []

    while True:
        q = input("\nAsk something (type 'exit' to quit): ")
        if q.lower() == "exit":
            break

        conversation_history.append(("human", q))

        try:
            response = agent_executor.invoke({"messages": conversation_history})
            conversation_history = response["messages"]
            answer = conversation_history[-1].content
            print("\nAnswer:", answer)
        except Exception as e:
            print("\nSorry, I couldn't process that request. Please try rephrasing your question.")
            # agar galat message history mein reh gaya ho, use hata do taaki agli baar issue na ho
            conversation_history.pop()