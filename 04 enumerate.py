# --------------enumerate function-----------/
list  = ["vikash", 45.23,True,37,23]
index = 1
for items in list:
    print(f"{index}. {items}")
    index +=1

            #or
for index, item in enumerate(list): #enumerate function
    print(index,item)