L1, R1, L2, R2 = list(map(int, input().split()))

if L1 > L2:
    if R1 < R2:
        print(R1 - L1)
    else:
        print(R2 - L1 if R2 - L1 > 0 else 0)
else:
    if R1 > R2:
        print(R2 - L2)
    else:
        print(R1 - L2 if R1 - L2 > 0 else 0)