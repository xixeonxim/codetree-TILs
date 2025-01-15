
n = int(input())
satisfied = True

for i in range(2, n):
    # 1과 자기자신을 제외한 약수가 없다면 그 수는 소수이다. 
    if n % i == 0:
        satisfied = False


if satisfied == True:
    print("P")
else:
    print("C")