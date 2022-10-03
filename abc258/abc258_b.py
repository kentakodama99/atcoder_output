N = int(input())
A = list(input() for _ in range(N))

X = [1, 1, 0, -1, -1, -1, 0, 1]
Y = [0, -1, -1, -1, 0, 1, 1, 1]
mx_num = 0

for i in range(N):
    for j in range(N):
        first = A[i][j]
        for x, y in zip(X, Y):
            num = ""
            point = [int(i), int(j)]
            for _ in range(N):
                yy = point[0] + y
                xx = point[1] + x
                point[0] = yy % N if yy >= 0 else N - 1
                point[1] = xx % N if xx >= 0 else N - 1
                num += A[point[0]][point[1]]
            mx_num = max(mx_num, int(num))

print(mx_num)