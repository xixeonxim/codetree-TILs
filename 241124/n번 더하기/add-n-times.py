arr = input().split()

a = int(arr[0])
n = int(arr[1])

a += n

for i in range(n):
    print(a)
    a += n
