import random, Weather

class Ai:

    def __init__(self):
        self.name = "Computer"
        self.pricepercup = 0
        self.customers = 0
        self.gains = 0

        self.weather = Weather.Weather()

    def getpricepercup(self):
        self.pricepercup = ((random.randint(30, 100)) / 100)
        return self.pricepercup
    def getCustomers(self):
        self.weather.weatherGenerator()
        self.customers = self.weather.customers
        return self.customers
    def getGains(self):
        self.gains = self.gains + ((self.pricepercup) * (self.customers))
        return self.gains        
