N = int(input())
A = list(map(int,input().split()))

M = max(A)
cnt = [0] * (M + 1)
ans = 0

for i in range(N):
    cnt[A[i]] += 1

for j in range(1, M + 1):
    for k in range(1, M // j + 1):
        ans += cnt[j * k] * cnt[j] * cnt[k]
print(ans)