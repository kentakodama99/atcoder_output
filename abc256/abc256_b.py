N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    tmp = A[i]
    if A[i] >= 4:
        cnt += 1
        continue
    for j in range(i + 1, N):
        tmp += A[j]
        if tmp >= 4:
            cnt += 1
            break
print(cnt)