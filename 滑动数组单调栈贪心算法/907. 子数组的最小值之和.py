'''
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
'''
'''
arr = [3,1,2,4]
'''
class solution:
      def process(self,arr):
          n  = len(arr)
          left = [0] * n
          right  = [0] * n
          monostack = []
          for i in range(n):
              while monostack and arr[i] <= arr[monostack[-1]]:
                    monostack.pop()
              left[i] = i - (monostack[-1] if monostack else -1)
              monostack.append(i)
          monostack = []
          for i in range(n-1,-1,-1):
              while monostack and arr[i] < arr[monostack[-1]]:
                    monostack.pop()
              right[i] = (monostack[-1] - i) if monostack else n - i
              monostack.append(i)
          ans = 0
          for i in range(n):
              ans += (arr[i] * left[i] * right[i])
          return ans








arr = [11,81,94,43,3]
print(solution().process(arr))