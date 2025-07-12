# Ai_QA_Bot

## 🤖 Beginner-Friendly LLM Q&A Assistant

This project uses a local open-source LLM (like LLaMA 3.2 via Ollama) to answer programming or general questions in **simple beginner-friendly language**.

---

## 🧠 What It Does

- Takes a user question (you can type any Python or tech question)
- Formats it so the model explains the answer as if talking to a **beginner**
- Uses the `ollama` library to query the **LLaMA 3.2** model
- Returns and prints a clean, understandable explanation

---

## 📄 Example Use Case

**Input:**
```python
yield from {book.get("author") for book in books if book.get("author")}
