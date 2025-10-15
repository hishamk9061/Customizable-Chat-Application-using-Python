import os
from datetime import datetime

def clear_screen():
    # Clears the console screen (works on Windows and Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def save_chat(chat_history, filename):
    """Save chat messages to a file."""
    with open(filename, 'a', encoding='utf-8') as file:
        for line in chat_history:
            file.write(line + '\n')
    print(f"💾 Chat saved to {filename}\n")

def get_timestamp():
    """Return current time as formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def chat_app():
    print("💬 Welcome to the Customizable Chat App!")
    print("Choose mode:")
    print("1. Personal Chat 💕")
    print("2. Business Chat 💼")
    mode = input("Enter your choice (1 or 2): ")

    if mode == "1":
        chat_type = "Personal"
        filename = "personal_chat.txt"
        print("\nYou selected Personal Chat Mode 💕\n")
    elif mode == "2":
        chat_type = "Business"
        filename = "business_chat.txt"
        print("\nYou selected Business Chat Mode 💼\n")
    else:
        print("Invalid choice. Defaulting to Personal Mode.")
        chat_type = "Personal"
        filename = "personal_chat.txt"

    user1 = input("Enter username for User 1: ")
    user2 = input("Enter username for User 2: ")

    print("\nType your messages below! (Type 'exit' to quit, 'clear' to clear screen, 'save' to save chat)\n")

    chat_history = []

    turn = 0  # 0 = user1's turn, 1 = user2's turn

    while True:
        current_user = user1 if turn == 0 else user2
        message = input(f"{current_user}: ")

        # Check for commands
        if message.lower() == 'exit':
            print("👋 Exiting chat... Goodbye!")
            break
        elif message.lower() == 'clear':
            clear_screen()
            continue
        elif message.lower() == 'save':
            save_chat(chat_history, filename)
            continue

        # Format message depending on mode
        timestamp = get_timestamp()
        if chat_type == "Personal":
            formatted_message = f"[💕 {current_user} at {timestamp}]: {message}"
        else:
            formatted_message = f"[{timestamp} | {current_user}]: {message}"

        print(formatted_message)
        chat_history.append(formatted_message)

        # Switch turns
        turn = 1 - turn

    # Save chat at the end automatically
    save_chat(chat_history, filename)

# Run the chat app
if __name__ == "__main__":
    chat_app()
