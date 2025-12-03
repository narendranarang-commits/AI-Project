#!/usr/bin/env python3
"""
Advanced Mistral AI Bot
A feature-rich chatbot powered by Mistral AI with system prompts and conversation management
"""

import os
from mistralai import Mistral

# Initialize the Mistral client with your API key from environment
API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "MISTRAL_API_KEY environment variable not set. Set it before running the bot."
    )
client = Mistral(api_key=API_KEY)

# System prompt to define bot behavior
SYSTEM_PROMPT = """You are a helpful, friendly, and knowledgeable AI assistant powered by Mistral AI. 
You provide accurate information, engage in thoughtful conversations, and help users with various tasks.
You are respectful, honest, and always try to be as helpful as possible."""

def create_system_message():
    """Create the system message for the conversation"""
    return {
        "role": "user",
        "content": "You are a helpful assistant. Please respond to all queries helpfully."
    }

def chat_with_bot(system_prompt=None):
    """Main chat loop for the advanced Mistral AI bot"""
    print("=" * 70)
    print("🤖 Welcome to Advanced Mistral AI Bot!")
    print("Commands:")
    print("  - Type 'quit' or 'exit' to exit")
    print("  - Type 'clear' to clear conversation history")
    print("  - Type 'help' for more information")
    print("=" * 70)
    print()
    
    conversation_history = []
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Handle special commands
            if user_input.lower() == 'quit' or user_input.lower() == 'exit':
                print("Bot: Goodbye! Thank you for chatting with me! 👋")
                break
            
            elif user_input.lower() == 'clear':
                conversation_history = []
                print("Bot: Conversation history cleared! Starting fresh.")
                print()
                continue
            
            elif user_input.lower() == 'help':
                print("Bot: Available commands:")
                print("  - 'quit' or 'exit': Exit the chat")
                print("  - 'clear': Clear conversation history")
                print("  - 'history': Show conversation count")
                print()
                continue
            
            elif user_input.lower() == 'history':
                print(f"Bot: You have {len(conversation_history)} messages in history.")
                print()
                continue
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Add user message to history
            conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from Mistral AI
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=conversation_history,
                max_tokens=1024
            )
            
            # Extract the assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant message to history
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            print(f"Bot: {assistant_message}")
            print()
            
        except KeyError:
            print("Bot: Error - Invalid API key. Please check your API key.")
            break
        except Exception as e:
            print(f"Bot: An error occurred: {str(e)}")
            print("Please try again.")
            print()

if __name__ == "__main__":
    chat_with_bot(system_prompt=SYSTEM_PROMPT)
