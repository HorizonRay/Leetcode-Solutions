from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 核心:前缀和+哈希表
        freq={0:1} # 统计出现过的每个大小的前缀和的频率(当前缀和为0的时候算一个)
        sums=ans=0
        for num in nums:
            sums+=num
            if sums-k in freq: # 如果差值 即之前的一段前缀和存在于哈希表中 说明中间有和为k的子数组 个数为哈希表中那一段前缀和的频率
                ans+=freq[sums-k]
            if sums in freq: # 存储当前前缀和
                freq[sums]+=1
            else:
                freq[sums]=1
        return ans
