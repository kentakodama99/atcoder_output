

N = int(input())
A = list(input() for _ in range(N))


res_str = {}
res = 0

for i in range(N):
    res_str["sum_x"] = ""
    res_str["sum_y"] = ""
    res_str["sum_xy"] = ""
    res_str["sum_re_xy"] = ""
    sum_x = 0 # 横方向
    sum_y = 0 # 縦方向
    sum_xy = 0 # 45度方向
    sum_re_xy = 0 # 135度方向
    
    max_n = 0
    max_idx = 0
    for i, a in enumerate(A[i]):
        sum_x += int(a)
        res_str["sum_x"] += a
        if max_n < int(a):
            max_n = int(a)
            max_idx = i
    
    sum_y = int(A[i][max_idx])
    res_str["sum_y"] += A[i][max_idx]
    sum_xy = int(A[i][max_idx])
    res_str["sum_xy"] += A[i][max_idx]
    sum_re_xy = int(A[i][max_idx])
    res_str["sum_re_xy"] += A[i][max_idx]
    idx = max_idx
    re_idx = max_idx

    for j in range(N):
        if i == j:
            continue
        sum_y += int(A[j][max_idx])
        res_str["sum_y"] += A[j][max_idx]
        idx = (idx + 1) % N
        re_idx = (re_idx - 1) % N if (re_idx - 1) % N >= 0 else N - 1
        sum_xy += int(A[j][idx])
        res_str["sum_xy"] += A[j][idx]
        sum_re_xy += int(A[j][idx])
        res_str["sum_re_xy"] += A[j][idx]
    
    if res > sum_x:
        res_str["sum_y"]
    res = max(res, sum_x, sum_y, sum_xy, sum_re_xy)

print(res)