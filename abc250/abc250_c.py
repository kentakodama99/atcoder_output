N, Q = map(int, input().split())
A = list(range(N + 1))
idxs = list(range(N + 1))

for _ in range(Q):
    q = int(input())
    q_num = idxs[q]

    if q_num == N:
        st, fi = N - 1, N
    else:
        st, fi = q_num, q_num + 1
    
    A[st], A[fi] = A[fi], A[st]
    idxs[A[st]], idxs[A[fi]] = idxs[A[fi]], idxs[A[st]]
print(*A[1:])