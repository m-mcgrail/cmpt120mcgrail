#tennissimulation.py
#Lab 10
#from simstats import SimStats
#from tennismatch game import TGame

def printIntro():
    print("This program simulates a series of tennis matches.")

def getInputs():
    probA = .6
    probB = .5
    n = 50
    print("This particular program gives player A a 60% chance of winning a serve\n")
    print("\n and player B a 50% chance. They will play a total of 50 games.")

    return probA, probB, n

def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()

    for i in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        stats.update(theGame)
    stats.printReport()

main()
    
