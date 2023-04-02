'''
 difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
'''
import bisect
class solution:
      def process(self,difficulty,profit,worker):
          difficulty,profit = zip(*sorted(zip(difficulty,profit)))
          difficulty = list(difficulty)
          profit = list(profit)
          for i in range(1,len(profit)):
              if profit[i] < profit[i-1]:
                 profit[i] = profit[i-1]
          worker.sort()
          ans = 0
          i = 0
          for work in worker:
              i = bisect.bisect_right(difficulty, work)
              if i != 0:
                  ans += profit[i - 1]
          return ans

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(solution().process(difficulty,profit,worker))