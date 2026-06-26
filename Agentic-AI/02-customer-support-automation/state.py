from typing import TypedDict, List

class CustomerSupportState(TypedDict):
    customer_name: str
    query: str
    intent: str
    department: str
    context: str
    response: str
    approval_required: bool
    approved: bool
    history: List[str]