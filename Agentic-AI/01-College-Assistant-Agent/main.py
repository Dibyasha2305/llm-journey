from langchain_ollama import ChatOllama

from langchain.agents import (
    create_tool_calling_agent,
    AgentExecutor
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from tools import (
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_info
)

# LLM
llm = ChatOllama(
    model="qwen3:4b"
)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful college assistant. Use tools whenever calculations are required."
        ),
        (
            "human",
            "{input}"
        ),
        (
            "placeholder",
            "{agent_scratchpad}"
        )
    ]
)

# All tools in one place
tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_info
]

# Agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
print("College Assistant Started!")
print("Type 'exit' to quit.\n")

while True:

    user_query = input("You: ")

    if user_query.lower() == "exit":
        print("Goodbye!")
        break

    response = agent_executor.invoke(
        {
            "input": user_query
        }
    )

    print("\nFinal Answer:")
    print(response["output"])
    print("\n" + "-" * 50 + "\n")