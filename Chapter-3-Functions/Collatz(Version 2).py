'''
Version 2 of Collatz

What is Collatz?
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.

This version:
In this version of Collatz, I have used Recursion in the Collatz function and I
have validated the input by using the try and except block. As I have used recursion,
I didn't have to write an external loop calling the Collatz function again and again
until it returns 1. 
'''
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
