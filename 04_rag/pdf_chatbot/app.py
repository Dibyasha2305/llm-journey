from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Load vector database
vector_db = Chroma(
    persist_directory="vectorstore",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="local-rag"
)

print("Vector database loaded successfully!")

# Create retriever
retriever = vector_db.as_retriever()

print("Retriever created successfully!")

# Initialize LLM
llm = ChatOllama(model="llama3")

print("LLM initialized successfully!")

# User question
question = input("Ask your PDF: ")

# Retrieve relevant chunks
results = retriever.invoke(question)

# Combine retrieved chunks into context
context = "\n\n".join([doc.page_content for doc in results])

# Create prompt
prompt = ChatPromptTemplate.from_template("""
Answer the question based ONLY on the following context:

{context}

Question:
{question}
""")

# Create final prompt
final_prompt = prompt.format(
    context=context,
    question=question
)

# Generate response
response = llm.invoke(final_prompt)

print("\nANSWER:\n")

print(response.content)