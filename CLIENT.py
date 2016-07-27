from socket import *
from threading import Thread
import random, os
import Store, Weather, CustomerSold, Player, Advertisement, Scores
import time

class Utilitys:
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

class Client:
    def __init__(self,HOST,PORT):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.HOST = HOST
        self.PORT = PORT
        self.store = Store.Store()
        self.weather = Weather.Weather()
        self.advert = Advertisement.Advertise()
        self.customerSold = CustomerSold.CustomerSold()
        self.scores = Scores.Scores()
        self.player = Player.Player()
       
    def Connect(self):
        self.s.connect((self.HOST, self.PORT))

    def waiting_room(self):
        wait = self.s.recv(1024).decode()
        print(wait)
        wait = self.s.recv(1024).decode()
        print(wait)
        username_request = self.s.recv(1024).decode()
        print(username_request)
        username = input("Enter your username")
        self.player.playerName = username
        username = username.encode("utf-8")
        self.s.send(username)
        time.sleep(3)

    def Disconnect(self):
        s.close()

    def Reconnect(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((self.HOST,self.PORT))

    def sendMessage(self):
        message = "whatever you need to send"
        self.s.send(message)

    def receiveMessage(self):
        reply = self.s.recv(1024)
        print("Received ", repr(reply))

    
    def Game(self):
        for days in range(1,self.player.turns+1):
            weather_conditions = self.s.recv(1024).decode()
            self.weather.conditions = weather_conditions
            self.weather.conditionsPrinter()
            self.weather.customerGenerator() #this generates weather.customers which will be passed back to server
            self.store.lemonaidMaker(self.player.gains)
            self.player.gainsEdit(store.changeAmount)
            self.advert.advertiser(self.player.gains)
            self.player.gainsEdit(self.player.gains)
            self.customerSold.pitchersSold(self.store.numPitchers, self.store.totalPitchers, self.weather.conditions, self.weather.customers, self.advert.newTotalCustomers)
            self.player.gainsEdit(self.player.gains)
            #self.scores.updateScore(player.playerName,player.gains) This will be done on server side and then send back
            # score card at end of each day (round)
            print()
            print("You started with $100")
            print("This is your end bank :", self.player.gains)
            self.s.send(self.player.gains.encode("utf-8")) # Send server current gains
            self.opponent_score = self.s.recv(1024).decode()
            print("Your opponents current end bank :", self.opponent_score)
            time.sleep(4)
        
        if self.opponent_score > self.player.gains:
            print("You lost to your opponent, your opponent made more bank than you")
        else:
            print("You defeated your opponent, get rich or die tryin")

        #Highscore prints and prompt if players want to play again if statements up next and then debugging



        

if __name__ == "__main__":

    client = Client("10.2.20.36",12345)
    client.Connect()
    client.waiting_room()
    client.Game()


