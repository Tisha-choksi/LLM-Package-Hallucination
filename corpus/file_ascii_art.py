import pyfiglet
import sys

def start_game():
    print(pyfiglet.figlet_format("Adventure Game"))
    print("Welcome to the text adventure game!")
    print("You find yourself in a dark room.")
    while True:
        action = input("What do you want to do? (look, exit): ").strip().lower()
        if action == "look":
            print("You see a door and a window.")
        elif action == "exit":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid action.")

if __name__ == "__main__":
    start_game()
