class Player:
    def __init__(self):
        self.playerName = None
        self.gains = 100
        self.pitcherAmount = 0
        self.turns = None
        self.highscore = 0
        #self.address = address

    def pitcherEdit(self, pitcherAmount):
        self.pitcherAmount = pitcherAmount

    def getPlayerName(self):
        self.playerName = input("Please enter your name: ")
        print("")
    def getTurns(self):
        print("How many turns would you like to play?")
        while self.turns == None:
            self.turns = input("Please enter a number: ")
            print("")
            try:
                self.turns = int(self.turns)
                return self.turns
            except:
                self.turns = None
    def gainsEdit(self, gains):
        self.gains = gains
    def getGains(self):
        return self.gains
    def getPitcherAmount(self):
        return self.pitcherAmount


# player = Player()
# player.getPlayerName()



