import sys

X,A,D,N=map(int,input().split())

if D == 0: # 公差が固定
    print(abs(A - X))
    sys.exit()
m = A + (N - 1) * D # 末項
ans = min(abs(A - X), abs(m - X)) # 初項、末項とXの差の最小値
# print(ans)
y = A + (X - A) // D * D # A + |(X - A) / D| * D
print(y)
for i in range(-2, 3): # 周辺±2程度探索
    z = y + i * D
    if A <= z <= m or m <= z <= A: # 探索範囲内に存在するかどうか
        ans = min(ans, abs(z - X))
print(ans)