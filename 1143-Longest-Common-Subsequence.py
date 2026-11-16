class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 核心:动态规划
        m,n=len(text1),len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)] # 内外长度都多一个空间 是因为多出来的首个空间是初始元素 作为哨兵
        for i in range(1,m+1): # 因为初始空间是额外设定的 所以从第二个空间开始遍历
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]: # 相等的时候 两个字符配成一对 各去掉一个 落到左上角 再加1
                    dp[i][j]=dp[i-1][j-1]+1
                else: # 不相等的时候 选择竖直和水平两个方向上较大的
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
