from math import sqrt, ceil

N = int(input())

commit_num = [0] * (N ** 2 + 1)
root = []
for i in range(1, N + 1):
    root.append(i * i)

def make_divisors(n : int) -> list:
    cnt = 0
    i = 1
    while i*i <= n:
        # print(i * i)
        if not commit_num[i] and n % i == 0:
            # print(i, n // i, n)
            if not i == n // i:
                cnt += 2
            else:
                cnt += 1
            commit_num[i] += 1
        i += 1
    return cnt

res = 0
# print(root)
for i in root:
    # print(make_divisors(i))
    res += make_divisors(i)
print(res)
# print(commit_num)

