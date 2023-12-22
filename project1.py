list_vaccines = ["Corona", "cancer", "Virus C"]
users = [['111', 'zeyad', 'zeyad2005@', 'zoz']]
admin_password = "admin"
vaccination_center = [['000', 'ax', 'cairo', list_vaccines]]
specfiy_who_are_u = input("Are you user or admin:").lower()


def clear():
    return False


if specfiy_who_are_u == 'admin':
    role = input("Enter admin password:").lower()
    if role == 'admin':
        print("\n")
    else:
        quit()
elif specfiy_who_are_u == 'user':
    print("")
# User login the System


def login():
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        if user[2] == email and user[3] == password:
            print("User Existed")
        else:
            print("User doesn't exist..")
            return False
        if role == admin_password:
            print("Admin menu\n")
            while True:
                choose = input(
                    "Add Vaccination Center:\nRemove Vaccination Center:\n:").lower()
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

                else:
                    print("invalid option...")
                    break

# Register to system


def register():
    user_name = input("Please Enter your name:")
    user_ID = input("Please enter your Id:")
    user_email = input("Please enter your email:")
    user_password = input("Please enter your password:")
    user_phone_number = int(input("Please enter your phone number:"))
    user_national_id = int(input("Please enter your national id:"))
    inputs = []
    inputs.append([user_ID, user_name, user_email, user_password])


if specfiy_who_are_u == 'admin':
    login()
if specfiy_who_are_u == 'user':
    register()
