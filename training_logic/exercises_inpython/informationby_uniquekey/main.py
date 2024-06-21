from module.utils import *

def main():
    users = {}
    db_directory = r"C:\Users\Dylan\Documents\devs\training_logic\exercises_inpython\informationby_uniquekey\users_database"
    file_path = os.path.join(db_directory, "db.txt")
    
    option = ask()
    while option in ["R", "E", "S", "D", "L", "F"]:
        if option == "R":
            register_user(users, file_path)
            save_db(users, file_path)
            users.clear()
        elif option == "S":
            search_user(file_path)
        elif option == "D":
            delete_user(users)
        elif option == "L":
            list_users(users)
        elif option == "F":
            print("Program ended")
            break
        else:
            print("An error occurred, please try again.")
            break
        option = ask()

if __name__ == "__main__":
    main()