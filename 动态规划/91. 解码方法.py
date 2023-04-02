'''
输入：s = "226"
输出：3
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        '''初始化：空字符串只有一种解码方法
                   一个字符只有一种解码方法 
        '''
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(1,n):
            if s[i] != '0':
               dp[i+1] += dp[i]
            if 10 <= int(s[i-1:i+1]) <= 26:
               dp[i+1] += dp[i-1]
        return dp[-1]
'''
输入：s = "226"
输出：[bbf,vf]
'''
class solution:
      def process(self,s):
          dict_map = {i+1:chr(i+ ord('a')) for i in range(26)}
          ans = []
          path = []
          self.dfs(s,ans,path,dict_map)
          return ans
      def dfs(self,s,ans,path,dict_map):
          if not s :
             ans.append(''.join(path[:]))
             return
          for i in range(2):
              if i >= len(s) or int(s[:i+1]) == 0:
                 break
              if 1 <= int(s[:i+1]) <= 26 :
                 self.dfs(s[i+1:],ans,path+[dict_map[int(s[:i+1])]], dict_map)

s = "105362"
print(solution().process(s))



