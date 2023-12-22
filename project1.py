import os
import json

list_vaccines = ["Corona", "cancer", "Virus C"]
users = [['111', 'zeyad', 'zeyad2005@', 'zoz']]
admin_password = "admin"
vaccination_center = [['000', 'ax', 'cairo', list_vaccines]]

# Take the input
choice = input(
    "Enter which you want:\n1-Login\n2-Register\n3-Add Vaccine center\n3-remove vaccine center:\n").lower()


# User login the System

def login():
    role = input("Enter admin password:").lower()
    Id = int(input("Enter your ID:"))
    name = input("Enter your name:")
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        if user[2] == email and user[3] == password:
            print("Iam here")
        else:
            print("invalid option..")

    if role == admin_password:
        print("Admin menu\n")
        while True:
            choose = input(
            "Add Vaccination Center:\nRemove Vaccination Center:\n").lower()
            if choose == 'add':
                vac_ID = int(input("Enter the vaccination center ID:"))
                vac_name = input("Enter the vaccination center name:")
                vac_address = input("Enter the vaccination center address:")
                vaccination_center.append([vac_ID, vac_name, vac_address])
                print("list added")
            else:
                print(vaccination_center)
                remove_input = input("Enter which list you want to remove:")
                remove_input - 1
                vaccination_center.pop(remove_input)

# Register to system


def register():
    pass


if choice == '1':
    login()
if choice == '2':
    register()

if choice == '#':
    pass
