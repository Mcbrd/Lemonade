import random, Store, Weather, time

store = Store.Store()
weather = Weather.Weather()

#class TestInput:
#    def __init__(self):
#        self.cash = 40


class Advertise():

    def __init__(self):
        #self.option = ""
        self.advertBalance = 0
        self.advertPrice = 0
        self.advertCostumerLow = 0
        self.advertCostumerHigh = 0
        
    def setPrices(self):
        self.advertPrice = random.randrange(9,19)
        self.advertCostumerLow = random.randrange(0,19)
        self.advertCostumerHigh = random.randrange(10,30)
        
    def option(self):
        option = 0
        print('Your current balance is :',self.cash)
        time.sleep(1)
        print ('The price for advertisement is:', self.advertPrice)
        option = input("Would you like to buy advertisement? y or n; ")
        if option == "y":
            self.advertBalance = self.cash - self.advertPrice
            if self.advertBalance < 0:
                self.advertBalance = 0
                print("You cannot afford advertising ")
                self.option()
            else:
                print("Your new balance is:", self.advertBalance)
                return self.advertBalance
        elif option == "n":
            print("Are you sure???????? this might be a good thing? no? ok no advertisement for you then.")
        else:
            print("Please enter y or n.")
            self.option()

    def new_advert_customers(self):
        if self.advertPrice <= 15:
            self.newTotalCustomers = self.advertCostumerLow
            return self.newTotalCustomers
        else:
            self.newTotalCustomers = self.advertCostumerHigh
            return self.newTotalCustomers
    def advertiser(self, cash):
        self.cash = cash
        self.setPrices()
        self.option()
        self.new_advert_customers()

#test1 = TestInput()
#test = Advertise()
#test.advertiser(test1.cash)