# n 입력받기
n = int(input())

#한 줄에 * 4개씩 출력하기 -> 안쪽 가로
# 이후 바깥 쪽에 4줄로 출력하기 위해 반복문 4번

for _ in range (n):
    for _ in range(n):
        print("*", end = "")
    print()