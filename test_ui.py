#!/usr/bin/env python3
"""
Test script to demonstrate the new Gemini-style UI
This script shows the UI layout without making actual API calls.
"""

import os
import sys

def display_gemini_ui():
    """Display the Gemini-style UI layout"""
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Header
    print("\033[38;2;135;206;235m" + "GEMINI" + "\033[0m")
    print()
    
    # Tips
    print("\033[38;2;255;255;255mTips for getting started:\033[0m")
    print("  • Ask questions, edit files, or run commands.")
    print("  • Be specific for the best results.")
    print("  • /help for more information.")
    print()
    
    # Directory warning (if in home directory)
    current_dir = os.getcwd()
    home_dir = os.path.expanduser("~")
    
    if current_dir == home_dir:
        print("\033[38;2;255;165;0m┌─────────────────────────────────────────────────────────────┐\033[0m")
        print("\033[38;2;255;165;0m│\033[0m You are running Gemini CLI in your home directory. It is")
        print("\033[38;2;255;165;0m│\033[0m recommended to run in a project-specific directory.")
        print("\033[38;2;255;165;0m└─────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    # Example conversation
    print("\033[38;2;255;255;255m> \033[0mdescribe for me how AI works in 2 sentences.")
    print("\033[38;2;0;255;0m+ \033[0mArtificial intelligence systems learn from vast amounts of data to identify patterns, make predictions, and decide on actions. By processing this information, they can perform tasks that traditionally require human intelligence, such as understanding language, driving cars, and generating creative content.")
    print()
    
    # Status bar
    terminal_width = 80
    status_left = f"~ {os.path.basename(current_dir)} no sandbox (see /docs)"
    status_right = "gemini-2.5-flash (99% context left) | * 0 errors (ctrl+o for details)"
    padding = terminal_width - len(status_left) - len(status_right)
    
    print("\033[38;2;100;100;100m" + "─" * terminal_width + "\033[0m")
    print(f"\033[38;2;100;100;100m{status_left}{' ' * padding}{status_right}\033[0m")
    
    print("\n\033[38;2;255;255;255m✅ UI Demo Complete!\033[0m")
    print("This shows the new Gemini-style interface layout.")

if __name__ == "__main__":
    display_gemini_ui() 