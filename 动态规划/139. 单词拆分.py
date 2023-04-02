's = "leetcode", wordDict = ["leet", "code"]'
'''
定义： dp[i] 表示前i个字符能在worddict中找到
状态转移方程：dp[j] = dp[i] and s[i:j] in worddict      
'''
def process(s,wordDict):
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n):
        for j in range(i+1,n+1):
            if dp[i] and s[i:j] in wordDict:
               dp[j] = 1
    return dp[-1]           