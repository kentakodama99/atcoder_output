N = int(input())
a = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i, x in enumerate(a):
    if i == (x - 1):
        cnt1 += 1
    elif i > (x - 1) and i == (a[x - 1] - 1):
        cnt2 += 1

print((cnt1 * (cnt1 - 1) // 2) + cnt2)