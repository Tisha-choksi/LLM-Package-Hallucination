import pickle

def load_habits():
    try:
        with open('habits.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_habits(habits):
    with open('habits.pkl', 'wb') as f:
        pickle.dump(habits, f)

if __name__ == "__main__":
    habits = load_habits()
    while True:
        action = input("Enter 'add' to add a habit, 'show' to view, or 'exit': ")
        if action == 'add':
            habit = input("Enter habit: ")
            habits[habit] = habits.get(habit, 0) + 1
            save_habits(habits)
        elif action == 'show':
            print(habits)
        elif action == 'exit':
            break
