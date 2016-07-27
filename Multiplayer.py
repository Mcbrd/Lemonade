class Multiplayer:
    def __init__(self):
        self.playerAmount = 0

    def promptForPlayerAmount(self):
        self.playerAmount  = int(input("enter 1 for one-player, or 2 for two-player:  "))
        return self.playerAmount