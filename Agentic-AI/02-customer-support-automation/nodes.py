from memory import get_last_conversation
from rag import retrieve_context
from state import CustomerSupportState


# -------------------------
# Intent Classification
# -------------------------
def classify_intent(state: CustomerSupportState):

    query = state["query"].lower()

    # Billing
    if any(word in query for word in ["refund", "payment", "invoice", "billing"]):
        state["intent"] = "Billing"

    # Sales
    elif any(word in query for word in ["price", "pricing", "plan", "subscription"]):
        state["intent"] = "Sales"

    # Technical
    elif any(word in query for word in ["error", "bug", "login", "install", "crash", "upload"]):
        state["intent"] = "Technical"

    # Account
    elif any(word in query for word in ["password", "profile", "account"]):
        state["intent"] = "Account"

    # Memory
    elif "previous" in query:
        state["intent"] = "Memory"

    else:
        state["intent"] = "General"

    return state


# -------------------------
# Sales Agent
# -------------------------
def sales_agent(state: CustomerSupportState):

    state["department"] = "Sales"

    context = retrieve_context(state["query"])

    state["context"] = context

    state["response"] = (
        "Based on our knowledge base:\n\n"
        + context
    )

    return state


# -------------------------
# Technical Agent
# -------------------------
def technical_agent(state: CustomerSupportState):

    state["department"] = "Technical Support"

    context = retrieve_context(state["query"])

    state["context"] = context

    state["response"] = (
        "Based on our technical documentation:\n\n"
        + context
    )

    return state


# -------------------------
# Billing Agent
# -------------------------
def billing_agent(state: CustomerSupportState):

    print(">>> Billing Agent")

    state["department"] = "Billing"

    context = retrieve_context(state["query"])

    state["context"] = context

    state["response"] = (
        "Based on our billing policies:\n\n"
        + context
    )

    return state

# -------------------------
# Account Agent
# -------------------------
def account_agent(state: CustomerSupportState):

    state["department"] = "Account"

    context = retrieve_context(state["query"])

    state["context"] = context

    state["response"] = (
        "Based on our account documentation:\n\n"
        + context
    )

    return state


# -------------------------
# Memory Agent
# -------------------------
def memory_agent(state: CustomerSupportState):

    last = get_last_conversation(state["customer_name"])

    if last:
        query, response = last

        state["response"] = (
            f"Your previous support issue was:\n\n"
            f"Query: {query}\n"
            f"Response: {response}"
        )
    else:
        state["response"] = "No previous conversation found."

    return state


# -------------------------
# Routing Function
# -------------------------
def route_intent(state: CustomerSupportState):

    intent = state["intent"]

    if intent == "Sales":
        return "sales"

    elif intent == "Technical":
        return "technical"

    elif intent == "Billing":
        return "billing"

    elif intent == "Account":
        return "account"

    elif intent == "Memory":
        return "memory"

    else:
        return "end"