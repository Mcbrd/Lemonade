import random, os
import Store, Weather, CustomerSold, Player, Advertisement, Multiplayer, Comp, Scores





class Utilitys:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Main():
    def __init__(self):
        self.playerList = []
        self.ai = True

    def checkNumberOfPlayers(self):
        multiplayer = Multiplayer.Multiplayer()
        numberOfPlayers = multiplayer.promptForPlayerAmount()
        if numberOfPlayers > 1:
            self.ai = False
            test.createPlayer(numberOfPlayers)
        else:
            test.createPlayer(numberOfPlayers)

    def createPlayer(self, numberOfPlayers):
        i=0
        while i < numberOfPlayers:
            player = Player.Player()
            self.playerList.append(player)
            i += 1

    def getInfo(self):
        store = Store.Store()
        weather = Weather.Weather()
        advert = Advertisement.Advertise()
        customerSold = CustomerSold.CustomerSold()
        ai = Comp.Ai()
        scores = Scores.Scores()
        test.runGame(store, weather, advert, customerSold, ai, scores)


    def runGame(self, store, weather,advert, customerSold, ai, scores):
        for player in self.playerList:
            player.getPlayerName()
            player.getTurns()
            player.gains = scores.checkForExisting(player.playerName)
            for days in range(1,player.turns+1):
                weather.weatherGenerator() 
                store.lemonaidMaker(player.gains) #fix spelling
                player.gainsEdit(store.changeAmount)
                advert.advertiser(player.gains)
                player.gainsEdit(player.gains)
                customerSold.pitchersSold(store.numPitchers, store.totalPitchers, weather.conditions, weather.customers, advert.newTotalCustomers)
                if self.ai == True:
                    ai.getpricepercup()
                    ai.getCustomers()
                    ai.getGains()
                    print("")

                    print("    Computer Total Earnings:", ai.getGains())
                player.gainsEdit(customerSold.cash + player.gains)
                scores.updateScore(player.playerName, player.gains)

            
            print()
            print("You started with $100")
            print("This is your end bank:",player.gains)
            if self.ai == True:
                print("    Computer Total Earnings:", ai.getGains())


    def main(self):
        test.checkNumberOfPlayers()
        test.getInfo()


test= Main()
test.main()