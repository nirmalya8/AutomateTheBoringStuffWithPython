  '''
  Say we have a list like
  [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

    In this script, we would print lists like the above
    in the form of a table, as shown below  
    apples    oranges    cherries    banana   

    Alice       Bob       Carol      David    

    dogs       cats      moose      goose    
'''


def printtable(table):
    for i in table:
        for j in i:
            print(j.center(10),end=' ')
        print('\n')

table = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]
printtable(table)
