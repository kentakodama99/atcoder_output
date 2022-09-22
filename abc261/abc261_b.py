import sys

N = int(input())
A = [input() for _ in range(N)]

loop_cnt = N
for i in range(N):
    for re_j in range(loop_cnt - 1):
        j = N - re_j - 1
        if (A[j][i] == "D" and not A[i][j] == "D") or (not A[j][i] == "D" and A[i][j] == "D"):
            print("incorrect")
            sys.exit()
        elif A[i][j] == A[j][i] and not (A[j][i] == "D" or A[i][j] == "D"):
            print("incorrect")
            sys.exit()
    loop_cnt -= 1

print("correct")