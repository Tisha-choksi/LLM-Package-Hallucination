import keyring

def store_password(service, username, password):
    keyring.set_password(service, username, password)

def retrieve_password(service, username):
    return keyring.get_password(service, username)

if __name__ == "__main__":
    service = input("Enter the service name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    store_password(service, username, password)
    print("Password stored.")

    print("Retrieving password...")
    retrieved = retrieve_password(service, username)
    print(f"Retrieved password: {retrieved}")
