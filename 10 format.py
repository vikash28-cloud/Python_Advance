name = "vikash sharma"
profession = 'data scientist'
age = 18

#a = f"hello my name is {name}, my profession is {profession} and my age is {age} "
#a = "this is {}".format(name)
#a = "this is {} and my profession is {}".format(name,profession)
a = "this is {}, profession{} and age is {}".format(profession,name,age)
a = "this is {1}, profession is {0} and age is {2}".format(profession,name,age)
print(a)