N = int(input())

a = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        a[i].append(1 if j == 0 or j == i else a[i - 1][j - 1] + a[i - 1][j])
    print(*a[i])