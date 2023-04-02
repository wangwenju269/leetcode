'''p = "zab"
return 6'''
class solution:
      def process(self,p):
          dp = [0] * 26
          n = len(p)
          dp[ord(p[0])- ord('a')] += 1
          k = 1
          for i in range(1,n):
              if (ord(p[i])- ord(p[i-1])) % 26  == 1:
                 k += 1
                 dp[ord(p[i]) - ord('a')] = max(k, dp[ord(p[i]) - ord('a')])
              else:
                 k = 1
                 if dp[ord(p[i]) - ord('a')] == 0:
                    dp[ord(p[i]) - ord('a')] = 1

          return sum(dp)
