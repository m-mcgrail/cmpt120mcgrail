#credentials.py
# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Mary McGrail
# Created: 2018-02-21

#Lab 4 Final
#lab 4 part 2 modular design
def names():
    first = input("Please enter first name:")
    last = input("Please enter last name:")
    return first, last
#lab 4 part 2 modular design 2
#lab 4 part 3 improvements - lowercase
def username():
    names()
    first, last = names()
    uname = first [:7] + '.' + last[:7]
    return print("Account configured. Your new email adress is", uname.lower() + "@marist.edu")
#lab 4 part 2 modular design 3
#lab 4 part 3 improvements - password cases
def password():
   passwd = input("Create a new password that is over 8 characters, including both upper and lower case letters: ")
   return passwd;
#lab 4 part 3 improvements 
def strength():
    srg = input(print("Do you feel that your password is strong? Y/N"))
    #'Y', 'yes' = True
    #'N', 'no' = False
    if True:
        print("Good job")
        if False:
            print("Change it") 
def main():
    username()
    password()
    strength()
main()

