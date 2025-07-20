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
        self.current_directory = os.getcwd()
        
    def add_to_history(self, role, content):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
    def display_header(self):
        """Display the Gemini-style header"""
        print("\033[38;2;135;206;235m" + "GEMINI" + "\033[0m")
        print()
        
    def display_tips(self):
        """Display tips for getting started"""
        print("\033[38;2;255;255;255mTips for getting started:\033[0m")
        print("  • Ask questions, edit files, or run commands.")
        print("  • Be specific for the best results.")
        print("  • /help for more information.")
        print()
        
    def display_directory_warning(self):
        """Display directory warning if in home directory"""
        home_dir = os.path.expanduser("~")
        current_dir = os.getcwd()
        
        # Check if we're in the home directory (not in a project)
        if current_dir == home_dir:
            print("\033[38;2;255;165;0m┌─────────────────────────────────────────────────────────────┐\033[0m")
            print("\033[38;2;255;165;0m│\033[0m You are running Gemini CLI in your home directory. It is")
            print("\033[38;2;255;165;0m│\033[0m recommended to run in a project-specific directory.")
            print("\033[38;2;255;165;0m└─────────────────────────────────────────────────────────────┘\033[0m")
            print()
        
    def display_status_bar(self):
        """Display status bar at bottom"""
        model_name = "gemini-2.5-flash"
        context_left = "99%"  # Placeholder - could be calculated based on actual usage
        errors = "0"  # Placeholder
        
        status_left = f"~ {os.path.basename(self.current_directory)} no sandbox (see /docs)"
        status_right = f"{model_name} ({context_left} context left) | * {errors} errors (ctrl+o for details)"
        
        # Calculate padding to align status bar
        terminal_width = 80  # Default terminal width
        padding = terminal_width - len(status_left) - len(status_right)
        
        print("\033[38;2;100;100;100m" + "─" * terminal_width + "\033[0m")
        print(f"\033[38;2;100;100;100m{status_left}{' ' * padding}{status_right}\033[0m")
        
    def show_help(self):
        """Display help information"""
        print("\n\033[38;2;255;255;255m📖 Help:\033[0m")
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
        print("\033[38;2;255;255;255m🗑️  Conversation history cleared.\033[0m\n")
        
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("\033[38;2;255;255;255m📝 No conversation history yet.\033[0m\n")
            return
            
        print("\n\033[38;2;255;255;255m📝 Conversation History:\033[0m")
        print("\033[38;2;100;100;100m" + "─" * 50 + "\033[0m")
        for i, message in enumerate(self.conversation_history, 1):
            role_icon = "👤" if message["role"] == "user" else "🤖"
            content_preview = message['content'][:80] + ('...' if len(message['content']) > 80 else '')
            print(f"{i}. {role_icon} {message['role'].title()}: {content_preview}")
        print("\033[38;2;100;100;100m" + "─" * 50 + "\033[0m")
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
            print(f"\033[38;2;255;100;100m❌ {error_msg}\033[0m")
            return None
            
    def run(self):
        """Main chat loop"""
        # Clear screen and display header
        os.system('clear' if os.name == 'posix' else 'cls')
        self.display_header()
        self.display_tips()
        self.display_directory_warning()
        
        while True:
            try:
                # Display status bar
                self.display_status_bar()
                
                # Get user input with styled prompt
                user_input = input("\033[38;2;255;255;255m> \033[0m").strip()
                
                # Handle commands
                if user_input.lower() == "/quit":
                    print("\033[38;2;255;255;255m👋 Goodbye!\033[0m")
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
                print("\033[38;2;0;255;0m+ \033[0m", end="", flush=True)
                response = self.send_message(user_input)
                
                if response:
                    print(response)
                print()
                
            except KeyboardInterrupt:
                print("\n\n\033[38;2;255;255;255m👋 Goodbye!\033[0m")
                break
            except EOFError:
                print("\n\n\033[38;2;255;255;255m👋 Goodbye!\033[0m")
                break

def main():
    """Main function to run the chat agent"""
    try:
        agent = ChatAgent()
        agent.run()
    except KeyboardInterrupt:
        print("\n\033[38;2;255;255;255m👋 Goodbye!\033[0m")
    except Exception as e:
        print(f"\033[38;2;255;100;100m❌ Error: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()