import sys

N, X, Y = list(map(int, input().split()))

if N == 1:
    print(0)
    sys.exit()

def calc(level, is_red):
    if level == 1:
        return 0 if is_red else 1
    if is_red:
        return calc(level - 1, True) + calc(level, False) * X
    else:
        return calc(level - 1, True) + calc(level - 1, False) * Y

print(calc(N, True))

# N2 X3 Y4

# L1赤交換　+ L2青交換 * X (level - 1赤 + level青) (青交換を3回繰り返す)
# L1赤交換：return 0 (ストップ)
# L2青交換：L1赤交換 + L1青交換 * Y

# N3 X3 Y4
# L2赤交換　+ L3青交換 * X (青交換を3回繰り返す表現)
# **********
# L2赤交換
# ----------
# L1赤交換　+ L2青交換 * X (青交換を3回繰り返す表現)
# L1赤交換：return 0 (ストップ)
# L2青交換：L1赤交換 + L1青交換 * Y
# **********
# **********
# L3青交換
# ----------
# L2赤交換 + L2青交換 * Y(青交換をY回繰り返す表現)
# L2赤交換：上記
# L2青交換：L1赤交換 + L1青交換 * Y
# **********