# Conversational Chatbot using LangChain and Flask
**Overview**
This project is a simple conversational chatbot built using LangChain for handling dialogue logic and Flask for the web-based UI. The chatbot maintains conversation history and responds to user queries using a free LLM from Hugging Face. It demonstrates skills in building AI applications, integrating LLMs, and creating interactive web interfaces, ideal for portfolio showcasing in AI and web development.

**Free API Used**

Hugging Face Inference API: Used for the LLM (e.g., GPT-2). Sign up for a free API token at Hugging Face and get your token from https://huggingface.co/settings/tokens. This API is free for limited usage and doesn't require payment for basic access.

**Project Structure**

**conversational_chatbot.py:** Main Flask app script with LangChain integration for the chatbot logic.

**index.html:** HTML template for the chat interface (placed in a templates folder).

**requirements.txt:** Lists required Python libraries.

**.gitignore:** Specifies files to exclude from version control.

**README.md:** This file.

**Prerequisites**

Python 3.11.9 (or compatible)
Hugging Face API token (free, as linked above)



**Usage**

Enter messages in the input field and click "Send".
The chatbot uses LangChain's memory to recall conversation history and generate responses via Hugging Face's free API.
Example: Ask "What's the weather like?" and follow up with "In New York?" to see context handling.

**Future Improvements**

Integrate more advanced models (e.g., fine-tuned BERT for specific tasks).
Add user authentication or persistent storage for conversations.
Deploy to a cloud platform like Heroku for online access.

