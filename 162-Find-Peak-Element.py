from typing import List
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # 核心:二分算法
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if mid>=n-1 or nums[mid]>nums[mid+1]: # 前者防止越界 后者判断如果有下降趋势就往左移
                right=mid-1
            else:
                left=mid+1
        return left
