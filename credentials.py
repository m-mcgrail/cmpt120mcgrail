#credentials.py
# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Mary McGrail
# Created: 2018-02-21

#lab 4 part 2 modular design
def names():
    first = input("Please enter first name:")
    last = input("Please enter last name:")
    return first, last
#lab 4 part 2 modular design 2
def username():
    names()
    first, last = names()
    uname = first [:7] + '.' + last[:7]
    return print("Username is:", uname)
def main():
    names()
    first, last = names()
# modified to generate a Marist-style username
    uname = first [:7] + '.' + last [:7] 
    print("Username is:", uname)
# ask user to create a new password
    passwd = input("Create a new password that is over 8 characters: ")
# modified to ensure the password has at least 8 characters through asking nicely
    print(passwd)
    print("Account configured. Your new email adress is", uname + "@marist.edu")
    print("Account password is", passwd) 
main()
