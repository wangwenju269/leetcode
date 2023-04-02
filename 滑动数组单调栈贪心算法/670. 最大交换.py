'''
'输入: 2736
输出: 7236'
解体思路：
从右侧向左遍历，找到最大的数字idx2，并找到最大数字最左端的数字idex1。
'''
class solution:
      def process(self,digit):
          nums = list(str(digit))
          n = len(nums)
          id_max = n-1
          id1,id2 = -1,-1
          for i in range(n-1,-1,-1):
              if nums[i] > nums[id_max]:
                  id_max = i
              elif nums[i] < nums[id_max]:
                  id1, id2 = i, id_max
              '相等的不做任何处理操作'
          if  id1 == -1:
              return digit
          nums[id1], nums[id2] = nums[id2], nums[id1]
          return int(''.join(nums))

