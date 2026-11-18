from typing import List
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # 回溯法
        res,path=[],[] # subsets这个函数的局部变量 被内层函数backtrack闭包捕获 内层函数在修改这种变量不用nonlocal声明 且修改有效
        def backtrack(start):
            res.append(path[:]) # 递归开始就保存path当前副本
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
            # Python函数的基本行为:函数执行到函数体最后一行之后 会自动返回None 不需要显式写return
        backtrack(0)
        return res
