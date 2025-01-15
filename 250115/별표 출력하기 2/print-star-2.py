n = int(input())

for i in range(n, 0, -1):  # n부터 1까지 반복
    for j in range(i):  # i개의 별 출력
        print("*", end=" ")
    print()  # 줄바꿈
