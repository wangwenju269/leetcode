'''
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
'''
'''
解题方法：数组映射的方法
'''
from collections import Counter
class solution:
      def process(self,s,p):
          s_len, p_len = len(s), len(p)
          dp_s = [0] * 26
          dp_p = [0] * 26
          ans = []
          if s_len < p_len:
             return []
          for i in range(p_len):
              dp_p[ord(p[i])- ord('a')] += 1
              dp_s[ord(s[i]) - ord('a')] += 1
          if dp_s == dp_p:
             ans.append(0)
          for i in range(s_len-p_len):
              dp_s[ord(s[i]) - ord('a')] -= 1
              dp_s[ord(s[i+p_len]) - ord('a')] += 1
              if dp_s == dp_p:
                 ans.append(i+1)
          return ans
s = "cbaebabacd"
p = "abc"
print(solution().process(s,p))