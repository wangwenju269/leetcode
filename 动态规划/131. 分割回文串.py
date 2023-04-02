
'将dp和dfs巧妙结合，难点在于解码方式dfs怎么做构造'
'''
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
'''
class Solution:
    def partition(self, s: str) :
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or dp[j+1][i-1]):
                   dp[j][i] = 1
        ans  = []
        path = []
        self.dfs(0,s,dp,path,ans)
        return ans
    def dfs(self,i,s,dp,path,ans):
        if i == len(s):
           ans.append(path[:])
           return
        for j in range(i,len(s)):
            if dp[i][j]:
               self.dfs(j+1,s,dp,path+[s[i:j+1]],ans)
s = "aab"
print(Solution().partition(s))