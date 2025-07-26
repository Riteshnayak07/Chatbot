import time
import random

print("ChatBot: Hello! I'm ChatBuddy 🤖. What's your name?")
name = input("You: ")

print(f"ChatBot: Nice to meet you, {name}! Type 'bye' anytime to exit.")

while True:
    user_input = input(f"{name}: ").lower()

    time.sleep(0.5)  # Simulates thinking

    if "hello" in user_input or "hi" in user_input:
        replies = ["Hi there!", "Hey!", "Hello!", "Good to see you!"]
        print("ChatBot:", random.choice(replies))

    elif "how are you" in user_input:
        replies = ["I'm doing great! Thanks for asking 😊", "I'm just a program, but I'm feeling chatty!", "All systems operational!"]
        print("ChatBot:", random.choice(replies))

    elif "your name" in user_input:
        print("ChatBot: I'm ChatBuddy, your friendly chatbot assistant.")

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        print(f"ChatBot: It's currently {now}.")

    elif "bye" in user_input:
        print(f"ChatBot: Bye {name}! Take care 👋")
        break

    else:
        replies = ["Hmm, I didn't quite get that.", "Can you rephrase?", "I'm still learning. Let's try something else!"]
        print("ChatBot:", random.choice(replies))
