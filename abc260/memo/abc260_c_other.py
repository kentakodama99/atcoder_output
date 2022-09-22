import sys

N, X, Y = list(map(int, input().split()))

if N == 1:
    print(0)
    sys.exit()

r = [0] * (10 + 1)
b = [0] * (10 + 1)

# level1はこれ以上増えない
# level1の赤い宝石を1個持っている状態でのlevel1の青い宝石の個数
r[1] = 0 # そもそもたどり着けない
# level1の青い宝石を1個持っている状態でのlevel1の青い宝石の個数
b[1] = 1 # たどり着けないので元々持ってる1個

for i in range(2, N + 1):
    b[i] = r[i - 1] + b[i - 1] * Y
    r[i] = r[i - 1] + b[i] * X

print(r[N])