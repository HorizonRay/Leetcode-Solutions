from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max_length=length=1 # 题目设定nums长度至少为1 所以答案至少为1
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]: # 符合严格递增的要求就加1
                length+=1
            else:
                length=1 # 否则重置为1
            max_length=max(max_length,length)
        return max_length
