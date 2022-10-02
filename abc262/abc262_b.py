N, M = list(map(int, input().split()))

num_list = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    U, V = list(map(int, input().split()))
    num_list[U][V] = 1
    num_list[V][U] = 1

ans = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        for k in range(j, N + 1):
            if num_list[i][j] and num_list[j][k] and num_list[k][i]:
                ans += 1
print(ans)