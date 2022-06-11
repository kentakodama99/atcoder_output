import heapq
from collections import defaultdict
Q = int(input())

cnt = defaultdict(int)
mx = []
mn = []
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x = q[1]
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)
        cnt[x] += 1
    elif q[0] == 2:
        x, c = q[1], q[2]
        cnt[x] = max(0, cnt[x] - c)
    elif q[0] == 3:
        while cnt[-mx[0]] == 0:
            heapq.heappop(mx)
        while cnt[mn[0]] == 0:
            heapq.heappop(mn)
        print(-mx[0] - mn[0])