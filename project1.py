import os
import json

file_path = 'logs.txt'
f = open("Logs.txt", 'w')

choice = input(
    "Enter which you want:\n1-Login\n2-Register\n3-Add Vaccine center\n3-remove vaccine center\n")


def check():
    pass


def login(Id, password, email, name):

    check()


if choice == '1':
    Id = int(input("Please enter your ID:"))
    password = input("Please enter your password:")

    login(Id, password, email='', name='')
    # print("Logged in successfull")

if choice == '2':

    user_name = input("Enter your username:")
    # user_email = input("Enter your email:")
    # user_password = input("Enter your password")
    # f.write("hi\n")
    f.write(f"username:{str(user_name)}")
