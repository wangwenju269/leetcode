'''
price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
输出：14
'''
class solution:
      def __init__(self):
          self.cost = 0
      def process(self,price, special, need):
          for i in range(len(price)):
              self.cost += need[i] * price[i]
          '''
          对special的集合做过滤
          过滤条件1：
                 大礼包总和 < 单个买的结果
                 大礼包要有数量
          '''
          special = [sp for sp in special   \
                     if (sum(sp[:-1]) > 0 and sum([sp * p for sp, p in zip(sp[:-1], price)]) > sp[-1])]
          money = 0
          self.dfs(price,special,need, money)
          return self.cost

      def dfs(self,price,special,need ,money):
          if min(need) < 0:
             return
          if self.cost > money + sum(map(lambda x: x[0] * x[1] ,zip(need,price))):
             self.cost =   money + sum(map(lambda x: x[0] * x[1] ,zip(need,price)))
          for i in range(len(special)):
              self.dfs(price,special,list(map(lambda x: x[0] - x[1],zip(need,special[i][:-1]))), \
              money + special[i][-1])

price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(solution().process(price,special,needs))