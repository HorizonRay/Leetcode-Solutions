class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        from sortedcontainers import SortedDict
        freq1=Counter(nums) # 统计每个元素的频率
        freq2=SortedDict() # 这个有序字典的性质为按照键大小升序排序:键为频率 值为列表 其中包含各种频率相同的元素 
        for num,freq in freq1.items():
            if -freq in freq2:
                freq2[-freq].append(num) # 频率为负数 实现降序排序
            else:
                freq2[-freq]=[num]
        ans=[]
        for freq,bucket in freq2.items():
            if len(bucket)<=k:
                ans+=bucket # 延长答案列表
                k-=len(bucket)
            else:
                ans+=bucket[:k]
                break
        return ans
