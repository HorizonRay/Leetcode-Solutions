from typing import List
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 核心:题目已经对列表非递减排列
        left=0
        for right in range(1,len(nums)): # 首个元素会重复 从第二个元素开始
            if nums[right]!=nums[left]:
                left+=1 # 先在原来的位置上 只有遇到不相等的情况下才到下一个位置然后赋值 防止因为先赋值后右移导致重复赋值
                nums[left]=nums[right]
        return left+1 # 索引比长度少1
