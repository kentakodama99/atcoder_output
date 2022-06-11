H, W = list(map(int,input().split()))
R, C = list(map(int,input().split()))
res = 0

if R - 1 > 0: res += 1 # top
if R + 1 <= H: res += 1 # bottom
if C - 1 > 0: res += 1 # left
if C + 1 <= W: res += 1 # right
print(res)