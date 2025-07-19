#!/usr/bin/env python3
"""
Demo script showing how to use the ChatAgent class programmatically.
This is useful for testing or integrating the chat agent into other applications.
"""

from ai_agent import ChatAgent

def demo_chat():
    """Demonstrate the chat functionality"""
    print("🚀 Starting Chat Agent Demo")
    print("=" * 40)
    
    # Create a chat agent
    agent = ChatAgent()
    
    # Demo messages
    demo_messages = [
        "Hello! Can you introduce yourself?",
        "What's the weather like today?",
        "Can you help me write a simple Python function?",
        "/history",
        "/clear",
        "Now let's start fresh. What's 2+2?"
    ]
    
    print("Sending demo messages to the chat agent...\n")
    
    for message in demo_messages:
        print(f"👤 Sending: {message}")
        
        if message.startswith("/"):
            # Handle commands
            if message == "/history":
                agent.show_history()
            elif message == "/clear":
                agent.clear_history()
            else:
                print("🤖 (Command executed)")
        else:
            # Send message to Gemini
            response = agent.send_message(message)
            if response:
                print(f"🤖 Response: {response[:100]}{'...' if len(response) > 100 else ''}")
        
        print("-" * 40)
    
    print("✅ Demo completed!")

if __name__ == "__main__":
    demo_chat() 