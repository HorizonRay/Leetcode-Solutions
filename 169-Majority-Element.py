from typing import List
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 当一个元素的个数超过整体个数的一半时 有序排列的列表正中间的那一个或者两个元素一定是这个元素
        return sorted(nums)[len(nums)//2]
