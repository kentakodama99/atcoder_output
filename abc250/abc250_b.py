N, A, B = list(map(int,input().split()))

tile1 = "."
tile2 = "#"
for a in range(A * N):
    view = ""
    if not a == 0 and a % A == 0:
        tile1, tile2 = tile2, tile1
    for n in range(N):
        view += tile1 * B if n % 2 == 0 else tile2 * B
    print(view)