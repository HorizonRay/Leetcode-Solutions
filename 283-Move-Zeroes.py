from typing import List
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 一个0可能被交换不止一次
        left=0
        for right in range(len(nums)):
            if nums[right]!=0: # 当nums[right]不为0的时候 和左指针对应的0交换位置 
                if left!=right:
                    nums[left],nums[right]=nums[right],nums[left]
                left+=1 # 当nums[right]不为0的时候 两个指针是一起移动的 所以不会出现非零元素相对顺序改变的情况
                # 当nums[right]为0的时候 左指针不前进 等待右指针之后指向非零元素交换
