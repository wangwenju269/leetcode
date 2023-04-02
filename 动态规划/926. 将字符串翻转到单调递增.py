's = "00110"'
'''
  dp_0:字符 0 前面的相邻字符一定是 0，dp_1:字符 1 前面的相邻字符可以是 0 或 1
'''
class solution :
      def process(self,s):
          n = len(s)
          dp_0 = [0] * n        # 当前s[i]翻转为0，所需最小的操作数量.
          dp_1 = [0] * n        # 当前s[i]翻转为1，所需最小的操作数量.
          '''初始化操作'''
          if s[0] == '0':
             dp_1[0] = 1
          else:
             dp_0[0] = 1

          for i in range(1,n):
              if s[i] == '1':
                  dp_0[i] = dp_0[i - 1] + 1
                  dp_1[i] = min(dp_1[i - 1], dp_0[i - 1])
              else:
                  dp_0[i] = dp_0[i - 1]
                  dp_1[i] = min(dp_1[i - 1], dp_0[i - 1]) + 1
          return min(dp_1[-1],dp_0[-1])