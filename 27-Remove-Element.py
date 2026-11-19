from typing import List
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left=0
        for right in range(len(nums)):
            if nums[right]!=val: # 只要遇到的元素不是val 就赋值到前面 从而排列统一
                nums[left]=nums[right]
                left+=1
        return left # left在每次循环最后增加 代表实际长度
