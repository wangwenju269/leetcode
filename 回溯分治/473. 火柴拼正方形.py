'matchsticks = [1,1,2,2,2]'
class solution:
      def process(self,matchsticks):
          matchsticks.sort(reverse = True)
          n = len(matchsticks)
          sums = sum(matchsticks)
          if sums % 4 != 0:
             return False
          avg = sums // 4
          block = [0] * 4
          self.dfs(avg,block,matchsticks,0)
      def dfs(self,avg,block,matchsticks,i):
          if i == len(matchsticks):
             return all(map(lambda x:x==avg,block))
          for j in range(4):
              if block[j] + matchsticks[i] > avg:
                 continue
              block[j] += matchsticks[i]
              if self.dfs(avg,block,matchsticks,i+1):
                 return True
              block[j] -= matchsticks[i]
          return False