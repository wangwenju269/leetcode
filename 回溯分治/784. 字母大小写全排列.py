'''
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]
'''
class solution:
      def process(self,s):
          ans = []
          path = []
          self.dfs(s,path,ans,0)
          return ans
      def dfs(self,s,path,ans,i):
          if i == len(s):
             ans.append(path[:])
             return
          if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
              self.dfs(s,path+s[i].lower(),ans,i+1)
              self.dfs(s,path+s[i].upper(),ans,i+1)
          else:
              self.dfs(s,path+s[i],ans,i+1)