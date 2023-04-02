'''
713. 乘积小于 K 的子数组
nums = [10,5,2,6], k = 100
'''
nums = [1,2,3]
k = 0
class solution:
      def process(self,nums,k):
          n = len(nums)
          l = 0
          temp = 1
          count = 0
          for r in range(n):
              temp *= nums[r]
              while  temp >= k and l <= r :
                    temp /= nums[l]
                    l += 1
              count += (r-l+1)
          return count
print(solution().process(nums,k))


