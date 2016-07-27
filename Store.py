import random

# class Player:
#     def __init__(self):
#         self.cash = 100

class Store:


    def __init__(self):
        self.cash = 0
        self.lemons = 0
        self.lemonsPrice = random.randrange(1,5)
        self.sugar = 0
        self.sugarPrice = random.randrange(1,5)
        self.ice = 0
        self.icePrice = random.randrange(1,5)
        self.numTotal_ingridients = 0
        self.numPitchers = 0
        self.numberCups = 0
        self.totalCost = 0
        self.numTotal_ingridients = 0
        self.pricePerPitcher = 0
        self.lemonadeRatio = None
        self.changeAmount = 0

    def makelemonade(self):
        print(' Your current balance :', self.cash)
        print()
        print (' The price of lemons is :  ', self.lemonsPrice)
        print (' The price of ice is    :  ', self.icePrice)
        print (' The price of sugar     :  ', self.sugarPrice) 
    
    def purchase(self):        
        while True:
            try:
                print()
                self.lemons = int(input (' How many lemons do you want to Buy:  '))
                break
            except ValueError:
                print("You should really try typing in a number.")
        while True:    
            try:
                self.sugar = int(input(' How much sugar do you want to buy:  '))
                break
            except ValueError:
                print("You should really try typing in a number.") 
        while True:    
            try:
                self.ice = int(input(' How much ice do you want to buy:  '))
                break
            except ValueError:
                print("You should really try typing in a number.")
                
    def cost(self):    
        self.lemonsCost = self.lemons * self.lemonsPrice
        self.sugarCost = self.sugar * self.sugarPrice
        self.iceCost = self.ice * self.icePrice
        self.totalCost  = self.lemonsCost + self.sugarCost + self.iceCost
        print()
        print (' Your bill for shopping is:', self.totalCost)
        print()
    
    def pitcher(self):
        self.numTotal_ingridients = self.lemons + self.sugar + self.ice
        #print ('Each Pitcher Can handle a total of 5 Ingredients')
        #I don't see the reason to tell the player/s how many ingrediants they can add if we aren't giving them a choice of how to make the lemondade. We can add this back in later if you feel like we should have this print. -Keith
        print()
        self.totalPitchers = (self.numTotal_ingridients / 5)
        self.pricePerPitcher = self.totalCost / self.totalPitchers
        print ('The number of pitchers is ', self.totalPitchers)
        print ('The price per pitcher is', self.pricePerPitcher)
        
    def cups(self):
        self.numberCups = (self.totalPitchers * 10)
        print ('Number of cups is :', self.numberCups)
        
    def Change(self):
        self.changeAmount = self.cash - self.totalCost
        print ('Your Change is : ', self.changeAmount)

    def lemonsToSugar(self):
        if self.lemons > self.sugar:
            self.lemonadeRatio = 0
            print("You made tart lemonade!")
        else:
            self.lemonadeRatio = 1
            print("You made sweet lemonade!")
                    
            
    def lemonaidMaker(self, playerCash):
        self.cash = playerCash
        self.makelemonade()
        self.purchase()
        self.cost()
        self.Change()
        self.pitcher()
        self.cups()
        self.lemonsToSugar()

        
#player = Player()
#sad = Store()
#sad.makelemonade()
#sad.purchase()
#sad.cost()
#sad.balance() 
#sad.lemonaidMaker(50)