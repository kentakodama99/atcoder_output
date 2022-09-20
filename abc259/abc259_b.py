import math
import sys

a, b, d = list(map(int, input().split()))

if a == 0 and b == 0:
    print("0.00000000000000000000 0.00000000000000000000")
    sys.exit()
elif d ==360:
    print(f"{a} {b}")
    sys.exit()
rad_d = math.radians(d)

x = a * math.cos(rad_d) - b * math.sin(rad_d)
y = a * math.sin(rad_d) + b * math.cos(rad_d)

print(f"{x:.20f} {y:.20f}")