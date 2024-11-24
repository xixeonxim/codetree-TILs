per1 = input().split()
per1_c, per1_t = per1[0], int(per1[1])

per2 = input().split()
per2_c, per2_t = per2[0], int(per2[1])

per3 = input().split()
per3_c, per3_t = per3[0], int(per3[1])

if per1_c == "Y" and per1_t >= 37:
    if (per2_c == "Y" and per2_t >= 37) or (per3_c == "Y" and per3_t >= 37):
        print("E")
    else:
        print("N")

else:
    if (per2_c == "Y" and per2_t >= 37) and (per3_c == "Y" and per3_t >= 37):
        print("E")
    else:
        print("N")