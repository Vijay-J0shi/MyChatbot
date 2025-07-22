from chatbot.redis_manager import load_history, clear_history
from chatbot.chatbot_core import handle_chat

def main():
    history = load_history()
    while True:
        user_input = input("\\nVijay: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "clear":
            clear_history()
            history = load_history()
            continue
        history = handle_chat(user_input, history)

if __name__ == "__main__":
    main()
