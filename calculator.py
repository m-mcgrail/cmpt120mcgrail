from graphics import *
#test for calculator project
win = GraphWin('Calc', 320, 500)
displayTextElement = Text(Point(0, 50), "")
#creates the window
calcGrid = [
    [7, 8, 9, '+'],
    [4, 5, 6, '-'],
    [1, 2, 3, '*'],
    ['', 0, '+/-', '/'],
     ['', '=', '', '']
]
buttons = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
def calcButton(x, y, value):
    button = Rectangle(Point(x,y),Point(x + 80,y + 80))
    button.setFill('cyan')
    button.draw(win)
    text = Text(Point(x + 40, y + 40), value)
    text.draw(win)
    return button

def inside(clicked, button):
    if clicked.getX() > button.p1.getX()and clicked.getX() < button.p2.getX():
            if clicked.getY() > button.p1.getY()and clicked.getY() < button.p2.getY():
                return True
    return False

def clickedButton(clicked):
    for i in range(5):
        for j in range(4):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(5):
        for j in range(4):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def checkInt(toCheck):
    return toCheck == '0' or toCheck == '1' or toCheck == '2' or toCheck == '3' or toCheck == '4' or toCheck == '5' or toCheck == '6' or toCheck == '7' or toCheck == '8' or toCheck == '9'

def checkOperator(toCheck):
    return toCheck == '/' or toCheck == '*' or toCheck == '+' or toCheck == '-' or toCheck == '+/-'

def checkEnter(toCheck):
    return toCheck == '='

def inceaseNumber(num1, num2):
    if(num1 == 0) :
        return num2
        print ('Fas')
    else :
        return (num1 * 10) + num2
        print ('Nefas')

#calculator functions
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def sign(x):
    return x * -1

def computation(num1, num2, operation):
    if(operation == '+'):
        return add(num1, num2)
    if(operation == '-'):
        return subtract(num1, num2)
    if(operation == '*'):
        return multiply(num1, num2)
    if(operation == '/'):
        return divide(num1, num2)

def answer(val_1, val_2):
    val_1 = int(input(displayTextElement))
    oper = input('+', '-', '*', '/', '+/-', '=')
    val_2 = int(input(displayTextElement))
    answer = ()
    if oper == '+':
        return(val_1, "+", val_2, add(val_1, val_2))
    elif oper == '-':
        return(val_1, '-', val_2, subtract(val_1, val_2))
    elif oper == '*':
        return(val_1, '*', val_2, multiply(val_1, val_2))
    elif oper == '/':
        return(val_1, '/', val_2, divide(val_1, val_2))
    elif oper == '+/-':
        return(val_1, '+/-', sign(val_1))
    elif oper == '=':
        return answer
    else:
        print("Invalid input")
    print(answer)

def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)

    firstNum = 0
    secondNum = 0
    operation = ''
    
    while 1 == 1:
        
        clicked = win.getMouse()
        row, col = clickedButton(clicked)
        if row >=0:
            buttons[row][col].setFill('pink')
            
            if (checkInt(str(calcGrid[row][col]))):
                if(len(operation) == 0):
                    firstNum = inceaseNumber(firstNum, calcGrid[row][col])
                else :
                    secondNum = inceaseNumber(secondNum, calcGrid[row][col])

            if (checkOperator(str(calcGrid[row][col]))):
                operation = calcGrid[row][col]

            if (checkEnter(str(calcGrid[row][col]))):
                firstNum = computation(firstNum, secondNum, operation)
                secondNum = 0
                operation = ''
                displayString = str(computation(firstNum, secondNum, operation))
            else :
                if(len(operation) == 0):
                    displayString = (str(firstNum) + operation)
                else:
                    displayString = (str(firstNum) + operation + str(secondNum))
            
            #print (len(displayString))

            displayTextElement.undraw()
            displayTextElement = Text(Point(300 - (len(displayString) * 7), 50), displayString)
            displayTextElement.draw(win)
        for i in range(5):
            for j in range(4):
                if not(i == row and j == col):
                    buttons[i][j].setFill('cyan')
    val_1 = int(input(calcGrid[row][col]))
    val_2 = int(input(calcGrid[row][col]))
    answer(val_1, val_2)
         

        
main()
