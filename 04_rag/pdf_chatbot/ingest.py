from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Path to PDF
pdf_path = "data/NIPS-2017-attention-is-all-you-need-Paper.pdf"

# Load PDF
loader = PyPDFLoader(pdf_path)

documents = loader.load()

print(f"Loaded {len(documents)} pages from PDF")

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Split into chunks
chunks = text_splitter.split_documents(documents)

print(f"\nCreated {len(chunks)} text chunks\n")

# Preview first chunk
print(chunks[0].page_content)

# Create vector database
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="local-rag",
    persist_directory="vectorstore"
)

print("Vector database created successfully!")