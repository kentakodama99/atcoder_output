from collections import defaultdict
N = int(input())
sug = defaultdict(int)
ST = [input().split() for _ in range(N)]

top_idx = 0
top_score = -1

for i, st in enumerate(ST):
    s, t = st[0], int(st[1])
    if not sug[s] and t > top_score:
        top_idx = i
        top_score = t
    if not sug[s]:
        sug[s] = 1
print(top_idx + 1)