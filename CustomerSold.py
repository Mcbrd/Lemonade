import random, math

class CustomerSold:
    def __init__(self):
        self.buyers      = 0
        self.custTart    = 0
        self.custSweet   = 0
        self.custThristy = 0 
        self.numBuyers   = 0
        self.extra       = 0
        self.dissatisfied= 0
        self.conditions  = 0
        self.customers   = 0
        self.pitcers     = 0
        self.price       = 0
        self.advertising = 0
    
    def custMather(self):
        custList = random.sample(range(1000),self.customers)
        for custNum in custList:
            if custNum % 3 == 0:
                self.custSweet += 1   
        for custNum in custList:
            if custNum % 5 == 0:
                self.custTart += 1
        self.custThristy = abs(self.customers - (self.custSweet + self.custTart))
    def custStopper(self):
        self.custMather()
        if self.conditions == 5:
            self.buyers = self.custThristy + self.custTart + self.custSweet
        elif self.conditions == 4:
            self.buyers = self.custThristy + self.custTart
        else:
            self.buyers = self.custThristy + self.custSweet
    def custBuyer(self):
        pricePerGlass = self.price / 10
        potentialBuyers = math.ceil(self.buyers / (1 + pricePerGlass))
        self.numBuyers = abs((potentialBuyers - 10) + random.randint(1,10))
    def lemmonPitcher(self):
        glasses = (self.pitchers * 10)
        if glasses > self.numBuyers:
            served = self.numBuyers
            self.extra = self.numBuyers - (glasses - self.numBuyers)
        else:
            served = self.numBuyers - (self.numBuyers - glasses)
            self.extra = 0
            self.dissatisfied = (self.numBuyers - glasses)
    def cashRegister(self):
        self.cash = self.numBuyers * (self.price/10)
    def pitchersSold(self, pitchers, price, conditions, customers, advertising):
        self.pitchers = pitchers
        self.price = price
        self.conditions = conditions
        self.customers = customers
        self.advertising = advertising
        self.custStopper()
        self.custBuyer()
        self.lemmonPitcher()
        self.cashRegister()

#for testing        

# store = Store()
# test = CustomerSold()
# test.pitchersSold()
# print(test.netGains)