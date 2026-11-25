from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mark=[0]*101 # 可以使用空间记录频率
        for num in nums:
            mark[num]+=1
        max_freq=max(mark) # 找出最大频率
        ans=0
        for freq in mark:
            if freq==max_freq:
                ans+=freq
        return ans
