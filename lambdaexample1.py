
def add(a, b):
    return a+b

def operator(f,a,b):
    return f(a, b)

c = operator(add, 1, 2)
print(c)

# lambda expressions
# anonymous function - it doesnt have a name for the function
# lambda [param1,[params]]: expression

c = operator(lambda a,b: a+b, 1, 2)
print(c)

f = lambda a,b: a+b
c = operator(f, 1, 2)
print(c)
f = lambda a,b: a-b
c = operator(f, 2, 1)
print(c)


