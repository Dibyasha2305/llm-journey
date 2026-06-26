from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# -----------------------------
# Load all knowledge base files
# -----------------------------
documents = []

folder = "knowledge_base"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        loader = TextLoader(
            os.path.join(folder, file),
            encoding="utf-8"
        )
        documents.extend(loader.load())

# -----------------------------
# Split documents into chunks
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# -----------------------------
# Create embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# Create FAISS vector database
# -----------------------------
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

# -----------------------------
# Function used by LangGraph
# -----------------------------
def retrieve_context(query: str):

    results = vectorstore.similarity_search(
        query,
        k=2
    )

    context = "\n".join(
        [doc.page_content for doc in results]
    )

    return context


# -----------------------------
# Testing (runs only when
# rag.py is executed directly)
# -----------------------------
if __name__ == "__main__":

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    print("Vector database created successfully!")

    query = "What are the pricing plans?"

    results = vectorstore.similarity_search(query, k=2)

    print("\nRetrieved Documents:\n")

    for doc in results:
        print(doc.page_content)
        print("-" * 50)

    context = retrieve_context(query)

    print("\nRetrieved Context:\n")
    print(context)