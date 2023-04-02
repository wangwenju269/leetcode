'''
输入：nums = [1,2,4,8]
输出：[1,2,4,8]
'''
class solution:
      def process(self,nums):
          amax_i = 0
          num_max = 0
          n = len(nums)
          dp = [0] * n
          for i in range(n):
              for j in range(i):
                  if nums[i] % nums[j] == 0:
                     dp[i] = max(dp[i],dp[j] + 1)
                     if dp[i] > amax_i:
                        amax_i = dp[i]
                        num_max = nums[i]
          print(dp)
          ans = []
          for i in range(n-1,-1,-1):
              if num_max % nums[i] == 0 and dp[i] == amax_i:
                 ans.append(nums[i])
                 amax_i -= 1
                 num_max = nums[i]
          return ans[::-1]
nums = [1,2,6,9]
print(solution().process(nums))
