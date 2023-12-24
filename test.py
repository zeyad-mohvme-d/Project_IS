vaccines = ["Corona", "Cancer", "Virus C"]
users = [
    ['usr1', 'usr2', 'usr3', 'usr4'], # username
    ['1', '2', '3', '4'], # ID
    ['nat1', 'nat2', 'nat3', 'nat4'], # national ID
    ['pass1', 'pass2', 'pass3', 'pass4'], # password
    ['email1', 'email2', 'email3', 'email4'], # email
    ['phone1', 'phone2', 'phone3', 'phone4'] # phone number
]
admins = [
    ["admin1", 'admin2'], # name
    ['1', '2'], # ID
    ['pass1', 'pass2'], # password
    ['email1', 'email2'] # email
]
vaccination_center = { # names: IDs
    'Center1': '1',
    'Center2': '2',
    'Center3': '3' 
}
reservation = [
    [], # user ID
    [], # vaccination center ID
    []  # vaccine name
]
requests = []
def admin_do():
    pass
def user_do(user_id):
    while True:
        print("Here is the options menu: \n1. Vaccination Centers\n2. Reserve a vaccination\n3. Exit")
        option = input("Enter your choice: ")
        if option.strip() == '1':
            for i in vaccination_center:
                print(i)
        elif option.strip() == '2':
            print("To reserve a vaccination you should specify where the center is and the vaccine name: ")
            get_center = input("Enter the name of the center: ")
            get_vaccine = input("Enter the name of the vaccine: ")
            ch = input("Do you want to proceed in reservation? (y/n): ").strip().lower()
            if ch == 'y':
                reservation[0].append(vaccination_center.get(user_id))
                reservation[1].append(vaccination_center.get(get_center))
                reservation[2].append(vaccination_center.get(get_vaccine))
                print("Reservation finished")
            elif ch == 'n':
                pass
            else: print("Invalid input")

        elif option.strip() == '3':
            break
        else: print("Invalid input")

def register():
    name = input("Please Enter a username: ")
    users[0].append(name)

    user_id = input("Please Enter your ID: ")
    users[1].append(user_id)

    national_id = input("Please enter your national id:")
    users[2].append(national_id.strip())

    password = input("Please Enter a strong password: ")
    users[3].append(password)

    email = input("Please Enter your email: ")
    users[4].append(email)

    phone_number = input("Please enter your phone number:")
    users[5].append(phone_number)

def login():
    while True:
        option = input("Do you want to log in as an admin or a user?\nType 'a' for admin and 'u' for user: ")
        if option.strip().lower() == 'a':
            pass
        elif option.strip().lower() == 'u':
            get_name = input("Enter your username: ")
            get_id = input("Enter your ID: ")
            get_password = input("Enter your password: ")
            if users[0].count(get_name) and users[1].count(get_id) and users[3].count(get_password):
                print(f"Welcome {get_name}")
                user_do(get_id)
                break
            else:
                print("\nNot foud")
        else:
            print("\nInvalid value")

print("Welcome to the Vaccination Scheduling Program!")
print("First you need to Sign in or Sign up\n")

while True:
    option = input("To Sign in press 1\nTo Sign up press 2\nTo exit press 0\n\nYour choice: ")
    if option.strip() == '1':
        login()
        break
    elif option.strip() == '2':
        register()
        break
    elif option.strip() == '0':
        break
    else:
        print("\nInvalid value")
