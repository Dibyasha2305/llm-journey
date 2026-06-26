from graph import graph

# Initial state
state = {
    "customer_name": "David",
   "query": "What was my previous support issue?",
    "intent": "",
    "department": "",
    "context": "",
    "response": "",
    "approval_required": False,
    "approved": False,
    "history": []
}

# Run the LangGraph
result = graph.invoke(state)

# Print the result
print(result)