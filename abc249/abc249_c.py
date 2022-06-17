from itertools import product

N, K = list(map(int,input().split()))
S = [input() for _ in range(N)]
res = 0

for bit in product(range(2), repeat=N):
    cnt = 0
    al = [0] * 26
    for i in range(N):
        if bit[i] == 1:
            for s in S[i]:
                al[ord(s) - ord("a")] += 1
    for a in al:
        if a == K:
            cnt += 1
    res = max(res, cnt)

print(res)