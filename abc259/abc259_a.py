N, M, X, T, D= list(map(int, input().split()))

if M > X:
    print(T)
else:
    print(T - (X - M) * D)