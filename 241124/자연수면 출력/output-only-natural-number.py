arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a > 0:
    for i in range(b):
        print(a, end = "")
else:
    print(0)