N, A, B = list(map(int,input().split()))

for i in range(A*N):
    ans = ""
    for j in range(B*N):
        h = int(i/A)
        w = int(j/B)
        if (h + w) % 2 == 0:
            ans += "."
        else:
            ans += "#"
    print(ans)