from typing import List
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # 核心:哈希表单遍计数 + 在线检查相邻值
        freq={}
        ans=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            # 只要当前的数字和相邻的数字都存在 就说明符合条件 且子序列只要求相对顺序不变可以不用连续 所以直接加频率
            if num+1 in freq:
                ans=max(ans,freq[num]+freq[num+1])
            if num-1 in freq:
                ans=max(ans,freq[num]+freq[num-1])
        return ans
