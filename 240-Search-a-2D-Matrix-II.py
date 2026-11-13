from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 核心:从右到左搜索 从上到下搜索:从右上角开始搜索
        m,n=len(matrix),len(matrix[0])
        row,col=0,n-1
        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target: # 数值过大 需要向左移动减小数值
                col-=1
            else: # 数值过小 需要向下移动增大数值
                row+=1
        return False
