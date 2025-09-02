from flask import Flask, render_template, request, jsonify
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import HuggingFaceHub
import os

app = Flask(__name__)

# Set your Hugging Face API token (get it from https://huggingface.co/settings/tokens)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_hf_api_token_here"  # Replace with your free token

# Initialize LangChain with a free model from Hugging Face (e.g., GPT-2 for conversation)
llm = HuggingFaceHub(repo_id="gpt2", model_kwargs={"temperature": 0.7, "max_length": 100})

# Prompt template for conversational chatbot
template = """You are a helpful assistant. Answer the user's question based on the conversation history.

Conversation history:
{chat_history}

User: {question}
Assistant:"""

prompt = PromptTemplate(input_variables=["chat_history", "question"], template=template)

# Memory to keep conversation history
memory = ConversationBufferMemory(memory_key="chat_history")

# LangChain chain for conversation
chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chain.run(question=user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
