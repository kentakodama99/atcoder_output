import sys

def conv(text):
    res = []
    cnt = 0
    last = ""
    for te in text:
        if te == last:
            cnt += 1
        else:
            if cnt > 0:
                res.append((last, cnt))
            last = te
            cnt = 1
    res.append((last, cnt))
    return res

S = conv(input())
T = conv(input())

if not len(S) == len(T):
    print("No")
    sys.exit()

for s, t in zip(S, T):
    if not s[0] == t[0] or s[1] > t[1] or (s[1] == 1 and 1 < t[1]):
        print("No")
        sys.exit()
print("Yes")