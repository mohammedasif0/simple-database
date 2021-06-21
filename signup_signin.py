import sys

def alphanumeric(password):
    return password.isalnum() and not password.isalpha() and not password.isdigit()

handle =open("register.txt",'a')

print("welcome to Sample solutions ")
up_in=input("Signup (up) or signin (in)  : ").lower()


#SIGNUP ; check the password and registering username and password to .txt file
if up_in == "up":
    print("Welcome to sign up portal")
    user_name=input("Choose your user name : ")
    handle = open("register.txt", 'r')
    for line in handle:
        items = line.split(":")
        reg_user_name = items[0]
        if user_name == reg_user_name:
            print("User name already exists")
            break
        else:
            a = False
            while not a:
                password = input("Enter your password : ")

                if password[0] != password[0].upper():
                    print("Please enter password  start with capital alphabet")
                else:
                    a = True

                    b = False
                    while not b:
                        if len(password) < 8:
                            print("Please enter password with minimum 8 characters")
                        else:
                            b = True
                            c = False
                            while not c:
                                if alphanumeric(password) is not True:
                                    print("Please enter a alphanumric password")
                                else:
                                    c = True
                                    handle = open("register.txt", 'a')
                                    handle.write(user_name + ":")
                                    handle.write(password+":\n")
                                    handle.close()
                                    print("Account successfully created :")

                                    sys.exit()

                                b = False
                                break

                        a = False
                        break

#SIGNIN : retrieving the registered username, password and checking whether it matches

elif up_in == "in":
    user_name=input("Enter your Username : ")
    password=input("Enter your password : ")
    handle = open("register.txt", 'r')
    for line in handle:
        items = line.split(":")
        reg_user_name = items[0]
        reg_password=items[1]

        p=False
        while not p:
            if password==reg_password and user_name==reg_user_name:
                print("Login successful")
                p=True
                break
            elif password==reg_password and user_name!=reg_user_name:
                print(" invalid username!!!")
                break
            elif password!=reg_password and user_name==reg_user_name:
                print("Incorrect password")
                break
            break

