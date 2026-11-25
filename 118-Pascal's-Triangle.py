class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 核心:动态规划
        dp=[[1]*(i+1) for i in range(numRows)] # 创建金字塔型数组
        for i in range(2,numRows): # 从第三行开始 因为前两行都是1
            for j in range(1,i): # 从每行的第二个数开始到倒数第二个数结束 因为两边都是1
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        return dp
