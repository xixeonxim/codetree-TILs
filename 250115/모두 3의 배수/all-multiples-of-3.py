
p = True
for _ in range(5):
    n = int(input())

    if n % 3 == 0:
        continue
    else:
        p = False
        break
    
if p == True:
    print(1)
else:
    print(0)
