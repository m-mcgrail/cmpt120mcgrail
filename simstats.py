# simstats.py
class SimStats:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA = self.winsA + 1

        else:
            self.winsB = self.winsB + 1
                
    def __printHeading(self):
        print("Summary of", self.winsA + self.winsB, "matches:\n")
        print("          wins (% total)     ")
        print("-----------------------------------------------")

    def printReport(self):
        self.__printHeading()
        n = self.winsA + self.winsB 
        self.printLine("A", self.winsA, n);
        self.printLine("B", self.winsB, n);

    def printLine(self, label, wins,  n):
        template = "Player {0}:{1:5}"
        print (template.format(label, wins))
        
