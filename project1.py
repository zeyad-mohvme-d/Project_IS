import os
import json

users = [['111', 'zeyad', 'zeyad2005@', 'zoz']]

# Take the input
choice = input(
    "Enter which you want:\n1-Login\n2-Register\n3-Add Vaccine center\n3-remove vaccine center:\n").lower()


# User login the System

def login():
    Id = int(input("Enter your ID:"))
    name = input("Enter your name:")
    email = input("enter your email:")
    password = input("Enter your password:")
    for user in users:
        if user[2] == email and user[3] == password:
            print("Logged in succssefull")

        else:
            print("invalid option..")

# Register to system


def register():
    pass


if choice == '1':
    login()
if choice == '2':
    register()

if choice == '#':
    pass
