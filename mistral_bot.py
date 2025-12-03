#!/usr/bin/env python3
"""
Mistral AI Bot
A simple chatbot powered by Mistral AI
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

def chat_with_bot():
    """Main chat loop for the Mistral AI bot"""
    print("=" * 60)
    print("Welcome to Mistral AI Bot!")
    print("Type 'quit' or 'exit' to stop the conversation")
    print("=" * 60)
    print()
    
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("Bot: Goodbye! Thanks for chatting with me!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get response from Mistral AI
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=conversation_history
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
            
        except Exception as e:
            print(f"Error: Failed to get response from Mistral AI")
            print(f"Details: {str(e)}")
            print()

if __name__ == "__main__":
    chat_with_bot()
