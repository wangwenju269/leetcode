'给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度'
'求解符合条件的连续子数组，滑动窗口解决，确定判断左指针移动的条件'
class Solution:
      def process(self,s):
          n = len(s)
          l,r = 0,0
          amax = 0
          stack = []
          while r < n:
                while s[r] in stack:
                      stack.remove(s[l])
                      l += 1
                stack.append(s[r])
                amax = max(amax,r-l+1)
          return amax    