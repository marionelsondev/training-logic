from module.utils import *

def main():
    users = {}
    option = ask()
    while option == "R" or option == "S" or option == "D" or  option == "L" or option == "F":
        if option == "R":
            register_user(users)
            save_db(users)
        elif option == "S":
            search_user(users)
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