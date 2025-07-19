import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY in your .env file.")

genai.configure(api_key=api_key)

class ChatAgent:
    def __init__(self, model_name="gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)
        self.chat = self.model.start_chat(history=[])
        self.conversation_history = []
        
    def add_to_history(self, role, content):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("🤖 Gemini Chat Agent")
        print("=" * 50)
        print("Type your message and press Enter to chat.")
        print("Commands:")
        print("  /help     - Show this help message")
        print("  /clear    - Clear conversation history")
        print("  /history  - Show conversation history")
        print("  /quit     - Exit the chat")
        print("=" * 50)
        print()
        
    def show_help(self):
        """Display help information"""
        print("\n📖 Help:")
        print("  Just type your message and press Enter to chat with Gemini.")
        print("  The conversation history is maintained throughout the session.")
        print("  Use /help to see this message again.")
        print("  Use /clear to start a fresh conversation.")
        print("  Use /history to see all messages in the current session.")
        print("  Use /quit to exit.\n")
        
    def clear_history(self):
        """Clear conversation history and start fresh"""
        self.chat = self.model.start_chat(history=[])
        self.conversation_history = []
        print("🗑️  Conversation history cleared.\n")
        
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("📝 No conversation history yet.\n")
            return
            
        print("\n📝 Conversation History:")
        print("-" * 30)
        for i, message in enumerate(self.conversation_history, 1):
            role_icon = "👤" if message["role"] == "user" else "🤖"
            print(f"{i}. {role_icon} {message['role'].title()}: {message['content'][:100]}{'...' if len(message['content']) > 100 else ''}")
        print("-" * 30)
        print()
        
    def send_message(self, message):
        """Send a message to Gemini and get response"""
        try:
            # Add user message to history
            self.add_to_history("user", message)
            
            # Get response from Gemini
            response = self.chat.send_message(message)
            response_text = response.text
            
            # Add assistant response to history
            self.add_to_history("assistant", response_text)
            
            return response_text
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"❌ {error_msg}")
            return None
            
    def run(self):
        """Main chat loop"""
        self.display_welcome()
        
        while True:
            try:
                # Get user input
                user_input = input("👤 You: ").strip()
                
                # Handle commands
                if user_input.lower() == "/quit":
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == "/help":
                    self.show_help()
                    continue
                elif user_input.lower() == "/clear":
                    self.clear_history()
                    continue
                elif user_input.lower() == "/history":
                    self.show_history()
                    continue
                elif user_input == "":
                    continue
                
                # Send message and get response
                print("🤖 Gemini: ", end="", flush=True)
                response = self.send_message(user_input)
                
                if response:
                    print(response)
                print()
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                break

def main():
    """Main function to run the chat agent"""
    try:
        agent = ChatAgent()
        agent.run()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()