strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
class solution:
     def process(self,strs,m,n):
         dp = [[0]*(n+1) for _ in range(m+1)]
         for str1 in strs:
             x = str1.count('0')
             y = str1.count('1')
             for i in range(m,x-1,-1):
                 for j in range(n,y-1,-1):
                     dp[i][j] = max(dp[i][j], dp[i-x][j-y] + 1)
         return dp[-1][-1]