arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 중앙값 구하기
if (b < a and a < c) or (c < a and a < b):
    print(a)
elif (a < b and b < c) or (c < b and b < a):
    print(b)
else:
    print(c)
