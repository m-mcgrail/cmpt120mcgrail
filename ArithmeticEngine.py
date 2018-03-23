# CMPT 120 - Lab #6
# Mary McGrail
# 3-23-18
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def inputNum(num1, num2):
   #added a try-block
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except:
        print("Please enter a numeric value next time")
    return num1, num2
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        num1 = 0
        num2 = 0
        #changed cmd to lowercase
        if cmd.lower() == "add":
            num1, num2 = inputNum(num1, num2)
            result = num1 + num2
        elif cmd.lower() == "sub":
            num1, num2 = inputNum(num1, num2)
            result = num1 - num2
        elif cmd.lower() == "mult":
            num1, num2 = inputNum(num1, num2)
            result = num1 * num2
        #try-block inserted
        elif cmd.lower() == "div":
            num1, num2 = inputNum(num1, num2)
            try:
                result = num1 // num2
            except:
                print("Unable to divide by 0")
                result = 0
        elif cmd.lower() == "quit":
            return False
        #invalid command
        elif cmd.lower() !="add" or "sub" or "mult" or "div" or "quit":
            print("This commmand wasn't valid")
            result = 0
    
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()
main()
