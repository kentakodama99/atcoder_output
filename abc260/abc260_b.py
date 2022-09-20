N, X, Y, Z = list(map(int, input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ex_idx = [0] * N
A_id = []
B_id = []
C_id = []
for i in range(N):
    A_id.append([A[i], i])
    B_id.append([B[i], i])
    C_id.append([A[i] + B[i], i])

A_id.sort(key=lambda x: x[1])
A_id.sort(reverse=True, key=lambda x: x[0])

B_id.sort(key=lambda x: x[1])
B_id.sort(reverse=True, key=lambda x: x[0])

C_id.sort(key=lambda x: x[1])
C_id.sort(reverse=True, key=lambda x: x[0])

for i in range(X):
    idx = A_id[i][1]
    ex_idx[idx] = 1

cnt = 0
for i in range(N):
    if cnt >= Y:
        break
    idx = B_id[i][1]
    if not ex_idx[idx]:
        ex_idx[idx] = 1
        cnt += 1

cnt = 0
for i in range(N):
    if cnt >= Z:
        break
    idx = C_id[i][1]
    if not ex_idx[idx]:
        ex_idx[idx] = 1
        cnt += 1

for i in range(N):
    if ex_idx[i]:
        print(i + 1)