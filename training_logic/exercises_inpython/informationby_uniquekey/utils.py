def ask():
    return input("What do you want to do today?\n"+
                   "<R> - Register user\n"+
                   "<S> - Search user\n"+
                   "<D> - Delete user\n"+
                   "<L> - List users\n").upper()

def registerUser(usersDicionary):
    usersDicionary[input("Enter the user's login:\n").upper()] = [input("Enter the user's name: \n").upper(), 
                                                         input("Enter the user's class:\n").upper(),
                                                         int(input("Enter the user's age::\n"))]