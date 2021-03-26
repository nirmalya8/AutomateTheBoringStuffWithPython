import random
def collatz(n):
    if n==1:
        return
    elif n%2 == 0:
        print(n//2)
        collatz(n//2)
    else :
        print(3*n +1)
        collatz(3*n +1)

try:
    n = int(input("Enter a number:"))
    collatz(n)       
    print("-------------DONE-------------")
except ValueError:
    print("Enter an integer")
