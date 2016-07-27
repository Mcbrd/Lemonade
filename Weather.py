import random

class Weather:
    def __init__(self):
        self.conditions = 0
        self.customers = 0
        self.paradeList = ["mostly sunny","sunny and warm","chance of clouds","perfect day for a parade!","sunny and warm"]
        self.sunnyList = ["mostly sunny","chance of showers","partly cloudy","sunny and warm","perfect day for a parade!"]
        self.overcastList = ["mostly sunny","chance of showers","partly cloudy","cool and cloudy","chance of clouds"]
        self.rainyList = ["storms a brewin","chance of showers","partly cloudy","cool and cloudy","chance of clouds"]
        self.stormList = ["storms a brewin","chance of showers","storms a brewin","cool and cloudy","chance of clouds"]
           
    def conditionsGenerator(self):
        theWeather = random.randint(1, 10)
        paradeTemp = 5
        sunnyTemp  = 4
        overcastTemp = 3
        rainyTemp = 2
        stormTemp = 1
        if theWeather == 10:
            self.conditions = paradeTemp
        elif theWeather >7:
            self.conditions = sunnyTemp
        elif theWeather >4:
            self.conditions = overcastTemp
        elif theWeather >= 2:
            self.conditions = rainyTemp
        elif theWeather  == 1:
            self.conditions = stormTemp

    def customerGenerator(self, conditions):
        paradeTemp = 5
        sunnyTemp = 4
        overcastTemp = 3
        rainyTemp = 2
        stormTemp = 1
        if self.conditions == paradeTemp:
            self.customers = random.randint(70,100)
        elif self.conditions == sunnyTemp:
            self.customers = random.randint(60,80)
        elif self.conditions == overcastTemp:
            self.customers = random.randint(40, 70)
        elif self.conditions == rainyTemp:
            self.customers = random.randint(20, 50)
        elif self.conditions == stormTemp:
            self.customers = random.randint(0,30)

    def weatherForecaster(self, conditions):
            paradeTemp = 5
            sunnyTemp = 4
            overcastTemp = 3
            rainyTemp = 2
            stormTemp = 1
            if self.conditions == paradeTemp:            
                quotes = random.choice(self.paradeList)
                self.forecast = (quotes)
            elif self.conditions == sunnyTemp:
                quotes = random.choice(self.sunnyList)
                self.forecast = (quotes)
            elif self.conditions == overcastTemp:
                quotes = random.choice(self.overcastList)
                self.forecast = (quotes)
            elif self.conditions == rainyTemp:
                    quotes = random.choice(self.rainyList)
                    self.forecast = (quotes)
            elif self.conditions == stormTemp:
                    quotes = random.choice(self.stormList)
                    self.forecast = (quotes)

    def weatherGenerator(self):
        
        self.conditionsGenerator()
        self.customerGenerator(self.conditions)
        self.weatherForecaster(self.conditions)

day = Weather()
day.conditionsGenerator()
day.customerGenerator(day.conditions)
day.weatherForecaster(day.conditions)
print(day.conditions)
print(day.customers)
print("Forecast :",day.forecast)
#day.weatherGenerator()