import socket
import sys
import threading
import Store, Weather, CustomerSold, Player, Advertisement, Multiplayer, Comp, Scores

class Server:
    def __init__(self,HOST,PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.client_list = []
        self.playerList = []
        self.scores = Scores.Scores()
        self.weather = Weather.Weather()
        
        try:
            self.s.bind((HOST, PORT))
        except socket.error:
            print("Bind failed.")
            sys.exit()
        print("Socket Binded")
        self.s.listen(5)
        print('Server started. Listening...')
        self.waiting_room()
    
    def waiting_room(self):
        while True:
            client, addr = self.s.accept()
            print('Connected with ',addr[0],':',str(addr[1]))
            client.send("You have connected successfully to server".encode('utf-8'))
            self.client_list.append(client)
            self.client_list[0].send("Please wait for your opponent to connect...".encode('utf-8'))
            if len(self.client_list) > 1:
                self.client_list[1].send("Other player is ready...".encode('utf-8'))
                self.client_list[0].send("Enter your username :".encode('utf-8'))
                self.client_list[1].send("Enter your username :".encode('utf-8'))
                Player1 = self.client_list[0].recv(1024).decode()
                self.Player1 = Player.Player()
                self.Player1.playerName = Player1
                Player2 = self.client_list[1].recv(1024).decode()
                self.Player2 = Player.Player()
                self.Player2.playerName = Player2
                self.Player1.highscore = self.scores.checkForExisting(Player1) # Might *probably have to decode from unicode
                self.Player2.highscore = self.scores.checkForExisting(Player2)
                self.Player1.turns = 5
                self.Player2.turns = 5
                
                for c in self.client_list:
                    c.send("Welcome player, Get Ready the game will now start..".encode('utf-8'))
                    return False

    def runGameServer(self, weather, scores):
        for days in range(1,player.turns+1):
            weather.weatherGenerator()
            weather_conditions = weather.conditions # grab the new conditions and now need to pass to client, can run weather algo on client side
            for c in self.client_list:
                c.send(weather_conditions)
            p1score = self.client_list[0].recv(1024).decode()
            p2score = self.client_list[0].recv(1024).decode()
            self.Player1.gains = p1score   
            self.Player2.gains = p2score   
            self.client_list[0].send(p2Score)
            self.client_list[1].send(p1score)
            print("current day in game is {}".format(days))

        print("Current game over")
        
        
if __name__ == "__main__":
    server = Server("",12345)
    server.rungameServer(server.weather,server.scores)
    print("game is over")
    #self.s.close()




