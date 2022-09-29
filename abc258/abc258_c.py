N, Q = list(map(int,input().split()))
s = input()

mx_len = 0
for _ in range(Q):
    q, x = list(map(int,input().split()))
    if q == 1:
        mx_len += x
    else:
        mx_len = mx_len % N
        indent = (x - mx_len) % N
        print(s[indent - 1])