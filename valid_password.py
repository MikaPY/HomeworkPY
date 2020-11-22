def valid_pass():
    while True:
        password = input("Enter a password: ")
        if len(password) < 12:
            print("Your password must consist of 12 characters or more.")
        elif not password.isdigit():
            print("Your password must have a number")
        elif not password.isupper(): 
            print("Your password must be capitalized")
        else:
            print("Your password is good")
            break

valid_pass()