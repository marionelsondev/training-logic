import os

def ask():
    return input("Choose an option:\n"+"<R> - Register user\n"+"<E> - Edit user\n"+"<S> - Search user\n"+"<D> - Delete user\n"+"<L> - List users\n""<F> - End program\n").upper()

def register_user(users_dictionary, file_path):
    login = input("Enter the user login:\n").upper()
    if login in users_dictionary or user_exists_in_db(login, file_path):
        print(f"This user {login} already exists in the database\n"+"To edit the user, select option <E>\n")
        return

    name = input("Enter the user name: \n").upper()
    user_sector = input("Enter the user sector:\n").upper()
    age = int(input("Enter the user age:\n"))

    users_dictionary[login] = [name, user_sector, age]
    print(f"User {login} registered successfully.\n")

def save_db(users_dictionary):
    db_directory = r"C:\Users\Dylan\Documents\devs\training_logic\exercises_inpython\informationby_uniquekey\users_database"

    if not os.path.exists(db_directory):
        os.makedirs(db_directory)
    
    file_path = os.path.join(db_directory, "db.txt")
    
    with open(file_path, "a") as user_database:
        for login, user_info in users_dictionary.items():
                user_database.write (f"{login}:{user_info}\n")
                print(f"User {login} has been saved in database!\n")

def user_exists_in_db(login, file_path):
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, "r") as user_database:
        for line in user_database:
            user_key = line.split(":")[0]
            if user_key.strip() == login:
                return True
    return False


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