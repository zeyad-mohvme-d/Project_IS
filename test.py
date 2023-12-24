'''
This is the [Vaccination System] project

'''

list_vaccines = ["Corona", "cancer", "Virus C"]
users = [['111', 'zeyad', 'zeyad2005@', 'zoz'],
         ['222', 'sadek', 'sadek2004@', 'sadek20']]
admin_password = "admin"
vaccination_center = [['000', 'ax', 'cairo', list_vaccines]]
registered_users_list = ["Ahmed Adel", "Sadek Rizkallah"]


def login():
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        # check if the email and password is existed
        if user[2] == email and user[3] == password:

            print("\n*******User Existed*******\n\n")

        else:

            print("invalid option..")
            return False

        if role == admin_password:  # Enter the Admin menu
            print("Admin menu\n")

            while True:
                choose = input(
                    "Add Vaccination Center:\nRemove Vaccination Center\nSearch\nShow Registered Users\n:").lower()  # The admin Choose which operation

                if choose == 'add':
                    vac_ID = int(input("Enter the vaccination center ID:"))
                    vac_name = input("Enter the vaccination center name:")
                    vac_address = input(
                        "Enter the vaccination center address:")
                    vaccination_center.append(
                        [vac_ID, vac_name, vac_address, list_vaccines])
                    print("list added")

                elif choose == 'remove':
                    print(vaccination_center)
                    remove_input = int(input(
                        "Enter which list you want to remove:"))
                    removed_center = remove_input - 1
                    vaccination_center.pop(removed_center)

                elif choose == "search":
                    search_input = input(
                        "Please enter the name of the vaccination center:")

                elif choose == 'Show':
                    print(
                        f"those are registered users:{registered_users_list}")

                else:
                    print("invalid option...")
                    break


# *******User Login into the system*******

def user_login():
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        # check if the email and password is existed
        if user[2] == email and user[3] == password:

            print("\n*******User Existed*******\n\n")

            print(vaccination_center)

            print(
                f"Your reservation has been accepted ---->(user ID:444), (vaccination center id:000), (vaccine name: Corona)")

            print("\nYour vaccination date is: 1/1/2024")

            quit()

        else:
            print("User doesn't exist")
            return False


# *********Register to system*********


def register():
    # Take the credintals from the user
    user_ID = input("Please enter your Id:")
    user_name = input("Please Enter your name:")
    user_email = input("Please enter your email:")
    user_password = input("Please enter your password:")
    user_phone_number = int(input("Please enter your phone number:"))
    user_national_id = int(input("Please enter your national id:"))
    # *********save the new user data into the list*********
    users.append([user_ID, user_name, user_email, user_password])
    registered_users_list.append(user_name)
    return True


# ******************
specfiy_who_are_u = input("1-New user\n2-User\n3-admin\n:")

while True:
    if specfiy_who_are_u == '3':
        role = input("Enter admin password:").lower()
        if role == 'admin':
            login()
        else:
            quit()
    elif specfiy_who_are_u == '2':
        user_login()

    elif specfiy_who_are_u == '1':
        register()
        break
