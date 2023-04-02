'''
输入：values = [8,1,5,2,6]
输出：11
解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
'''
class solution:
     def process(self,values):
         n = len(values)
         amax = values[0] + 0
         res = 0
         for i in range(1,n):
             res = max(res,amax + values[i] - i)
             amax = max(amax,values[i] + i)
         return res
values = [8,1,5,2,6]
print(solution().process(values))