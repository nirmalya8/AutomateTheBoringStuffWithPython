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
    
