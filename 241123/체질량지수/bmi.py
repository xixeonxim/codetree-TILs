arr = input().split()

h = int(arr[0])
w = int(arr[1])
b = int((10000 * w) / (h * h))

print(b)

if b >= 25:
    print("Obesity")

