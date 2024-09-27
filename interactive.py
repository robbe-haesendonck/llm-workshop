from llama_index.indices.managed.colbert import ColbertIndex
from llama_index.llms.groq import Groq

index = ColbertIndex.load_from_disk("./index", "factoids")

llm = Groq(
    model="llama3-8b-8192",
    api_key="some-api-key"
)

chat_engine = index.as_chat_engine(llm=llm)
try:
    chat_engine.chat_repl()
except ValueError as e:
    print(e)