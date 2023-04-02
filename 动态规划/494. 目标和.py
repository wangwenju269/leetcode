'nums = [1,1,1,1,1], target = 3'
class solution:
      def process(self,nums,target):
          sums = sum(nums)
          if (sums+target) % 2 or sums < abs(target):
              return False
          avg = (sums+target) // 2
          dp = [0] * (avg+1)
          dp[0] = 1
          for num in nums:
              for j in range(avg,num-1,-1):
                  dp[j] += dp[j-num]
          return dp[-1]