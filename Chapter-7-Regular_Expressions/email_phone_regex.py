'''
The problem statement goes: Suppose there is a huge passage
and you want to find out all the email addresses and phone 
numbers in the passage. So, we have to use Regular Expressions
to do this task and use pyperclip to copy or paste stuff from 
or onto the clipboard

Valid Phone numbers - 
123-456-7890, 123 456 7890, 123.456.7890 The first three numbers
might also be contained in a parenthesis. The last part is an optional
extension made up of any number of spaces followed by ext, x, or ext.,
followed by two to five digits.
Valid Email format -
abc@domain.extension 
'''
import pyperclip
import re

p  = str(pyperclip.paste())

phone  = re.compile(r''' (
                        (\d{3}|\(\d{3}\))? #area code
                        (\s|\.|-)  #separator
                        (\d{3}) #next three numbers
                        (\s|\.|-) #separator
                        (\d{4}) #last four digits
                        (\s*(ext\.|ext|x)\s*(\d{2,5}))? #final extension
                        )''',re.VERBOSE)

email = re.compile(r''' (
                        ([A-Za-z0-9._%+-]+)
                        @
                        ([A-Za-z0-9.-]+)
                        \.[A-Za-z]{2,4}
                        )''',re.VERBOSE)


matches = []
for groups in phone.findall(p):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in email.findall(p):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')