import json

class Scores:
    def __init__(self):
        self.scoreFile = open('scores.json', 'r+')
        self.scoresDict = json.load(self.scoreFile)
        self.scoreFile.close()
    def updateScore(self, playerName, playerScore):
        self.scoreFile = open('scores.json', 'r+')
        self.scoresDict = json.load(self.scoreFile)
        self.scoreFile.close()
        self.scoresDict[str.upper(playerName)] = playerScore
        self.scoreFile = open('scores.json', 'w')
        json.dump(self.scoresDict, self.scoreFile)
        self.scoreFile.close()
    def openForRead(self):
        self.scoreFile = open('scores.json', 'r+')
        self.scoresDict = json.load(self.scoreFile)
        self.scoreFile.close
    def checkForExisting(self, playerName):
        self.scoreFile = open('scores.json', 'r+')
        self.scoresDict = json.load(self.scoreFile)
        playerName = str.upper(playerName)
        score = 0
        for player in self.scoresDict:
            if player == playerName:
                print(player)
                score = self.scoresDict[playerName]
            else:
                score = 100
        return score
#scores = Scores()
#scores.updateScore("james", 56)
#score = scores.checkForExisiting("james")
#print(score)