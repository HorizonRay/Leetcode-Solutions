from typing import List
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        if n==0:
            return []
        elif n==1:
            return intervals
        # 如果第一个元素相等 Python的sort是稳定排序 会保持它们在原列表中的相对顺序 不会自动再按第二个元素排序
        intervals.sort(key=lambda x:x[0]) # 根据第一个元素大小进行升序排序 可以找到重叠区间
        ans=[]
        ans.append(intervals[0]) # 第一个区间添加到答案中作为基准判断
        for i in range(1,n):
            last_interval=ans[-1] # 上一个未重叠区间
            current_interval=intervals[i] # 当前区间
            if last_interval[1]>=current_interval[0]: # 区间重叠(端点相连的时候也可以连在一起)
                last_interval[1]=max(last_interval[1],current_interval[1]) # 扩展上一个区间的右端
            else: # 区间不重叠
                ans.append(intervals[i]) # 直接添加到答案中
        return ans
