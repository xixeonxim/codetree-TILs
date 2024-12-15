n = int(input())
sum_val = 0

for _ in range(n):
    score = int(input())
    sum_val += score

avg = sum_val / n

print(f"{sum_val} {avg:.1f}")