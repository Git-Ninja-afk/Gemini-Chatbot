![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?logo=google&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-Tool-black?logo=windowsterminal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

# 🤖 Gemini AI Chatbot

> A conversational AI chatbot powered by Google Gemini 1.5 Flash. Chat naturally, save conversations, and experience the power of Gemini AI — all from your terminal.

## ✨ Features

- 💬 Natural multi-turn conversation with memory
- 🧠 Powered by Google Gemini 1.5 Flash
- 💾 Save chat history to a text file
- 🗑️ Clear conversation history anytime
- ⚡ Fast responses with streaming output
- 🔐 Secure API key management with .env

## 📋 Prerequisites

- Python 3.9+
- Google Gemini API Key ([Get it here](https://aistudio.google.com/apikey))

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Git-Ninja-afk/gemini-chatbot.git
cd gemini-chatbot

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Add your Gemini API key to .env file

# Run the chatbot
python chatbot.py
```

## 🔑 Environment Variables

```bash
cp .env.example .env
```

Open `.env` and add your key:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🎮 Usage

```
🤖 GEMINI AI CHATBOT
==================================================
Powered by Google Gemini 1.5 Flash
Commands: 'quit' to exit | 'save' to save chat | 'clear' to clear history
==================================================

 You: What is open source?

🤖 Gemini: Open source refers to software whose source code is made 
available to the public for use, modification, and distribution...

 You: save
✅ Chat saved to chat_20260509_143022.txt

 You: quit
👋 Goodbye!
```

## 📁 Project Structure

```
gemini-chatbot/
├── chatbot.py        # Main chatbot application
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore rules
└── README.md         # Documentation
```

## 🗺️ Roadmap

- [ ] Web interface using Streamlit
- [ ] Support for image inputs (Gemini Vision)
- [ ] Multiple personality modes
- [ ] Voice input/output support

## 👨‍💻 About

Built to explore Google Gemini AI API integration and conversational AI development using Python.

## 📜 License

MIT License
