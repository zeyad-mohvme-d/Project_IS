import os
import json


users = [['111', 'zeyad', 'zeyad2005@', 'zoz']]
admin_password = "admin"
vaccination_center = [['000', 'ax', 'cairo',
                      ["Corona\n", "cancer\n", "Virus C"]]]

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
            return True

        else:
            print("invalid option..")

    if role == admin_password:

        pass

# Register to system


def register():
    pass


if choice == '1':
    login()
if choice == '2':
    register()

if choice == '#':
    pass
