'''
Version 1 of Collatz

What is Collatz?
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.

This version:
In this version of Collatz, I have used the random.randint function to generate
numbers and for 2 of such random numbers, I have performed the Collatz Operation.
To continually call the collatz function till it returns a 1, I have used an external
loop.
'''
import random
def collatz(n):
    if n%2 == 0:
        return n//2
    else :
        return 3*n +1

for i in range(2):
    n = random.randint(1,100)
    while(collatz(n)!= 1):
        print(collatz(n))
        n = collatz(n)
    else:
        print("1")
        print("-------------DONE-------------")
    
