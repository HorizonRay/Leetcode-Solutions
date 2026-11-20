from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans=0
        judge=float('-inf')
        intervals.sort(key=lambda x:x[1]) # 按照第二个元素的大小进行排序 可以防止出现区间覆盖的时候判断错误的情况
        for start,end in intervals:
            if start<judge: # 当前区间的左端如果比上一个区间的右端小 说明区间重叠 要移除 并且不用更新judge 因为这个区间被移除了
                ans+=1
            else: # 否则没有重叠 更新右端
                judge=end
        return ans
