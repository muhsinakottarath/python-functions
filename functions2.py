
def subtract(a, b):
    return a-b

def subtract3(a, b, c):
    return c-b-a

def multiply(a, b=2):
    return a*b

def multiply3(a, b=2, c=3):
    return a*b*c

c = subtract(2, 1)
print(c)

c = subtract(b=1, a=2)
print(c)

# once you have specified a parameter with a name when the
# function is called, will have to pass other params with name
# only

# c = subtract(b=1,a=2)

c = subtract3(1,2,3)
print(c)
# named parameter
c = subtract3(c=3,a=1,b=2)
print(c)

c = subtract3(1, c=3, b=2)
print(c)

c = multiply(2)
print(c)
c = multiply(2, 4)
print(c)

c = multiply3(3)
print(c)
c = multiply3(3, 3)
print(c)
c = multiply3(3, 3, 4)
print(c)

c = multiply3(3, c=5, b=2)
print(c)






