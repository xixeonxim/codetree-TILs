sum_val = 0
cnt = 0

while True:
    n = int(input())  # 나이 입력 받기

    if n < 30:  # 30 미만의 나이는 20대
        sum_val += n
        cnt += 1
    else:
        break  # 20대가 아닌 사람이 나오면 종료

# 20대의 나이들의 평균 계산
if cnt > 0:
    avg = sum_val / cnt
    print(f"{avg:.2f}")  # 소수점 둘째자리까지 출력
