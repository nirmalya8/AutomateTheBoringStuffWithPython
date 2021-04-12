'''
This script checks whether a password is STRONG or not
using Regular Expressions. A password will be considered to be
strong iff it contains a lower casealphabet, an uppercase alphabet,
a digit and has a minimum length 8.
'''
import re
strong = re.compile(r'([A-Z]|[a-z]|[0-9]){8,}')
p = input("Enter passowrd")
try:
    s = strong.search(p).group()
    print("Strong Password")
except AttributeError:
    print("Weak Password")
#if strong.search(p) != None:
#    print("Strong password!")
#else:
#    print("Weak password")

    