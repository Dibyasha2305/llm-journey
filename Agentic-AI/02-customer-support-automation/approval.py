from state import CustomerSupportState


def check_approval(state: CustomerSupportState):

    print(">>> Approval Node")

    query = state["query"].lower()

    approval_keywords = [
        "refund",
        "cancel",
        "account closure",
        "compensation",
        "management"
    ]

    if any(word in query for word in approval_keywords):
        state["approval_required"] = True
    else:
        state["approval_required"] = False

    return state