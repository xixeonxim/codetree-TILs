arr = input().split()

a = int(arr[0])
b = int(arr[1])

if b >= a:
    for i in range(b,a-1, -1):
        print(i, end = " ")
else:
    for i in range(a, b-1, -1):
        print(i, end = " ")