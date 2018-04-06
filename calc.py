#Calculator Project part 3
#calculator3.py
from graphics import *
from button import Button
import math

def createCalculatorGui():
    #changed dimensions to make room for scientific mode
    win = GraphWin("calculator", 900, 500)
    win.setCoords(0, .5, 9, 6.75)
    win.setBackground("aliceblue")
    #scientific buttons
    bSpecs = [(1,1,'ln'), (2,1,'10^x'), (3,1,"( )"),(4,1,'0'), (5,1,'.'),
          (1,2,'tan^-1'), (2,2,'tan'), (3,2,'1'), (4,2,'2'), (5,2,'3'), (6,2,'+'), (7,2,'-'),
          (1,3,'cos^-1'), (2,3,'cos'), (3,3,'4'), (4,3,'5'), (5,3,'6'), (6,3,'*'), (7,3,'/'),
          (1,4,'sin^-1'), (2,4,'sin'), (3,4,'7'), (4,4,'8'), (5,4,'9'), (6,4,'<-'),(7,4,'C'),
          (1,5,'log'), (2,5,'x^y'), (3,5,'MC'),(4,5,'M+'),(5,5,'M-'),(6,5,'MR'),(7,5,'MS')]
    
    buttons = createButtons(bSpecs, win)
    display = createDisplay(win)
    runDisp = runningDisplay(win)
    return buttons, display, win, runDisp

def createButtons(bSpecs, win):
    buttons = []
    for cx, cy, label in bSpecs:
        buttons.append(Button(win, Point(cx, cy), .75, .75, label))
    buttons.append(Button(win, Point(6.5,1), 1.75, .75, "="))
    for b in buttons:
        b.activate()
    return buttons

def createDisplay(win):
    bg = Rectangle(Point(.5, 5.75), Point(5, 6.5))
    bg.setFill('white')
    bg.draw(win)
    text = Text(Point(2.75, 6.15), "")
    text.draw(win)
    text.setFace("courier")
    text.setStyle("bold")
    text.setSize(16)
    return text
def runningDisplay(win):
    rd = Rectangle(Point(5.5, 5.75), Point(7.4, 6.5))
    rd.setFill('azure2')
    rd.draw(win)
    text = Text(Point(6.75,6), "")
    text.draw(win)
    text.setFace("courier")
    text.setStyle("bold")
    text.setSize(16)
    return text


def getButtonPressed(buttons, calc):
    while True:
        p = calc.getMouse()
        for b in buttons:
            if b.clicked(p):
                return b.getLabel()

def processButton(key, display, runDisp, memory):
    text = display.getText()
    memory = 0
    base = math.e
    if key == "<-":
        display.setText(text[:-1])
    elif key == "C":
        display.setText("")
        runDisp.setText("")
    #memory keys
    elif key == "MC":
        memory = 0
    elif key == "M+":
        memory == memory + text
    elif key == "M-":
        memory == memory - text
    elif key == "MR":
        display.setText(result)
    elif key == "MS":
        memory = display.setText(memory)
    #science keys
    elif key == "log":
        display.setText(math.log10(int(text)))
    elif key == "x^y":
        display.setText(int(text)**int(text))
    elif key == "sin^-1":
        display.setText(math.asin(int(text)))
        try:
                result = (math.asin(int(text)))
        except:
                print("Unable to divide by 0")
                result = 0
    elif key == "sin":
        display.setText(math.sin(int(text)))
    elif key == "cos^-1":
        display.setText(math.acos(int(text)))
        try:
                result = (math.acos(int(text)))
        except:
                print("Unable to divide by 0")
                result = 0
    elif key == "cos":
        display.setText(math.cos(int(text)))
    elif key == "tan^-1":
        display.setText(math.atan(int(text)))
        try:
                result = (math.atan(int(text)))
        except:
                print("Unable to divide by 0")
                result = 0
    elif key == "tan":
        display.setText(math.tan(int(text)))
    elif key == "ln":
        display.setText(math.log(int(text)))
    elif key == "10^x":
        display.setText(10 ** int(text))
    elif key == "( )":
        text = [(text)]
    elif key == "=":
        try:
            result = eval(text)
        except:
            result = "ERROR"
        display.setText(result)
    else:
        display.setText(text + key)
    runDisp.setText(str(text) + key)
def main():
    buttons, display, calc, runDisp = createCalculatorGui()
    memory = 0
    while True:
        key = getButtonPressed(buttons, calc)
        print(key)
        processButton(key, display, runDisp, memory)


main()
