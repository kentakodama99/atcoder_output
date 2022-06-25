N = int(input())
S = input()
A = list(map(int, input().split()))

mx = 0
A_data = []

for s in S:
    if int(s) == 1:
        mx += 1

for a, s in zip (A, S):
    A_data.append([a, int(s)])
A_data.sort(reverse=True, key=lambda x:x[1])
A_data.sort(key=lambda x:x[0])

tmp = mx
for i in range(0, N):
    if A_data[i][1] == 0:
        tmp += 1
    else:
        tmp -= 1
    mx = max(mx, tmp)

print(mx)