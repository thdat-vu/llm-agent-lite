# llm-agent-lite

🚀 **A lightweight, interactive chat agent powered by Google Gemini AI**

A Python-based CLI chat application that provides a seamless conversational experience with Google's Gemini AI, featuring a beautiful dark-themed interface that matches the official Gemini CLI design. Includes conversation history, command system, and a professional interface - perfect for developers, researchers, or anyone who wants to chat with AI from the terminal.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Gemini](https://img.shields.io/badge/Powered%20by-Gemini%20AI-orange.svg)](https://aistudio.google.com/)

## ✨ Features

- 🤖 **Interactive Chat**: Chat with Gemini AI in real-time
- 💬 **Conversation History**: Maintains context throughout the session
- 📝 **Command System**: Built-in commands for managing the chat
- 🎨 **Gemini-Style UI**: Beautiful dark-themed interface matching official Gemini CLI
- 🔄 **Session Management**: Clear history, view conversation, and more
- 📊 **Status Bar**: Real-time model info and context tracking
- 🎯 **Smart Warnings**: Directory-aware recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llm-agent-lite.git
   cd llm-agent-lite
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   Create a `.env` file in the project root:
   ```bash
   echo "GOOGLE_API_KEY=your-api-key-here" > .env
   ```

## Usage

Start the interactive chat:
```bash
python3 ai_agent.py
```

Or run the demo script to see the chat agent in action:
```bash
python3 demo.py
```

Test the new UI layout (no API required):
```bash
python3 test_ui.py
```

### Commands

Once in the chat interface, you can use these commands:

- **Just type your message** - Chat with Gemini AI
- `/help` - Show help information
- `/clear` - Clear conversation history and start fresh
- `/history` - View all messages in the current session
- `/quit` - Exit the chat

### Example Session

```
GEMINI

Tips for getting started:
  • Ask questions, edit files, or run commands.
  • Be specific for the best results.
  • /help for more information.

┌─────────────────────────────────────────────────────────────┐
│ You are running Gemini CLI in your home directory. It is
│ recommended to run in a project-specific directory.
└─────────────────────────────────────────────────────────────┘

> Hello! How are you today?
+ Hello! I'm doing well, thank you for asking. I'm ready to help you with any questions or tasks you might have. How can I assist you today?

> Can you explain quantum computing in simple terms?
+ Sure! Quantum computing is like having a computer that can be in multiple states at once, rather than just 0 or 1 like regular computers...

────────────────────────────────────────────────────────────────────────────────
~ llm-agent-lite no sandbox (see /docs)gemini-2.5-flash (99% context left) | * 0 errors (ctrl+o for details)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 Notes

- **API Key Required**: You need a Google Gemini API key to use this application. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
- **Conversation Context**: The chat maintains conversation context throughout the session for a more natural experience.
- **Exit Commands**: Use `/quit` or Ctrl+C to exit the chat at any time.
- **Model**: Uses Gemini 2.5 Flash by default for optimal performance and cost-effectiveness.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
