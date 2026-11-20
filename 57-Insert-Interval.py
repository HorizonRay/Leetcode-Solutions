from typing import List
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #分三步走
        i,n=0,len(intervals)
        ans=[]
        start,end=newInterval # 新区间的两个端点
        while i<n and intervals[i][1]<start: # 当前区间的右端点比新区间的左端点要小 说明没有重叠或者连接 直到找到当前区间的右端点比新区间的左端点要大于或者等于
            ans.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=end: # 当前区间的左端点比新区间的右端点要小于或者等于
            start=min(start,intervals[i][0]) # 第一次循环就可以确定左端点
            end=max(end,intervals[i][1]) # 每次循环都在扩展右端点
            i+=1
        ans.append([start,end]) # 确定重叠区间的左右端点
        while i<n: # 将剩余区间添加到答案中
            ans.append(intervals[i])
            i+=1
        return ans
