'''nums = [1,5,11,5]'''
class solution:
      def process(self,nums):
          sums = sum(nums)
          if sums % 2:
             return False
          avg = sums // 2
          dp = [0] * (avg+1)
          dp[0] = 1
          for num in nums:
              for j in range(avg,num - 1, -1):
                  dp[j] = dp[j] or dp[j-num]
          return dp[-1]
