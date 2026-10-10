
# def values(n):
#     list1 = []
#     for i in range(n):
#         list1.append(i)
#     return list1


def values(n):
    for i in range(n):
        print("yielding %d" % (i))
        yield i*i

for i in values(10):
    print("main %d" % (i))
    print(i)







