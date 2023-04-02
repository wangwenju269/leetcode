'''arr = [1,2,3,4,5,6,7,8]
return 5
状态转移方程：
   设：i > j > k
   if arr[i] = arr[j] + arr[k]
      dp[j][i] = dp[k][j] + 1
   剪枝操作：
      arr[i] > arr[j] > arr[k] = arr[i] - arr[j]
      推出：arr[i] < 2* arr[j]

'''
class solution:
      def process(self,arr):
          n = len(arr)
          dict_maps = {x:i for i,x in enumerate(arr)}
          dp = [[0] * n for _ in range(n)]
          amax = 0
          for i in range(2,n):  # i 遍历最小元素是从第3个位置开始的
              for j in range(i):
                  if  2 * arr[j] <= arr[i] :
                      continue
                  temp = arr[i] - arr[j]
                  if temp in dict_maps.keys():
                     k = dict_maps[temp]
                     dp[j][i] = max(dp[k][j] + 1,3)
                     if dp[j][i] > amax:
                        amax = dp[j][i]
          return amax
