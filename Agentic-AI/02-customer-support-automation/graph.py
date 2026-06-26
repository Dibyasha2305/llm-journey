from supervisor import supervisor_agent
from approval import check_approval
from langgraph.graph import StateGraph, START, END

from state import CustomerSupportState

from nodes import (
    classify_intent,
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent,
    memory_agent,
    route_intent
)
builder = StateGraph(CustomerSupportState)

# Add nodes
builder.add_node("intent_classifier", classify_intent)
builder.add_node("sales", sales_agent)
builder.add_node("technical", technical_agent)
builder.add_node("billing", billing_agent)
builder.add_node("account", account_agent)
builder.add_node("memory", memory_agent)
builder.add_node("approval", check_approval)
builder.add_node("supervisor", supervisor_agent)

# START -> Intent Classifier
builder.add_edge(START, "intent_classifier")

# Conditional Routing
builder.add_conditional_edges(
    "intent_classifier",
    route_intent,
    {
        "sales": "sales",
        "technical": "technical",
        "billing": "billing",
        "account": "account",
        "memory": "memory",
        "end": END
    }
)

# All agents -> END
builder.add_edge("sales", END)
builder.add_edge("technical", END)
builder.add_edge("billing", "approval")
builder.add_edge("approval", "supervisor")
builder.add_edge("supervisor", END)
builder.add_edge("account", END)
builder.add_edge("memory", END)

graph = builder.compile()