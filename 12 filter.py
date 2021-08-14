
# filter syntax: list(filter(function, list))
def greaterThan5(num):
    if num>5:
        return True
    else:
        return False
    

l = [1,2,3,5,6,5,34,34,7,8762,2677,343,67]
print(list(filter(greaterThan5, l)))



lambdaFunc = lambda num: num>10
print(list(filter(lambdaFunc, l)))