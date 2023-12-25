'''
This is the [Vaccination System] project

'''

list_vaccines = ["Corona", "cancer", "Virus C"]
users = [['111', 'zeyad', 'zeyad2005@', 'zoz'],  ['222', 'sadek', 'sadek2004@', 'sadek20']]

admin_password = "admin"
vaccination_center = [['000', 'ax', 'cairo', list_vaccines]]
registered_users_list = ["Ahmed Adel", "Sadek Rizkallah"]

lst_login = []
lst_user_login = []

def login():
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        for user_email in user:
            lst_login.append(user_email)
    if email in lst_login:
        if password in lst_login:
            pass
        print(f"User {email} existed")
    else:
        print("user doesn't exist")
        return False

    if role == admin_password:  # Enter the Admin menu
        print("Admin menu\n")
        while True:
            choose = input(
                    "Add Vaccination Center:\nRemove Vaccination Center\nSearch\nShow Registered Users\n:").lower()  # The admin Choose which operation

            if choose == 'add':
                vac_id = int(input("Enter the vaccination center ID:"))
                vac_name = input("Enter the vaccination center name:")
                vac_address = input(
                        "Enter the vaccination center address:")
                vaccination_center.append(
                        [vac_id, vac_name, vac_address, list_vaccines])
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
                for vaccine_name in vaccination_center:
                    for name in vaccine_name:
                        if search_input == name[1]:
                            print(f"The vaccination center name ({search_input} found)")

            elif choose == 'show':
                print(
                    f"those are registered users:{registered_users_list}")

            else:
                print("invalid option...")
                break


# *******User Login into the system*******

def user_login():
    user_id = input("Please enter your id:")
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        for inner in user:
            lst_user_login.append(inner)

    if email in lst_user_login:
        if password in lst_user_login:

            print("\n*******User Existed*******\n\n")

            print(vaccination_center)

            print(
                    f"Your reservation has been accepted ---->(user ID:{user_id}), (vaccination center id:000), (vaccine name: Corona)")

            print("\nYour vaccination date is: 1/1/2024")

            return True

    else:
        print(f"{email} User doesn't exist\n")
        return False


# *********Register to system*********


def register():
    # Take the credintals from the user
    user_ID = input("Please enter your Id:")
    user_name = input("Please Enter your name:")
    email = input("Please enter your email:")
    password = input("Please enter your password:")
    user_phone_number = int(input("Please enter your phone number:"))
    user_national_id = int(input("Please enter your national id:"))
    # *********save the new user data into the list*********
    users.append([user_ID, user_name, email, password])
    registered_users_list.append(user_name)


while True:
    specfiy_who_are_u = input("1-New user\n2-User\n3-admin\n:")

    if specfiy_who_are_u == '3':
        while True:

            role = input("Enter admin password:").lower()
            if role == 'admin':
                login()
        else:
            quit()
    elif specfiy_who_are_u == '2':
        user_login()
    elif specfiy_who_are_u == '1':
        register()
