# ----------------list comprihensions----------------/

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
'''even = []
for item in list:
    if item%2==0:
        even.append(item)
        
print(even)'''

            # or
'''a  = [item for item in list if item%2==0 ]   # list comprehension
print(a)'''

#---------programme to make a list of even no. in a range--------#
'''num  = int(input("enter num: "))
list = []
for num in range (1,num+1):
    list.append(num)
even  = []
for item in list:
    if item%2==0:
        even.append(item)
print(even)'''

#-----------------set comprihension-------------------/
a  = [1,2,2,3,3,4,4,5,5,6,6,7,8,9,10]
set = {item for item in a if item%2==0}
print(set)
print(type(set))



