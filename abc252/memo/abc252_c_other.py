N = int(input())
S = [input() for i in range(N)]


cnt = [[0] * 10 for _ in range(10)]

for n in range(N):
    for i in range(10):
        v = int(S[n][i])
        cnt[v][i] += 1

res = [0] * 10

for i in range(10):
    for j in range(10):
        res[i] = max(res[i], 10 * (cnt[i][j] - 1) + j)
        
print(min(res))