#lab 9
#RobotStore.py


#look up how to better make a class
#lab 9 part 1.a
class Product:
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

    def checkStock(self, count):
        if(self.stock >= count):
            return True
        else:
            return False

    #lab 9 part 1.c
    def costTotal(self, count):
        return self.price * count

    #lab 9 part 1.d
    def depleteStock(self, count):
        self.stock -= count

#lab 9 part 2                
productList = [
        Product("Ultrasonic range finder", 2.50, 4),
        Product("Servo motor", 14.99, 10),
        Product("Servo Controller", 44.95, 5),
        Product("Microcontroller Board", 34.95, 7),
        Product("Laser range finder", 149.99, 2),
        Product("Lithium polymer battery", 8.99, 8)
    ]

#lab 9 part 3                
def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productList)):
        if productList[i].getQuantity() > 0:
            print(str(i)+")", productList[i].getProduct(), "$",
                  productList[i].getPrice(), "->",
                  productList[i].getQuantity(), "left in stock")
            
    print()
def printIntro():
    print("This is a computer store!")
    print()
    
def main():
    printIntro()
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if productList[prodId].checkStock(count):
            if cash >= productList[prodId].getPrice():
                productList[prodId].depleteStock(count)
                cash -= productList[prodId].costTotal(count)
                print("You purchased", count, productList[prodId].getProduct()+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productList[prodId].getProduct())
main()
