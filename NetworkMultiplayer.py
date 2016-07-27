from CLIENT import Client
from SERVER import Server
import random, os
import Store, Weather, CustomerSold, Player, Advertisement
from Scores import Scores

class NetworkMultiplayer:
	def __init__(self):
		self.server = Server("",12345)
		self.scores = Scores()
		


	def Game(self):
		self.scores.openForRead()
		self.server.waiting_room()



Game = NetworkMultiplayer()
Game.