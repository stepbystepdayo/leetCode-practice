x = 2
y = 3

# need to be True both between and
compound = x + y and y + x  > 2


# need to be either right or left is true 
compound2 = x + y or y+x < 2


# not True = False then, False == False is True
compound3 = not True == False # True

'''
this is a lower precedence
compound4 = True == not False 
this is going to be ERROR 
compound4 = True == (not False) it will run () first 

'''

# DeMogan's Low

not (x and y) == (not x) or *(not y)

'''
conditional / comparison operators
Not
And 
Or

'''


