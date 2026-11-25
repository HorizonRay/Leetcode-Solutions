from typing import List
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(1,n-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]: # 找到就返回答案
                return nums[i]
        if n==1: # 长度为1
            return nums[0]
        if nums[0]!=nums[1]: # 最左侧元素
            return nums[0]
        elif nums[-1]!=nums[-2]: # 最右侧元素
            return nums[-1]
