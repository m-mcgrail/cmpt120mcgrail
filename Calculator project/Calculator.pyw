#calculator.pyw
#project 5 calculator interface class
from graphics import *
from button import Button
class CalcInter:
    def __init__(self):
        self.win = GraphWin("calculator", 900, 500)
        self.win.setCoords(0, .5, 9, 6.75)
        self.win.setBackground("mintcream")
        self.bSpecs = [[1,1,'ln'], [2,1,'10^x'], [3,1,"[ ]"],[4,1,'0'], [5,1,'.'],
          [1,2,'tan^-1'], [2,2,'tan'], [3,2,'1'], [4,2,'2'], [5,2,'3'], [6,2,'+'], [7,2,'-'],
          [1,3,'cos^-1'], [2,3,'cos'], [3,3,'4'], [4,3,'5'], [5,3,'6'], [6,3,'*'], [7,3,'/'],
          [1,4,'sin^-1'], [2,4,'sin'], [3,4,'7'], [4,4,'8'], [5,4,'9'], [6,4,'<-'],[7,4,'C'],
          [1,5,'log'], [2,5,'x^y'], [3,5,'MC'],[4,5,'M+'],[5,5,'M-'],[6,5,'MR'],[7,5,'MS']]
    
        buttons = self.createButtons(self.bSpecs, self.win)
        display = self.createDisplay(self.win)
        runDisp = self.runningDisplay(self.win)
        
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
        bg.setFill('snow')
        bg.draw(win)
        text = Text(Point(2.75, 6.15), "")
        text.draw(win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        return text
    def runningDisplay(win):
        rd = Rectangle(Point(5.5, 5.75), Point(7.4, 6.5))
        rd.setFill('honeydew')
        rd.draw(win)
        text = Text(Point(6.75,6), "")
        text.draw(win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        return text
    def getButtons():
        return self.buttons


