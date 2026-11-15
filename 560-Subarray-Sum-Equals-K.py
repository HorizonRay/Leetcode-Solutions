from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 核心:前缀和+哈希表
        freq={0:1} # 当前缀和为0的时候算一个
        sums=ans=0
        for num in nums:
            sums+=num
            if sums-k in freq:
                ans+=freq[sums-k]
            if sums in freq:
                freq[sums]+=1
            else:
                freq[sums]=1
        return ans
