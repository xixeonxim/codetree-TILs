arr = input().split()

a, b = int(arr[0]), int(arr[1])

if (a % 2 == 0) and (b % 2 == 0):
    for i in range(a+1, b, 2):
        print(i, end = " ")

elif (a % 2 == 1) and (b % 2 == 1):
    for i in range(a, b+1, 2):
        print(i, end = " ")
elif (a % 2 == 0)  and (b % 2 == 1):
    for i in range(a+1, b+1, 2):
        print(i, end = " ")
else:
    for i in range(a, b, 2):
        print(i, end = " ")