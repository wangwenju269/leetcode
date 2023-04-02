'''
输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
'''
class solution:
      def process(self,nums):
          nums.sort()
          ans = []
          path = []
          self.dfs(nums,path,ans)
          return ans
      def dfs(self,nums,path,ans):
          if len(path) >= 2:
             ans.append(path[:])
          if not nums:
             return
          for i in range(len(nums)):
              if i != 0 and nums[i] == nums[i-1]:
                 continue
              if not path or nums[i] >= path[-1]:
                 self.dfs(nums[i+1:],path+[nums[i]],ans)
nums = [4,6,7,7]
print(solution().process(nums))