'''
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
'''
class solution:
      def process(self,candidates,target):
          candidates.sort()
          ans = []
          path = []
          self.dfs(candidates,target,path,ans,0)
          return ans
      def dfs(self,candidates,target,path,ans,i):
          if target < 0:
             return
          if target == 0:
             ans.append(path[:])
             return
          for i in range(i, len(candidates)):
              if i > 0 and candidates[i] == candidates[i-1]:
                 continue
              self.dfs(candidates,target - candidates[i], path+[candidates[i]],ans,i)

candidates = [2,3,6,7]
target = 7
print(solution().process(candidates,target))