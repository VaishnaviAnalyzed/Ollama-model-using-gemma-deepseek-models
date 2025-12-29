# Local LLM Interface: Gemma & DeepSeek-R1

A Streamlit-powered local LLM interface utilizing Ollama to run Gemma and DeepSeek-R1 models. Features a clean chat UI for real-time interaction with lightweight, high-performance AI directly on your local machine. 🚀

## 🛠️ Features
* **Local Execution:** No API keys required; 100% private.
* **Model Selection:** Easily switch between Google's **Gemma** and DeepSeek's **R1 (1.5B)**.
* **Streamlit UI:** A simple, ChatGPT-like interface for chatting with your models.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and running.

### 2. Install Models
Open your terminal and pull the models used in this repo:
```bash
ollama pull gemma:2b
ollama pull deepseek-r1:1.5b
