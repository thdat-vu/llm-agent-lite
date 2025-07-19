# llm-agent-lite

An interactive chat agent using Google Gemini API, similar to Gemini CLI.

## Features

- 🤖 **Interactive Chat**: Chat with Gemini AI in real-time
- 💬 **Conversation History**: Maintains context throughout the session
- 📝 **Command System**: Built-in commands for managing the chat
- 🎨 **User-Friendly Interface**: Clean, emoji-enhanced interface
- 🔄 **Session Management**: Clear history, view conversation, and more

## Setup

1. **Clone the repository**
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or
   pip install google-generativeai python-dotenv
   ```
4. **Create a `.env` file** in the project root:
   ```
   GOOGLE_API_KEY=your-api-key-here
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

### Commands

Once in the chat interface, you can use these commands:

- **Just type your message** - Chat with Gemini AI
- `/help` - Show help information
- `/clear` - Clear conversation history and start fresh
- `/history` - View all messages in the current session
- `/quit` - Exit the chat

### Example Session

```
🤖 Gemini Chat Agent
==================================================
Type your message and press Enter to chat.
Commands:
  /help     - Show this help message
  /clear    - Clear conversation history
  /history  - Show conversation history
  /quit     - Exit the chat
==================================================

👤 You: Hello! How are you today?
🤖 Gemini: Hello! I'm doing well, thank you for asking. I'm ready to help you with any questions or tasks you might have. How can I assist you today?

👤 You: Can you explain quantum computing in simple terms?
🤖 Gemini: Sure! Quantum computing is like having a computer that can be in multiple states at once, rather than just 0 or 1 like regular computers...
```

## Notes
- Requires a Google Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
- The chat maintains conversation context throughout the session.
- Use Ctrl+C to exit at any time.
