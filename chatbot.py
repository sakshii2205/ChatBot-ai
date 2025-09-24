# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! 😃"
    elif "your name" in user_input:
        return "I'm a simple chatbot created in Python."
    elif "how's the weather" in user_input:
        return "It's great today."
    elif "will there be any rain today?" in user_input:
        return "no, it's all clear today."
    elif "how are you feeling today?" in user_input:
        return "it's all okiesh today."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day! 👋"
    else:
        return "Sorry, I don't understand that."

def main():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    main()