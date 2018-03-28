#Calculator Project part 3
#calculator3.py
from graphics import *
from button import Button
from math import *

def createCalculatorGui():
    win = GraphWin("calculator", 400, 500)
    win.setCoords(0, 0, 6, 7)
    win.setBackground("palevioletred1")
    bSpecs = [ (2,1,'0'), (3,1,'.'),
           (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
           (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
           (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C'),
           (1,5,'MC'),(2,5,'M+'),(3,5,'M-'),(4,5,'MR'),(5,5,'MS')]

    buttons = createButtons(bSpecs, win)
    display = createDisplay(win)
    return buttons, display, win

def createButtons(bSpecs, win):
    buttons = []
    for cx, cy, label in bSpecs:
        buttons.append(Button(win, Point(cx, cy), .75, .75, label))
    buttons.append(Button(win, Point(4.5,1), 1.75, .75, "="))
    for b in buttons:
        b.activate()
    return buttons

def createDisplay(win):
    bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
    bg.setFill('white')
    bg.draw(win)
    text = Text(Point(3,6), "")
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

def processButton(key, display, memory):
    text = display.getText()
    if key == "<-":
        display.setText(text[:-1])
    elif key == "C":
        display.setText("")
    elif key == "=":
        try:
            result = eval(text)
        except:
            result = "ERROR"
        display.setText(result)
    else:
        display.setText(text + key)

def main():
    buttons, display, calc = createCalculatorGui()
    memory = 0
    while True:
        key = getButtonPressed(buttons, calc)
        print(key)
        processButton(key, display, memory)

main()
