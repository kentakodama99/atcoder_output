from math import gcd
def aseqSum(t):
    return (t * (t + 1)) // 2

N, A, B = map(int, input().split())
lcm = (A * B) // gcd(A, B) # a * b /最大公約数 = 最小公倍数
print(aseqSum(N) - ((A * aseqSum(N // A)) + (B * aseqSum(N // B)) - (lcm * aseqSum(N // lcm)) ) )