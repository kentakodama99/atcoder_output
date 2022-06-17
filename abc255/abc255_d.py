import bisect

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

CumSum = [0] * (N + 1)
for i in range(1,N + 1):
    CumSum[i] = CumSum[i-1] + A[i - 1]

for _ in range(Q):
    x = int(input())
    k = bisect.bisect_left(A, x)
    sumlow = CumSum[k]
    sumhigh = CumSum[N] - CumSum[k]
    print((k * x - sumlow) + (sumhigh - (N - k) * x))