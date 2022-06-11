h, w = map(int, input().split())
s = [input() for _ in range(h)]
pieces = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            pieces.append((i, j))
a, b = pieces[0]
c, d = pieces[1]
print(abs(a - c) + abs(b - d))