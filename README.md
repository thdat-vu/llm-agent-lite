# llm-agent-lite

A simple demo for an LLM chat agent using Google Gemini API.

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

Run the agent:
```bash
python3 ai_agent.py
```

## Notes
- Requires a Google Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
- The agent will print a response from the Gemini model.
