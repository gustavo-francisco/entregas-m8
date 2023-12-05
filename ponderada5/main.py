from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import Runnable, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import gradio as gr

loader = TextLoader("/home/gustavo/entregas-m8/ponderada5/data/context.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}"""

prompt = ChatPromptTemplate.from_template(template)

model = Ollama(model="mistral")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()

    def respond(message, history):
        response = ""
        for s in chain.stream(message):
            response += s
        history.append((message, response))
        return "", history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

        