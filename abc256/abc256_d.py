N = int(input())

st = []
fi = []
for i in range(N):
    x, y = list(map(int, input().split()))
    st.append(x)
    fi.append(y)

# imos法
MAX_NUM = max(fi)
imos = [0] * (MAX_NUM + 1)
for i in range(N):
    imos[st[i]] += 1
    imos[fi[i]] -= 1

# シミュレート
for i in range(1, MAX_NUM + 1):
    imos[i] += imos[i - 1]

ans = []
top = 0
for i in range(1, MAX_NUM + 1):
    if imos[i] and top == 0:
        top = i
    if not imos[i] and top > 0:
        ans.append([top, i])
        top = 0

for a in ans:
    print(*a)