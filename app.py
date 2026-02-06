from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from flask import Flask, render_template, request
from prompts import qa_system_prompt, contextualize_q_system_prompt
import os

load_dotenv()

FAISS_PATH = "faiss"
llm = Ollama(model="gemma3:1b")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

app = Flask(__name__)

chat_history = []
conversation_store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in conversation_store:
        conversation_store[session_id] = ChatMessageHistory()
    return conversation_store[session_id]

def get_document_loader():
    loader = DirectoryLoader(
        "static",
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )
    return loader.load()

def get_text_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(documents)


def get_embeddings():
    path = os.path.join(os.getcwd(), FAISS_PATH)

    if os.path.exists(path):
        return FAISS.load_local(
            path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

    documents = get_document_loader()
    chunks = get_text_chunks(documents)

    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(path)

    return db

def get_retriever():
    return get_embeddings().as_retriever()


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():

    if request.method == "GET":
        return render_template("chat.html")

    question = request.form["question"]
    retriever = get_retriever()

    contextualize_prompt = ChatPromptTemplate.from_messages([
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_prompt
    )

    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

    conversational_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

    response = conversational_chain.invoke(
        {"input": question},
        config={"configurable": {"session_id": "default"}}
    )

    chat_history.append(question)
    chat_history.append(response["answer"])

    return render_template("chat.html", chat_history=chat_history)


if __name__ == "__main__":
    app.run(debug=True)
