N=int(input())
A=list(map(int,input().split()))

UPPER = 2 * 10 ** 5
cnt = [0] * (UPPER + 1)

for i in range(N):
    cnt[A[i]] += 1

for i in range(UPPER):
    cnt[i + 1] += cnt[i]

ans = 0
for i in range(N):
    ans += cnt[A[i] - 1] * (N - cnt[A[i]])
print(ans)