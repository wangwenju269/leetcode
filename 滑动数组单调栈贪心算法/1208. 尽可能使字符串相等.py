'''
s = "abcd", t = "bcdf", maxCost = 3
'''
class solution:
      def process(self,s,t,maxCost):
          temp = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
          ans = 0
          l = 0
          for r in range(len(s)):
              maxCost -= temp[r]
              while maxCost < 0 :
                    maxCost += temp[l]
                    ans = max(ans, r - l )
                    l += 1
          return max(ans, r -l + 1)
s = "abcd"
t = "cdef"
maxCost = 1
print(solution().process(s,t,maxCost))
