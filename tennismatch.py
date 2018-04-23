#tennismatch.py
#modified rballgame.py from lecture
from tennisplayer import Player


class TGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.setsA = 0
        self.setsB = 0
        self.winsA = 0
        self.winsB = 0

    def gamePlay(self):
        while not self.gameIsOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
            #instead of switching servers, the other player gets the point
                self.changeServer()
                self.server.incScore()
                self.changeServer()

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
            
    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()
   
    def gameIsOver(self):
        #changed for individual tennis games within a set
        return self.playerA.getScore() >40 or self.playerB.getScore() >40 \
            or (self.playerA.getScore() == 40 and self.playerB.getScore() >60) \
            or (self.playerB.getScore() >60 and self.playerA.getScore() == 40)

    def gameToSet(self):
        #modified from simstats update
        a, b  = self.playerA.getScore(), self.playerB.getScore()
        if a > b + 2:
            self.setsA = self.setsA + 1
            if a==6 and b == 5:
                #a would need one more set and b would need two
        else:
            self.setsB = self.setsB + 1
            if a ==5 and b == 6:
                #b would need one more set to win, a would need two
                
    def matchOver(self):
        return self.setsA == 3 or self.sets == 3
    
    def setToWin(self):
        while not matchOver():
            if self.setsA > self.setsB:
                self.winsA = self.winsA + 1
            else:
                self.winsB = self.winsB + 1
                
            
                       
        

    
