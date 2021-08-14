#reduce function: reduce applies a rolling computation to sequential pair of element
# syntax: val =reduce(function, list)

from functools import reduce

l = [1,2,3,4,5]
sum = lambda a,b : a+b
val = reduce(sum,l)
print(val)