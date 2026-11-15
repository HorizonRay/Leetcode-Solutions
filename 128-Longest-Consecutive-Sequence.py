from typing import List
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 核心:题目要求的序列不需要连续也不需要维护相对顺序 所以可以升序排序
        nums.sort()
        n=len(nums)
        ans=length=1 # 只要列表不为空 答案至少是1
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                length+=1
            elif nums[i]!=nums[i-1]: # 题目要求相邻元素如果相等长度不变 所以直接判断不相等的时候就重置1
                length=1
            ans=max(ans,length)
        return ans if n>0 else 0 # 列表如果为空就返回0
