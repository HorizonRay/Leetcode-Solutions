from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划:将列表想成一个金字塔形 从下往上:外层循环从倒数第二层开始 通过内层循环 在下一层的每个相邻两个数中选择较小的那个 累加上来 最终顶端元素就是答案
        for i in range(len(triangle)-2,-1,-1): # 原地修改
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
