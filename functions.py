

# def functionname([parameters]):
#     code

def add(a, b):
    return a+b

def display(name):
    print("hello "+name)

count = 0

def countvalues():
    global count
    count += 1

c = add(1,2)
print(c)

display("santhosh")

countvalues()
countvalues()

print(count)

# count is countsvalue
# print("Count is "+str(count))

print("Count is %d" % (count))

a = 1
b = 2

# a = 1, b = 2, sum = 3
print("a = %d, b = %d, sum = %d" % (a, b, a+b))

str1 = "a is %d, b is %d, sum is %d" % (a, b, a+b)
print(str1)

