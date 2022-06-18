import sys

h1, h2, h3, w1, w2, w3 = list(map(int, input().split()))

if not h1 + h2 + h3 == w1 + w2 + w3:
    print(0)
    sys.exit()

cnt = 0
'''
a b c
d e f
g h i
'''
# grid[i][j] + 1 - 2 = grid[i][j] - 1
for a in range(1, min(h1 - 1, w1 - 1)):
    for b in range(1, min(h1 - 1, w2 - 1)):
        c = h1 - (a + b)
        if c < 1: break
        for d in range(1, min(h2 - 1, w1 - 1)):
            g = w1 - (a + d)
            if g < 1: break
            for e in range(1, min(h2 - 1, w2 - 1)):
                f = h2 - (d + e)
                h = w2 - (b + e)
                if min(f, h) < 1: break
                if h3 - (g + h) == w3 - (c + f) and w3 - (c + f) > 0:
                    cnt += 1

print(cnt)