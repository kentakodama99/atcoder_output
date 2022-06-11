N, K = list(map(int,input().split()))
A = list(map(int,input().split()))


B = [None] * K
for i in range(K):
    B[i] = sorted(A[i::K])

ans = 'Yes'
prev = 0
for i in range(N):
    q, r = divmod(i, K)
    if B[r][q] < prev:
        ans = 'No'
        break
    prev = B[r][q]
print(ans)