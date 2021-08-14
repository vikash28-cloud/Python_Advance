# ----------normal function----------/
'''def func(a):
    return a+50

print(func(20))'''

# -------lambda function----------/
# syntax =   lambda argument : expression

func = lambda x: x+54
square = lambda x: x*x
sum = lambda a,b,c: a+b+c
a= 3
print(func(a))     # it returns 57
print(square(a))   # it returns 9
print(sum(a,4,5))  # it returns 12