import sys

X, A, D, N = map(int, input().split())
if D == 0:
    print(abs(X - A))
    sys.exit()
# 公差の符号によって大小関係の正規化
elif D < 0:
    st, fi = A + (N - 1) * D, A
    D = -D
else:
    st, fi = A, A + (N - 1) * D
    
f = lambda n : st + (n - 1) * D
# 二分探索で最小距離更新
r = 1
l = N
ans = min(abs(st - X), abs(fi - X))

while abs(r - l) > 1:
    c = (r + l) // 2
    if st <= f(c) <= fi or fi <= f(c) <= st:
        ans = min(ans, abs(X - f(c)))
    if f(c) <= X:
        r = c
    else:
        l = c

print(ans)