import sys

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = max(A)
for b in B:
    if A[b-1] == m:
        print("Yes")
        sys.exit()
print("No")