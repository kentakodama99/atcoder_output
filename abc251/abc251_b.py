N, W = list(map(int,input().split()))
A = list(map(int,input().split()))

sum_num = [0] * (10 ** 6 + 1)

ans = 0
for i in range(N):
    tmp = A[i]
    if tmp <= W and not sum_num[tmp]:
        ans += 1
        sum_num[tmp] = 1
    for j in range(i + 1, N):
        tmp = A[i] + A[j]
        if tmp <= W and not sum_num[tmp]:
            ans += 1
            sum_num[tmp] = 1
        for k in range(j + 1, N):
            tmp = A[i] + A[j] + A[k]
            if tmp <= W and not sum_num[tmp]:
                ans += 1
                sum_num[tmp] = 1
print(ans)