N,M,K = map(int, input().split())
 
total  = 0
 
dp = [ [0 for _ in range(K+1)] for _ in range(N+1)]
 
dp[0][0] = 1

for i in range(0,N):
    for j in range(0,K):
        for k in range(1,M+1):
            if j + k <= K:

                dp[i+1][j+k] += dp[i][j]

for j in range(1,K+1):
    total += dp[N][j] 

# print(dp)
print(total%998244353)