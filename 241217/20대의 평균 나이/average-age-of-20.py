cnt = 0
sum_val = 0 

while True:
    n = int(input())

    if n < 30:
        sum_val += n
        cnt += 1
    
    else:
        break

if cnt > 0:
    avg = sum_val / cnt
    print(f"{avg:.2f}")