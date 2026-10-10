def fib(n):
    n1 = 0
    n2 = 1
    for i in range(n):
            i = n1+n2
            n1 = n2
            n2 =i
            print(n1, end=" ")
a =int(input("enter n"))
fib(a)



