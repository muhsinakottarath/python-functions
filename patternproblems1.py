

n = input("Enter n: ")
n = int(n)

for i in range(1, n+1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

str1 = "hello "
print(str1 * 5)

for i in range(1, n+1):
    str1 = "%d " % (i)
    print(str1 * i)




