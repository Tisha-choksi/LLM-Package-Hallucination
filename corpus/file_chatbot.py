import nltk
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

def chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Tokenize the input
        tokens = word_tokenize(user_input)
        
        if "hello" in tokens or "hi" in tokens:
            print("Chatbot: Hello! How can I help you today?")
        elif "how" in tokens and "are" in tokens:
            print("Chatbot: I'm just a program, but thanks for asking!")
        elif "your" in tokens and "name" in tokens:
            print("Chatbot: I'm a chatbot created by OpenAI.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()