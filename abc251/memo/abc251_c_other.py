from collections import defaultdict
N = int(input())
sug = defaultdict(list)
ST = [input().split() for _ in range(N)]

top_idx = 0
top_score = 0

for i, st in enumerate(ST):
    s, t = st[0], int(st[1])
    if sug[s] == []:
        sug[s] = [int(t), i]
    if top_score < sug[s][0]:
        top_score = sug[s][0]
        top_idx = sug[s][1]

print(top_idx + 1)