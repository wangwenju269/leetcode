'num = "1432219", k = 3'
class solution :
      def process(self,nums,k):
          monostack = []
          for str in nums :
              while monostack and k and str < monostack[-1]:
                    monostack.pop()
                    k -= 1
              monostack.append(str)
          '可能是升序排列，及k值存在现象'
          monostack = monostack[:-k] if k else monostack
          return ''.join(monostack).lstrip('0') or '0'
num = "1432219"
k = 3
print(solution().process(num,k))