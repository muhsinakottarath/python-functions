

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

# operator a higher order function
# it is accepting a function as a reference
def operator(f, a, b):
    return f(a, b)

c = operator(add, 1, 2)
print(c)
c = operator(sub, 2, 1)
print(c)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# op = "add","sub","mul","div"
# a = v1, b = v1, and op = result
# a = int(a)
# b = int(b)

print(a+b)



