class Solution:
    def restoreIpAddresses(self, s: str):
        ans = []
        path = []
        self.dfs(s,path,ans)
        return ans
    def dfs(self,s,path,ans):
        if len(path) == 4:
           if not s:
              ans.append(path[:])
           return

        for i in range(3):
            if i != 0 and s[0] == '0':
               break
            if i > len(s):
               break
            if 0 <= int(s[:i+1]) <= 255:
               self.dfs(s[i+1:],path+[s[:i+1]],ans)