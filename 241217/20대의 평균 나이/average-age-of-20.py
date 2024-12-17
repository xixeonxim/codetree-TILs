# 나이 입력 받기
ages = []

while True:
    age = int(input())
    if 20 <= age <= 29:
        ages.append(age)
    else:
        break

# 나이들의 평균 계산
average_age = sum(ages) / len(ages)

# 소수점 둘째 자리까지 반올림하여 출력
print(f"{average_age:.2f}")
