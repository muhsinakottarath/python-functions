

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def operator(f, a, b):
    return f(a, b)

def operator2(op):
    if op=='add':
        return add
    elif op=='sub':
        return sub
    elif op=='mul':
        return mul
    elif op=='div':
        return div

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
operator1 = input("operator: ")

# if operator1=='add':
#     print("a = %f, b = %f, %s = %f" % (a, b, operator1, operator(add, a, b)))
# elif operator1=='sub':
#     print("a = %f, b = %f, %s = %f" % (a, b, operator1, operator(sub, a, b)))
# elif operator1=='mul':
#     print("a = %f, b = %f, %s = %f" % (a, b, operator1, operator(mul, a, b)))
# elif operator1=='div':
#     print("a = %f, b = %f, %s = %f" % (a, b, operator1, operator(div, a, b)))

f = operator2(operator1)
print("a = %f, b = %f, %s = %f" % (a, b, operator1, operator(f, a, b)))


