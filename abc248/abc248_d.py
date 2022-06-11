import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

query = [map(int, input().split()) for _ in range(Q)]

posi_memo = [[] for _ in range(2*10**5+1)]
for i in range(N):
    posi_memo[A[i]].append(i+1)

for q in query:
    L, R, X = q
    tmp = posi_memo[X] 
    if tmp:
        print(bisect.bisect_right(tmp, R)-bisect.bisect_left(tmp, L))
    else:
        print(0)