# ------------------------------
# 🤖 LLM-Powered Q&A Assistant (Streaming)
# ------------------------------
# Uses Ollama (LLaMA 3.2) to provide clear answers to user questions
# Designed for beginners — explains answers in simple language
# ------------------------------

# 📦 Imports
import requests
import ollama
from typing import List
from IPython.display import Markdown, display, update_display  # Works in notebooks only
from openai import OpenAI  # Placeholder if integrating with OpenAI later

# 🔧 Model Constants
MODEL_GPT = 'gpt-4o-mini'       # OpenAI model (unused here, placeholder)
MODEL_LLAMA = 'llama3.2'        # Local LLaMA model via Ollama

# 🧠 System Prompt
system_prompt = (
    "You are an ai chatbot that takes questions (frontier model).\n"
    "You will analyse or process the question given to you.\n"
    "You will respond with an answer that is appropriate to the question with clear explanation.\n"
)

# 📝 Sample Question
question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

# 🧾 Prompt Formatter
def user_query(qn):
    """
    Formats the user prompt to instruct the model to explain as if the user is a beginner.
    """
    user_prompt = f"Here is the question {qn} - "
    user_prompt += "please treat user as a beginner in that field in which he asked question on"
    return user_prompt

print(user_query(question))  # Optional: View formatted prompt

# 📤 LLM Response Handler
def get_answer(qn):
    """
    Sends the question to the Ollama LLaMA model and returns a plain-text answer.
    """
    response = ollama.chat(
        model=MODEL_LLAMA,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query(qn)}
        ]
    )

    answer = response['message']['content'].strip()
    return answer

# ✅ Get and print the result
result = get_answer(question)
print(result)
