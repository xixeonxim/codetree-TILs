N = int(input())

for _ in range(N):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        print(a)