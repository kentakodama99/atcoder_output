from collections import defaultdict
import sys

N = int(input())
d = defaultdict(int)
res = ""
for i in range(N):
    s = input()
    cnt = d[s]
    if cnt > 0:
        print(f"{s}({cnt})")
    else:
        print(f"{s}")
    d[s] += 1
