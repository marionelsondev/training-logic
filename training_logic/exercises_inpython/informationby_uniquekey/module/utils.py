import os

# Function that asks the user what they want to do

def ask():
    return input("Choose an option:\n"+"<R> - Register user\n"+"<E> - Edit user\n"+"<S> - Search user\n"+"<D> - Delete user\n"+"<L> - List users\n""<F> - End program\n").upper()

# Function to register the user within the dictionary and check if the key (login) already exists in the dictionary or database

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

# Edit user record

def edit_user(file_path):
    login = input("Enter the login of the user you want to edit:\n").upper()
    if not user_exists_in_db(login, file_path):
        print(f"User {login} not found")
        return
    
    name = input("Enter the new user name: \n").upper()
    user_sector = input("Enter the new user sector: \n").upper()
    age = int(input("Enter the new user age: \n"))

    updated_user_info = [name, user_sector, age]

    with open(file_path, "r") as user_database:
        lines = user_database.readlines()
        
    with open(file_path, "w") as user_database:
        for line in lines:
            user_key, _ = line.strip().split(":", 1)
            if user_key.strip() == login:
                user_database.write(f"{login}:{updated_user_info}\n")
                print(f"User {login} updated successfully. \n")
            else:
                user_database.write(line)

# Function that searches for and retrieves the requested user's record

def search_user(file_path):
    login = input("Enter the user's login to search:\n").upper()
    user_info = get_user_info_from_db(login, file_path)
    if user_info:
        print(f"User found!\n------------------------\nLogin: {login}\nName: {user_info[0]}\nSector: {user_info[1]}\nAge: {user_info[2]}\n------------------------")
    else:
        print("User not found")

# Delete the user from the database

def delete_user(file_path):
    login = input("Enter the login of the user you want to delete:\n").upper()
    if not user_exists_in_db(login, file_path):
        print(f"Could not delete user.\nReason: User {login} not found")
        return
    
    with open(file_path, "r") as user_database:
        lines = user_database.readlines()
    
    with open(file_path, "w") as user_database:
        for line in lines:
            user_key, _ = line.split(":")
            if user_key.strip() != login:
                user_database.write(line)
            else:
                print(f"User {login} deleted from database") 

# List all users that exist in the database

def list_users(file_path):
    if not os.path.exists(file_path):
        print("Database file does not exist.")
        return

    with open(file_path, "r") as user_database:
        lines = user_database.readlines()
        if not lines:
            print("No users registered")
            return
        
        for line in lines:
            login, user_info = line.strip().split(":", 1)
            user_info = eval(user_info.strip())
            print(f"------------------------\nLogin: {login}\nName: {user_info[0]}\nSector: {user_info[1]}\nAge: {user_info[2]}\n------------------------")

# Function that saves the user's record in the database

def save_db(users_dictionary, file_path):
    db_directory = r"C:\Users\Dylan\Documents\devs\training_logic\exercises_inpython\informationby_uniquekey\users_database"

    if not os.path.exists(db_directory):
        print("Database file does not exist.")
        os.makedirs(db_directory)
    
    file_path = os.path.join(db_directory, "db.txt")
    
    with open(file_path, "a") as user_database:
        for login, user_info in users_dictionary.items():
            user_database.write (f"{login}:{user_info}\n")
            print(f"User {login} has been saved in database!\n")

# Function that validates if the user exists in the database

def user_exists_in_db(login, file_path):
    if not os.path.exists(file_path):
        print("Database file does not exist.")
        return False
    
    with open(file_path, "r") as user_database:
        for line in user_database:
            user_key = line.split(":")[0]
            if user_key.strip() == login:
                return True
    return False

# Function to extract detailed information from the entered login

def get_user_info_from_db(login, file_path):
    if not os.path.exists(file_path):
        print("Database file does not exist.")
        return None
    with open(file_path, "r") as user_database:
        for line in user_database:
            user_key, user_info = line.split(":")
            if user_key.strip() == login:
                return eval(user_info.strip())
    return None