'''
Say you copied a few lines from anywhere and you want bullets
in front of each new line. Before running this script, we have
to copy those lines from somewhere. pyperclip.paste() will 
take those lines from the clipboard. 
'''

import pyperclip
s = pyperclip.paste()
l = s.split('\r\n')
s1 = ""
for i in l:
    s1 += '*'.ljust(4)+i+'\n'
    
    

print(s1)
