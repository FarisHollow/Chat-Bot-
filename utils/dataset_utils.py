import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import openai
from dotenv import load_dotenv


if not load_dotenv():
    print("Warning: .env file not found!")
else:
    print("Successfully loaded .env file.")

openai.api_key = os.getenv("api_key")

if not openai.api_key:
    raise Exception("OpenAI API key not found. Please add it to your .env file.")

PERSIST_DIR = "./storage"

documents = SimpleDirectoryReader("data").load_data()
if not os.path.exists(PERSIST_DIR):

 index = VectorStoreIndex.from_documents(documents)
 index.storage_context.persist(persist_dir=PERSIST_DIR)

else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
