'''
intervals = [[1,3],[2,6],[8,10],[15,18]]
'''
'''
解题思想：
定义merged数组，
首先向merged数组中加入元素
每次更新merged数组最后元素的右侧位置取max
'''
class solution:
      def process(self,intervals):
          merged = []
          for interval in intervals:
              if not merged or merged[-1][1] < interval[0]:
                 merged.append(interval)
              else:
                 merged[-1][1] = max(merged[-1][1],interval[1])
          return merged
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution().process(intervals))