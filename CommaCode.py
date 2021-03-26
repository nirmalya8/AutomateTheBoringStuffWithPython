'''
In CommaCode, we take the input as a list
and the output is basically the elements
separated by commas and a space and the
last element is preceeded by the string
'and'.

Example:
Input: [1,2,3,4,5]
Output: 1, 2, 3, 4 and 5
'''
def commacode(l):
    s = ""
    for i in range(len(l)):
        if i==0:
            s = s+l[i]
        elif i<len(l)-1:
            s = s+", "+l[i]
        elif i == len(l)-1:
            s = s+" and "+l[i]

    return s

n = int(input("Enter the number of elements in the list : "))
print("Enter {} elements: ".format(n))
l = []
for i in range(n):
    inp  = input()
    l.append(inp)

print("Comma Code is: ")
print(commacode(l))
      
