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

# 2. Define all tools (same as before)

@tool
def search_docs(query: str) -> str:
    """Searches Razorpay documentation for relevant information."""
    results = vectordb.similarity_search(query, k=4)
    return "\n\n".join([doc.page_content for doc in results])

@tool
def refund_payment(payment_id: str, amount: int) -> str:
    """Processes a refund for a payment. The amount should be passed exactly as the user states it in rupees, do not convert to paise."""
    result = process_refund(payment_id, amount)
    return f"Refund successful. Refund ID: {result['id']}, Status: {result['status']}"
@tool
def payment_status(payment_id: str) -> str:
    """Checks the current status of a payment."""
    result = check_payment_status(payment_id)
    return f"Payment {result['payment_id']} status: {result['status']}, Amount: {result['amount']}"

@tool
def raise_ticket(issue: str, customer_email: str) -> str:
    """Creates a support ticket."""
    result = create_support_ticket(issue, customer_email)
    return f"Support ticket created: {result['ticket_id']}. Our team will reach out soon."

# 3. LLM setup
llm = ChatGroq(model="openai/gpt-oss-20b", api_key=os.getenv("GROQ_API_KEY"))

# 4. Three specialized sub-agents, each with only the tools it needs

support_agent = create_react_agent(llm, [search_docs], prompt="You are the Support Agent, part of the Customer Support Multi-Agent System. You are not ChatGPT or any other AI — always identify yourself accordingly if asked.")
billing_agent = create_react_agent(llm, [refund_payment, payment_status], prompt="You are the Billing Agent, part of the Customer Support Multi-Agent System. You are not ChatGPT or any other AI — always identify yourself accordingly if asked.")
ticket_agent = create_react_agent(llm, [raise_ticket], prompt="You are the Ticket Agent, part of the Customer Support Multi-Agent System. You are not ChatGPT or any other AI — always identify yourself accordingly if asked.")

# 5. Router: a small LLM call that decides which agent should handle the question

def route_query(question: str) -> str:
    """Asks the LLM to classify the question into one category."""
    routing_prompt = f"""Classify the following user message into exactly one category:
- "support" : general questions, how-to, documentation, policies
- "billing" : refunds, payment status, transaction issues
- "ticket" : the user explicitly wants to raise/create a support ticket, or has a complex issue

Message: "{question}"

Reply with only one word: support, billing, or ticket."""

    response = llm.invoke(routing_prompt)
    category = response.content.strip().lower()

    if "billing" in category:
        return "billing"
    elif "ticket" in category:
        return "ticket"
    else:
        return "support"

# 6. Main loop

if __name__ == "__main__":
    conversation_history = []

    while True:
        q = input("\nAsk something (type 'exit' to quit): ")
        if q.lower() == "exit":
            break

        conversation_history.append(("human", q))

        category = route_query(q)
        print(f"[Routed to: {category} agent]")

        agent_map = {
            "support": support_agent,
            "billing": billing_agent,
            "ticket": ticket_agent
        }
        chosen_agent = agent_map[category]

        try:
            response = chosen_agent.invoke({"messages": conversation_history})
            conversation_history = response["messages"]
            answer = conversation_history[-1].content
            print("\nAnswer:", answer)
        except Exception as e:
            print("\nSorry, I couldn't process that request. Please try rephrasing your question.")
            conversation_history.pop()