from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import VectorDBQA
from langchain.llms import Cohere
from langchain.embeddings import CohereEmbeddings
import os

loader = PyPDFLoader(r"C:\Users\67988\OneDrive\Documents\Temp Revised SWE Mansoor Lunawadi Resume Moti.pdf")
pages = loader.load_and_split()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(pages)

# Set the Cohere API key in the environment
os.environ["COHERE_API_KEY"] = 'ISZTWo9YqEizcG710vFjlUgCyIVZF6wCJUUwLLEX'

# Initialize Cohere embeddings
embeddings = CohereEmbeddings()
db = Chroma.from_documents(docs, embeddings)
qa = VectorDBQA.from_chain_type(llm=Cohere(), chain_type="stuff", vectorstore = db)

query = "Based on my resume, tell me what I am good at"
print(qa.run(query))
