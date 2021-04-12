'''
This script checks whether a password is STRONG or not
using Regular Expressions. A password will be considered to be
strong iff it contains a lower casealphabet, an uppercase alphabet,
a digit and has a minimum length 8.
'''
import re
strong = re.compile(r'([a-z][A-Z][0-9]){8,}')
p = input("Enter passowrd")
if strong.search() != None:
    print("Strong password!")
else:
    print("Weak password")

    