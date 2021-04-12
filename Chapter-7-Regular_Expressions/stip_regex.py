'''
This script is an imitation of the strip() method for strings.
What it basically does is remove the spaces preceeding and 
succeeding characters in a string using RegEx.
So, for eg, "   ABCD    " will become "ABCD"
'''

import re
s = input("Enter the string")
print(f"The string with preceeding and succedding spaces \n {s}")
startsp = re.compile(r'^(( )?)*')
endsp = re.compile(r'(( )?)*$')
s = startsp.sub("",s)
s = endsp.sub("",s)
print(s)
