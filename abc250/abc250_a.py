H, W = list(map(int,input().split()))
R, C = list(map(int,input().split()))

a = (R == 1 or R == H)
b = (C == 1 or C == W)

if H == 1 and W == 1:
    print("0")
elif H == 1 or W == 1:
    print("1" if a and b else "2")
elif a and b:
    print("2")
elif (a and not b) or (not a and b):
    print("3")
else:
    print("4")