'''
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
'''
class solution:
      def process(self,stones):
          stones.sort()
          n = len(stones)
          sums = sum(stones)
          avg = sums // 2
          dp = [0] * (avg + 1)
          dp[0] = 1
          for stone in stones:
              for j in range(avg,stone-1,-1):
                  dp[j] = dp[j] or dp[j-stone]
          i = 0
          for i in range(avg,-1,-1):
              if dp[i]:
                  break
          return sums - 2 * i


