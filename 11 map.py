# map function: map applies a function to all the items in an input list
    # syntax: list(map(function, list))
    
def square(num):
    return num*num

l =[1,2,3,4,5]

# method 1
'''l2 = []
for item in l:
    l2.append(square(item))
print(l2)'''

# method 2  map method
print(list(map(square,l)))

