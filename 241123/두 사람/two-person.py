per1 = input().split()
per1_age = int(per1[0])
per1_gen = per1[1]

per2 = input().split()
per2_age = int(per2[0])
per2_gen = per2[1]

if (per1_age >= 19 and per1_gen == "M") or (per2_age >= 19 and per2_gen == "M"):
    print("1")
else:
    print("0")