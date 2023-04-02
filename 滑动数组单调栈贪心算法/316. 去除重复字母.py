'输入：s = "bcabc" 输出："abc"'
'需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）'
from collections import Counter
class solution:
      def process(self,s):
          counts = Counter(s)
          monostack = []
          n = len(s)
          for i in range(n):
              if s[i] not in monostack:
                  while monostack and s[i] < monostack[-1] and counts[monostack[-1]] >= 1:
                        monostack.pop()
                  monostack.append(s[i])
              counts[s[i]] -= 1
          return ''.join(monostack)

print(solution().process("bbcaac"))