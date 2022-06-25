N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = list(map(int, input().split()))

table = [0] * (N + 1)
for i in A:
    table[i] = 1

for l in L:
    target = A[l - 1]
    if target == N or table[target + 1]:
        continue
    table[target], table[target + 1] = 0, 1
    A[l - 1] = target + 1

res = []
for i in range(1, N + 1):
    if table[i]: res.append(i)
print(*res)