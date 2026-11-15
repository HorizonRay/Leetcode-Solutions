from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums) # nums有序
        for i in range(1,n-1):
            if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]: # 排序之后如果相邻元素都不等于当前元素 说明是答案
                return nums[i]
        return nums[0] if n==1 or nums[0]!=nums[1] else nums[-1] # 当数组长度为1或者开头元素和相邻元素不相等 说明开头元素为答案 否则是结尾元素
