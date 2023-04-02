'''
nums = [1,-2,3,-2]
输出：3
'''
class solution:
      def process(self,nums):
          n = len(nums)
          dp_max = [0] * n
          dp_min = [0] * n
          dp_max[0] , dp_min[0] = nums[0] ,nums[0]
          for i in range(1,n):
              dp_max[i] = max(dp_max[i-1]+nums[i] , nums[i])
              dp_min[i] = min(dp_min[i-1]+nums[i],nums[i])
          ans = max(max(dp_max), sum(nums) - min(dp_min))
          if ans == 0:
              return max(nums)
          return ans
nums = [-3,-2,-3]
print(solution().process(nums))
