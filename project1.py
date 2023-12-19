import os
import json
import pickle

file_path = 'logs.txt'
f = open("Logs.txt", 'a+')
login_dic = {"ID": '', "password": ''}

# Take the input
choice = input(
    "Enter which you want:\n1-Login\n2-Register\n3-Add Vaccine center\n3-remove vaccine center:\n").lower()


# User login the System


def login():

    pass


if choice == '1':
    Id = int(input("Please enter your ID:"))
    password = input("Please enter your password:")
    login_dic['ID'] = Id
    login_dic['password'] = password
    # f.write(str(login_dic))

    login(Id, password, email='', name='')

if choice == '2':

    user_name = input("Enter your username:")
    user_email = input("Enter your email:")
    user_password = input("Enter your password")
    # f.write("hi\n")
    f.write(f"username:{str(user_name)}")

if choice == '#':
    pass
