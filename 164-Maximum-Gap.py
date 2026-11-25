from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort() # 排序
        ans=0
        for i in range(1,n):
            ans=max(ans,abs(nums[i]-nums[i-1])) # 计算最大差值
        return ans
