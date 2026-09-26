import streamlit as st
from multi_agent import support_agent, billing_agent, ticket_agent, route_query

st.set_page_config(page_title="Customer Support Multi-Agent System", page_icon="🤖")
st.title("🤖 Customer Support Multi-Agent System")
st.caption("Ask about refunds, payment status, documentation, or raise a support ticket")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

# Show previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# New input from user
user_input = st.chat_input("Type your question...")

if user_input:
    # Show the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.history.append(("human", user_input))

    # Decide which agent should handle this
    category = route_query(user_input)
    agent_map = {
        "support": support_agent,
        "billing": billing_agent,
        "ticket": ticket_agent
    }
    chosen_agent = agent_map[category]

    with st.chat_message("assistant"):
        with st.spinner(f"Thinking... (routed to {category} agent)"):
            try:
                response = chosen_agent.invoke({"messages": st.session_state.history})
                st.session_state.history = response["messages"]
                answer = st.session_state.history[-1].content
            except Exception as e:
                answer = "Sorry, I couldn't process that request. Please try rephrasing your question."
                st.session_state.history.pop()

        st.markdown(f"*[Routed to: {category} agent]*")
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})