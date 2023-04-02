'''
nums = [2,2,3,4]
输出: 3
'''
'解题思路：'
class solution:
      def process(self,nums):
          nums.sort()
          n = len(nums)
          count = 0
          for i in range(n-1,1,-1):
              l , r = 0 ,i-1
              while l < r:
                  if  nums[i] - nums[r] < nums[l]:
                      count += (r-l)
                      r -= 1
                  else:
                      l += 1
          return count
