'贪心算法维护最远能到达的距离位置'
class Solution:
      def process(self,nums):
          n = len(nums)
          along = 0
          for i in range(n):
              if i > along:
                 return False
              along = max(along,i + nums[i])
          return True
      