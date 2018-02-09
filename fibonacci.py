#fibonacci.py
#This program calculates the fibonacci sequence to the nth term
def main():
    print("This program calculates the Fibonacci Sequence to the nth term")
    n = int(input("Enter the number of terms to calculate to:"))
    if n < 3:
        print("The", n, "th term in the Fibonacci sequence is 1")
    fibPrev = 1
    fib = 1
    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    print("The", n, "th term in the Fibonacci sequence is:", fib)
main()

