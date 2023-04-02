'''子数组最小和'''
arr = [11,81,94,43,3]
'''
11
81,81
94,94,94
94,94,94,43
94,94,94,3,3
'''
class solution :
      def process(self,arr):
          n = len(arr)
          dp = [0] * n
          monostack = []
          for i in range(n):
              while  monostack and arr[monostack[-1]] > arr[i]:
                     monostack.pop()
              if monostack:
                 dp[i] = (i - monostack[-1]) * arr[i] + dp[monostack[-1]]
              else:
                 dp[i] = (i+1)*arr[i]
              monostack.append(i)
          return sum(dp)

arr = [11,81,94,43,3]
print(solution().process(arr))