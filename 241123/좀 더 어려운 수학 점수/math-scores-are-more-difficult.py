arr1 = input().split()
arr2 = input().split()

a_math = int(arr1[0])
a_eng = int(arr1[1])

b_math = int(arr2[0])
b_eng = int(arr2[1])

if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print("A")
else:
    print("B")