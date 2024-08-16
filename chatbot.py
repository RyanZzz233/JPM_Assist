import os
import sys
import warnings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning)

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Load environment variables from .env file
load_dotenv(resource_path('.env'))

# Set OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

# Check if the directory exists
data_directory = resource_path("data")
if not os.path.exists(data_directory):
    raise FileNotFoundError(f"Directory not found: {data_directory}")

# Load all .txt and .pdf files in the "data" directory
loaders = {
    ".txt": DirectoryLoader(
        data_directory,
        glob="**/*.txt",
        loader_cls=TextLoader,
        show_progress=True,
    ),
    ".pdf": DirectoryLoader(
        data_directory,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True,
    ),
}

# Collect documents from all loaders
documents = []
for file_type, loader in loaders.items():
    print(f"Loading {file_type} files")
    documents.extend(loader.load())

# Create an index with embeddings
embedding_function = OpenAIEmbeddings()
index_creator = VectorstoreIndexCreator(embedding=embedding_function)
index = index_creator.from_documents(documents)

# Set a context for the model
context = "You are an expert consultant for digital transformation for JP Morgan. You have professional background in both technology and business. Answer in a professional tone."

print("Welcome to the JP Morgan Digital Transformation Assistance System!")
print("We use Large Language Models and Retrieval-Augmented Generation")
print("to assist you with digital transformation guidelines and best practices.\n")

# Query loop
while True:
    user_query = input("Enter your query (or type 'exit' to quit): ")
    if user_query.lower() in ['exit', 'quit']:
        break
    # Prepend the context to the user's query
    query = f"{context}\n\n{user_query}"
    response = index.query(query, llm=ChatOpenAI(model="gpt-4o-mini"))
    print(response)