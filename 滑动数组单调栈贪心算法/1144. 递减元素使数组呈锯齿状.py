'''
输入：nums = [1,2,3]
输出：2
'''
class solution:
      def process(self,nums):
          n = len(nums)
          ans = [0,0]
          for k in [0,1]:
              for i in range(k,n,2):
                  d = 0
                  if i > 0:
                     d = max(d, nums[i] - nums[i - 1] + 1)
                  if i + 1 < n:
                     d = max(d, nums[i] - nums[i + 1] + 1)
                  ans[k] += d
          return min(ans)
nums = [9,6,1,6,2]
print(solution().process(nums))