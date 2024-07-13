from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_community.document_loaders import UnstructuredEPubLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# load the book
content = UnstructuredEPubLoader('../ebooks/monkeys_paw.epub').load()

# split the document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500, chunk_overlap=50, separators=['.',';',' ']
)
splits = text_splitter.split_documents(content)

# Load into vector database, Chroma
# create an embeding
embed_model = OpenAIEmbeddings()
# load the splits into the database
vector_store = Chroma.from_documents(documents=splits, embedding=embed_model)

# perform a similarity search
results = vector_stor.similarity_search_with_score(
    query="what are the three wishes",
    k=5
)
for i, r in enumerate(results):
    print('\n---------------')
    #print(f'{r[i].page_content}')
    print(r)
    