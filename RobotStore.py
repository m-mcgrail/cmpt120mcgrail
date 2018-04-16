#lab 9
#RobotStore.py


#look up how to better make a class
#lab 9 part 1.a
class ProductInfo:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def getProduct(self):
        return self.name
    def getPrice(self):
        return self.price
    def getQuantity(self):
        return self.stock
    #lab 9 part 1.b
    def stockQuantity(self, name, stock):
        for i in range(0,len(name)):
            if stock[i] > 0:
                print("There are", int(stock), name, "left in stock")
    #lab 9 part 1.c
    def costTotal(self, name, price):
        orderQuan = 0 + #how much of the product are they buying
        itemTotal = orderquan * self.price
        costTotal = itemTotal + itemTotal
    #lab 9 part 1.d
    def depleteStock(self, name, stock):
        orderQuan = #as seen above
        stock = stock - orderQuan
        for i in range(0,len(name)):
            if stock[i] > 0:
                print("There are", int(stock), name, "left in stock")
                
#OG code below

productNames = [ "Ultrasonic range finder"
 , "Servo motor"
 , "Servo controller"
 , "Microcontroller Board"
 , "Laser range finder"
 , "Lithium polymer battery"
 ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

                
def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")",productNames[i], "$", productPrices[i])
    print()
    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if productQuantities[prodId] >= count:
            if cash >= productPrices[prodId]:
                productQuantities[prodId] -= count
                cash -= productPrices[prodId] * count
                print("You purchased", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productNames[prodId])
main()
