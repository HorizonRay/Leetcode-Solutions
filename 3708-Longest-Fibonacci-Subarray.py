from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=mark=2
        for i in range(2,n):
            if nums[i]==nums[i-1]+nums[i-2]: # 符合条件就加1
                mark+=1
            else:
                mark=2 # 否则变回初始长度
            ans=max(ans,mark)
        return ans
