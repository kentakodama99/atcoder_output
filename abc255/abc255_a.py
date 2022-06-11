R, C = list(map(int, input().split()))

for i in range(max(R, C)):
    A = list(map(int, input().split()))
    if i + 1 == R:
        print(A[C - 1])
        exit()