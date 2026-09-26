import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_FOLDER = "data"
DB_FOLDER = "chroma_db"

# loading .md files
loader = DirectoryLoader(DATA_FOLDER, glob="*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
docs = loader.load()
print(f"Loaded {len(docs)} documents")

#chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

# 3. Embeddings + save in chroma
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=DB_FOLDER)

print("Done! Vector DB saved in 'chroma_db' folder.")