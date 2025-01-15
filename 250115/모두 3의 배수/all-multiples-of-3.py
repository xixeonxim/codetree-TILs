#5개의 정수 받기
arr = list(map(int, input().split())) #입력을 정수 리스트로 변환

#모든 3의 배수인지 확인하는 변수 
is_all_multiple_3 = True

#모두 3의 배수인지 확인

for num in arr:
    if num % 3 != 0:
        is_all_multiple_3 = False
        break

if is_all_multiple_3:
    print(1)
else:
    print(0)