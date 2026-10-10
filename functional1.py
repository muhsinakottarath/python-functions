from functools import reduce
# import functools

list1 = [i for i in range(1, 10)]

def square(i):
    return i*i

def isodd(i):
    if i%2==1:
        return True
    else:
        return False

squares = [i*i for i in list1]
print(squares)
squares = [square(i) for i in list1]
print(squares)

# map(function, collection)
# filter(function, collection)
# reduce(function, collection)
# generator

# list2 = list(map(square, list1))
# print(list(list2))

for i in map(square, list1):
    print(i)

for i in map(lambda i: i*i, list1):
    print(i)

list2 = list(filter(isodd, list1))
print(list2)

for i in filter(lambda i: i%2==1, list1):
    print(i)

# [1,2,3,4,5,6,7,8,9]
# a=1,b=2 = 3
# a=3,b=3 = 6
# a=6,b=4 = 10
# a=10,b=5 = 15
# a=15,b=6 = 21
# a=21,b=7 = 28
# a=28,b=8 = 36
# a=36,b=9 = 45
print(reduce(lambda a,b: a+b, list1))
print(reduce(lambda a,b: a+b, filter(lambda i: i%2==1, list1)))

list2 = [[1,2], [2,3], [3,4,5], [5,6], [6,7]]
# flattening -> collection of collection to one collection
# list3 = [1,2,2,3,3,4,5,5,6,6,7]
# a=[1,2],b=[2,3]
# [1,2,2,3]
# a=[1,2,2,3],b=[3,4,5]
# [1,2,2,3,3,4,5]..
print(reduce(lambda a,b: a+b, list2))





