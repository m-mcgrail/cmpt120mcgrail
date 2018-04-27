#testcalc.py
from calcface import CalcInter
from calcfunction import Functions

def getButtonPressed(buttons, calc):
    while True:
        p = calc.getMouse()
        for b in buttons:
            if b.clicked(p):
                return b.getLabel()
def main():
    interface = CalcInter()
    memory = 0
    while True:
        key = getButtonPressed(interface.buttons, interface.win)
        print(key)
        Functions.processButton

main()
