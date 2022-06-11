from math import sqrt
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
XY = [input().split() for _ in range(N)]
 
mx_dis = []
for i in range(N):
    if i + 1 in A:
        continue
    x, y = int(XY[i][0]) ,int(XY[i][1])
    mn = float("inf")
    for a in A:
        a1,b1 = int(XY[a - 1][0]), int(XY[a - 1][1])
        mn = min(mn, float(abs(a1 - x) ** 2 + abs(b1 - y) ** 2))
    mx_dis.append(mn)
 
print(f"{sqrt(max(mx_dis)):.20f}")