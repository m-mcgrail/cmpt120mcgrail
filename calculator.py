#Calculator project
from graphics import *
#test for calculator project
win = GraphWin('Calc', 400, 580)
displayTextElement = Text(Point(0, 50), "")
#creates the window
calcGrid = [
    [7, 8, 9, '+', 'MC'],
    [4, 5, 6, '-', 'M+'],
    [1, 2, 3, '*', 'M-'],
    ['.', 0, '+/-', '/', 'MR'],
    ['^2', '%', '1/x', 'SQRT', 'MS'],
    ['', '', '=', '', '']
    
]
buttons = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
def calcButton(x, y, value):
    button = Rectangle(Point(x,y),Point(x + 80,y + 80))
    button.setFill('palevioletred1')
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
    for i in range(6):
        for j in range(5):
            if clicked.getX() > buttons[i][j].p1.getX()and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY()and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range(6):
        for j in range(5):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

#calculator functions
def checkInt(toCheck):
    return toCheck == '0' or toCheck == '1' or toCheck == '2' or toCheck == '3' or toCheck == '4' or toCheck == '5' or toCheck == '6' or toCheck == '7' or toCheck == '8' or toCheck == '9'

def checkOperator(toCheck):
    return toCheck == '/' or toCheck == '*' or toCheck == '+' or toCheck == '-' or toCheck == '%'or toCheck == 'SQRT' or toCheck == '^2'or toCheck == '1/x' 

def checkSignChange(toCheck):
    return toCheck == '+/-'

#adding decimals
def checkDecimal (toCheck):
    return toCheck == '.'

def checkEnter(toCheck):
    return toCheck == '='

def inceaseNumber(num1, num2):
    if(num1 == 0) :
        return num2
       
    else :
        return (num1 * 10) + num2
#operations
#adding decimals
def decimal(x, y):
    return x +  (y / 10)

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
#adding other operators
def percent(x, y):
    return y -((x / 100) * y)
def squareRoot(x):
    return x ** (0.5)
def square(x):
    return x **2
def reciprocal(x):
    return 1 / x

def computation(num1, num2, operation):
    if(operation == '+'):
        return add(num1, num2)
    if(operation == '-'):
        return subtract(num1, num2)
    if(operation == '*'):
        return multiply(num1, num2)
    if(operation == '/'):
        return divide(num1, num2)
    if(operation == '+/-'):
        return sign(num1)
#new operators
    if(operation == '%'):
        return percent(num1, num2)
    if(operation == 'SQRT'):
        return squareRoot(num1)
    if(operation == '^2'):
        return square(num1)
    if(operation == '1/x'):
        return reciprocal(num1)
    if(operation == '.'):
        return decimal(num1, num2)
#Creates Calculator
def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)

    nextDecimal = False
    firstNum = 0
    secondNum = 0
    operation = ''
    
    while 1 == 1:
        
        clicked = win.getMouse()
        row, col = clickedButton(clicked)
        if row >=0:
            buttons[row][col].setFill('pink1')
            
            if(nextDecimal != True):
                if (checkInt(str(calcGrid[row][col]))):
                    if(len(operation) == 0):
                        firstNum = inceaseNumber(firstNum, calcGrid[row][col])
                    else :
                        secondNum = inceaseNumber(secondNum, calcGrid[row][col])

                if (checkOperator(str(calcGrid[row][col]))):
                    operation = calcGrid[row][col]
                #adding decimals
                if (checkDecimal(str(calcGrid[row][col]))):
                    nextDecimal = True
                                    
                if(checkSignChange(str(calcGrid[row][col]))):
                    displayString = str(computation(firstNum, secondNum, '+/-'))
                    firstNum = computation(firstNum, secondNum, operation)
                    secondNum = 0
                    operation = ''
                elif (checkEnter(str(calcGrid[row][col]))):
                    displayString = str(computation(firstNum, secondNum, operation))
                    firstNum = computation(firstNum, secondNum, operation)
                    secondNum = 0
                    operation = ''
                else :
                    if(len(operation) == 0):
                        displayString = (str(firstNum) + operation)
                    else:
                        displayString = (str(firstNum) + operation + str(secondNum))
            else:
                if(checkInt(str(calcGrid[row][col]))):
                    #print(firstNum)
                    #print(secondNum)
                    if(secondNum == 0):
                        print('Fas Unos')
                        firstNum = decimal(firstNum, calcGrid[row][col])
                        nextDecimal = False
                        displayString = str(firstNum)
                    else:
                        print('Fas Duos')
                        secondNum = decimal(secondNum, calcGrid[row][col])
                        nextDecimal = False
                        displayString = str(firstNum) + operation + str(secondNum)

            displayTextElement.undraw()
            displayTextElement = Text(Point(300 - (len(displayString) * 7), 50), displayString)
            displayTextElement.draw(win)
        for i in range(6):
            for j in range(5):
                if not(i == row and j == col):
                    buttons[i][j].setFill('palevioletred1')

        
main()
