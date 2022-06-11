from math import sqrt, ceil
def Eratosthenes(n : int) -> list:
    prime = [True] * (n + 1)
    prime[:2] = [False, False]
    for i in range(2, ceil(sqrt(n))):
        if prime[i]:
            for j in range(2 * i, n , i):
                prime[j] = False
    return prime

N = int(input())

is_prime = Eratosthenes(10 ** 6)
plist = []
for i in range(10 ** 6 + 1):
    if is_prime[i]:
        plist.append(i)
        
cnt = 0
for i in range(len(plist)):
    for j in range(i + 1, len(plist)):
        if plist[i] *(plist[j] ** 3) > N:
            break
        else:
            cnt += 1
print(cnt)