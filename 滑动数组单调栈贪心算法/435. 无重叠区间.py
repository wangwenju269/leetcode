'''
'给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
返回 需要移除区间的最小数量，使剩余区间互不重叠 。
'''
class solution:
      def process(self,intervals):
          intervals.sort(key = lambda x:x[1])
          n = len(intervals)
          rightpoint = intervals[0][1]
          ans = [intervals[0]]
          for i in range(n):
              if intervals[i][0] >= rightpoint:
                 ans.append(intervals[i])
                 rightpoint = intervals[i][1]
          return ans

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        rightpoint = intervals[0][1]
        count = 1
        for left, right in intervals:
            if left >= rightpoint:
               count += 1
               rightpoint = right
        return n - count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(solution().process(intervals))