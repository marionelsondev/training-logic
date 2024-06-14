from informationby_uniquekey.utils import *

users = {}
option = ask()
while option == "R" or option == "S" or option == "D" or  option == "L":
    if option == "R":
        registerUser(users)
    option = ask()
print(users)