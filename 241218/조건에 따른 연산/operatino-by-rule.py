cnt = 0 
n = int(input())

while True:
    if n % 2 == 0:
        n = n * 3 + 1
    
    else:
        n = n * 2 + 2
    
    cnt += 1

    if n >= 1000:
        break
    
print(cnt)