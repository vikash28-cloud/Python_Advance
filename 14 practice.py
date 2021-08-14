# --------------format problem-------------/
'''name = input("enter your name: ")
marks =input("enter your marks: ")
phone = input("enter your  phone no.: ")

template = "the name of the student is {}, his marks are {} and phone number is {}"
output = template.format(name,marks,phone)
print(output)'''

# ----------------vertical table of 7-----------/
'''l = [str(i*7) for i in range(1,11)]
print(l)


verticalTable = "\n".join(l)
print(verticalTable)'''

# -------------filter problem----/
'''l = [5,3,98,25,35,85,90,54,75,454,23,455,590]

x = filter(lambda x: x%5==0, l)
print(list(x))'''

# ------------reduce problem------------/
from functools import reduce
l = [329, 902, 920, 74, 72918, 9200844]

a  =reduce(max, l)
print(a)
