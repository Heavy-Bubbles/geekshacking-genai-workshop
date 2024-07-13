from os import path

from langchain_core.vectorstores import VectorStore

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_community.document_loaders import DirectoryLoader, UnstructuredEPubLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Utility to load Chroma
def load(db_path = './chroma_db', load_dir = '../ebooks') -> VectorStore:
   # if db_path does not exists then create the database
   if path.exists(db_path):
      print('Loading dtabase...')
      return Chroma(persist_directory=db_path, embedding_function=embed_model)

   else:
      # create the database
      print('Create database...')
      loader = DirectoryLoader(path=load_dir, glob='./*.epub', loader_cls=UnstructuredEPubLoader)
      content = lader.load()
      text_splitter = RecursiveTextSplitter(chunk_sie=2000, chunk_overlap=50)
      splits = text_splittr.split_documents(content)
      return Chroma.from_documents(persist_directory=db_path, document=splits, embedding=embed_model)
