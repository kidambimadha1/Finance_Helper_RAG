# 💰 FinanceHelper – AI-Powered Personal Finance Assistant (RAG + LLaMA3.2)

**FinanceHelper** is an offline, privacy-first AI assistant that helps you track and understand your personal expenses. It uses **Retrieval-Augmented Generation (RAG)** 
and your own local **LLaMA 3.2 model (via Ollama)** to answer queries like:

> 🧠 *“What is my total food expense?”*  
> 🧠 *“How much did I spend on travel last week?”*

---

## 🚀 Features

- 📂 Drag-and-drop your expense data into the `/data` folder (mainly .txt and .csv)
- 🔍 Fast semantic search using **FAISS vector DB**
- 🧠 Query handled by **local LLaMA3.2** using **Ollama**
- 🔒 No cloud APIs – Fully offline and private
- 🌐 Frontend to ask questions and see instant responses

---

** How It Works (RAG Pipeline) **:

1) Text Loader: Reads your .txt and .csv data

2) Chunking: Breaks text into small paragraphs

3) Embedding: Each chunk converted to vector via SentenceTransformers

4) FAISS Index: Stores all embeddings

5) Query: Your question is embedded and top matches are selected

6) RAG Prompt: Sends relevant context + query to LLaMA 3.2 via Ollama

7) Answer: Response shown on the frontend




