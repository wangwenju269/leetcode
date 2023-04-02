class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        ans = float('inf')
        sums = 0
        l = 0
        for r in range(n):
            sums += nums[r]
            while sums >= target:
                  sums -= nums[l]
                  ans = min(ans, r - l + 1)
                  l += 1
        return 0 if ans == float('inf') else ans
print(Solution().minSubArrayLen(11,[1,2,3,4,5]))

