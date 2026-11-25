from typing import List
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[1]*n # dp每个空间记录的是以当前元素结尾的最长严格递增子序列的长度
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]: # 严格递增
                    dp[i]=max(dp[i],dp[j]+1) # 因为是以当前元素结尾的 所以+1指的是加当前这个元素 所以j也不用遍历到i
        return max(dp)
