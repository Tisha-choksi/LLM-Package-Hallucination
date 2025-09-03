from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def setup_chatbot():
    chatbot = ChatBot('SimpleBot')
    trainer = ListTrainer(chatbot)
    trainer.train([
        "Hi",
        "Hello!",
        "How are you?",
        "I'm good, thanks!",
        "Goodbye",
        "See you later!"
    ])
    return chatbot

if __name__ == "__main__":
    bot = setup_chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye"]:
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")
