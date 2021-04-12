'''
This script checks whether a password is STRONG or not
using Regular Expressions. A password will be considered to be
strong iff it contains a lower casealphabet, an uppercase alphabet,
a digit and has a minimum length 8.
'''
import re
l = re.compile(r'.{8,}')
small = re.compile(r'[a-z]{1,}')
capital  = re.compile(r'[A-Z]{1,}')
dig = re.compile(r'[0-9]{1,}')
p = input("Enter passowrd")
try:
    s = l.search(p).group()
    s = small.search(p).group()
    s = capital.search(p).group()
    s = dig.search(p).group()
    print("Strong Password")
except AttributeError:
    print("Weak Password")
#if strong.search(p) != None:
#    print("Strong password!")
#else:
#    print("Weak password")

    