def ask():
    return input("What do you want to do today?\n"+
                   "<R> - Register user\n"+
                   "<S> - Search user\n"+
                   "<D> - Delete user\n"+
                   "<L> - List users\n"
                   "<F> - Finish program\n").upper()

def register_user(users_dictionary):
    name = input("Enter the user's name: \n").upper()
    user_class = input("Enter the user's class:\n").upper()
    age = int(input("Enter the user's age::\n"))
    login = input("Enter the user's login:\n").upper()
    users_dictionary[login] = [name, user_class, age]
    
def search_user(users_dictionary):
    login = input("Enter the user's login to search:\n").upper()
    if login in users_dictionary:
        user_info = users_dictionary[login]
        print(f"User found!\n------------------------\nLogin: {login}\nName: {user_info[0]}\nClass: {user_info[1]}\nAge: {user_info[2]}\n------------------------")
    else:
        print("User not found")

def delete_user(users_dictionary):
    login = input("Enter the login of the user you want to delete:\n").upper()
    if login in users_dictionary:
        del users_dictionary[login]
        print(f"User {login} deleted")
    else:
        print(f"Could not delete user.\n" + "Reason: User not found")

def list_users(users_dictionary):
    if users_dictionary:
        for login, details in users_dictionary.items():
            print(f"------------------------\nLogin: {login}\nName: {details[0]}\nClass: {details[1]}\nAge: {details[2]}\n------------------------")
    else:
        print("No users registered")
