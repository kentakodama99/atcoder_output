from collections import defaultdict
N = int(input())


memo = defaultdict(int)

def main(n):
    if n == 1:
        return "1"
    elif memo[n]:
        return memo[n]
    memo[n] = main(n - 1) + " " + str(n) + " " + main(n - 1)
    return memo[n]

print(main(N))