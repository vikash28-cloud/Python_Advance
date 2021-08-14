# -------file not found error-------/
'''def readfile(fname):
    try:
        with open(fname , "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"file {fname} is not found")

readfile("01.txt")
readfile("02.txt")
readfile("03.txt")'''
# ----------list comprehension programme----/
'''list = [1,2,3,4,5,6,7,8]

b= [list[3],list[5],list[7]]
print(b)'''
       #or
#---------enumerate function-----------------/       
'''l = [1,2,3,4,5,6,7,8,9,10] 
for index, item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"the {index+1}th element is {item}")'''

# ----------multiplication table using list comprehension------/
'''while (True):
    num = input("enter the no. here: ")
    if( num=="q"):
        break
    try:
        num = int(num)
        table_list = [num*i for i in range(1,11)]
        print(table_list)
    except Exception as e:
        print("sorry!\nplease enter a valid number")
print("Thanks! for using python multiplicator")'''

#------zero division error----------/
'''a = int(input('enter the no. here: '))
b = int(input("enter the no. here: "))
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e)
    print("Infinite(oo)")'''

#-----------tables store in a i/o file----------/
num = int(input("enter the no. here: "))
table = [num*i for i in range(1,11)]    
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table)) 
    f.write('\n')



