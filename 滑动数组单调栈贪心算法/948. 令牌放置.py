'''
tokens = [100,200,300,400], power = 200
'''
class solution:
      def process(self,tokens,power):
          tokens.sort()
          n = len(tokens)
          l,r = 0,n-1
          ans = 0
          '左右双指针算法，需要明白边界条件'
          while l <= r:
                while power - tokens[l] < 0 and ans > 0 :
                      power += tokens[r]
                      r -= 1
                      ans -= 1
                power -= tokens[l]
                ans += 1
                l += 1
          return ans
      
tokens = [100,200,300,400]
power = 200
print(solution().process(tokens,power))