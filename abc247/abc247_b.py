import sys

N = int(input())
names = [input().split() for _ in range(N)]

for i in range(N):
    s, t = names[i]
    s_flag, t_flag = False, False
    for j in range(N):
        if i == j:
            continue
        tmps, tmpt = names[j]
        if s in (tmps,tmpt):
            s_flag = True
        if t in (tmps,tmpt):
            t_flag = True
        if s_flag and t_flag:
            print("No")
            sys.exit()
print("Yes")
