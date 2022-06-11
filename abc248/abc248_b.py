A, B, K = list(map(int,input().split()))
cnt = 0
while A < B:
    A *= K
    cnt += 1
print(cnt)