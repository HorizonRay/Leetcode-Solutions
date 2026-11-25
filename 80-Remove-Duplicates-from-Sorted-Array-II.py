from typing import List
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 原地修改(对比26题)
        n=len(nums)
        fast=slow=2
        while fast<n:
            if nums[slow-2]!=nums[fast]: # 因为是非递减顺序的数组 所以第前二个元素如果和快指针对应元素不一样 说明这个元素至多出现一次 所以可以赋值
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow
