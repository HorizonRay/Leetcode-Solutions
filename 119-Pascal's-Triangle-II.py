class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # 核心:动态规划
        dp=[[1]*(i+1) for i in range(rowIndex+1)] # 题目的rowIndex指的是索引 所以创建数组得多一行
        for i in range(2,rowIndex+1): # 遍历同上 多一行
            for j in range(1,i):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp[rowIndex] # 正好对应
