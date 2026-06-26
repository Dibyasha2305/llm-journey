from state import CustomerSupportState


def supervisor_agent(state: CustomerSupportState):

    print(">>> Supervisor Node")

    if state["approval_required"]:

        state["approved"] = False

        state["response"] = (
            "⚠️ Your request requires human supervisor approval.\n\n"
            "Your request has been forwarded to the support supervisor. "
            "You will receive a confirmation once it has been reviewed."
        )

    else:

        state["approved"] = True

    return state