class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        n = len(A)
        l_temp = [0] * n
        for i in range(n-L+1):
            if i == 0:
               l_temp[i] = sum(A[:L])
            else:
               l_temp[i] = l_temp[i-1] - A[i-1] + A[i+L-1]
        m_temp = [0] * n
        for j in range(n-M+1):
            if j == 0:
               m_temp[j] = sum(A[:M])
            else:
               m_temp[j] = m_temp[j-1] - A[j-1] + A[j+M-1]
        print(l_temp)
        print(m_temp)
        res = 0
        for i in range(n - L + 1):
            for j in range(i+L,n-M+1):
                res = max(res,l_temp[i]+m_temp[j])
        for i in range(n -M + 1):
            for j in range(i+M,n-L+1):
                res = max(res,l_temp[j]+m_temp[i])
        return  res






A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2
print(Solution().maxSumTwoNoOverlap(A,L,M))