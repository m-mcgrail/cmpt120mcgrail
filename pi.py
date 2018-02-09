#pi.py
#This program approximates the value of pi by summing terms in a series
import math
def pi():
    print("This program approximates the value of pi by summing terms in a series")
    n=int(input("Enter the number of terms to use:"))
    pi = 0
    sign = 1
    for i in range(1, n * 2 + 1, 2):
        term = 4 / i * sign
        pi = pi + term
        sign = sign * -1
    print("The approximate value of pi is:", pi)
    dif = (math.pi) - pi
    print("The difference between pi and this approximation is", dif)
pi()
    
