from langchain_openai import ChatOpenAI
from load_vector_db import load

from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors.chain_extract import LLMChainExtractor

from langchain_community.callbacks import get_openai_callback

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


db_dir = "./chroma_db"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

# create context compressor
compressor = LLMChainExtractor.from_llm(llm=llm)

# compressor retriever
document_retriever = ContexualCompressionRetiever(
    base_retriever=vector_store.as_retriever()
    base_compressor=compressor
)

prompt = ChatPromptTemplate.from_messages([
    ('system', """
        Use the following place of retrieved context to answer the question.
        If you do not know the answer, say I don't know.

        {context}
    """),
    ('human', '{input}')
])

# create a stuff document chain
stuff_document_chain = create_stuff_document_chain(
    llm-llm, prompt=prompt
)

# retrieve doc -> stuff doc
retrieval_chain = create_retrieval_chain(document_retriever, stuff_document_chain)

with get_openai_callback() as cb:
    question = inpur('Question ')
    if not bool(question):
        break
    result = retrieval_chain.invoke({ 'input': question})
    print(f'Input: {result["input"]}')
    print(f'Answer: {result["answer"]}')
    print('\n-------------------------')

