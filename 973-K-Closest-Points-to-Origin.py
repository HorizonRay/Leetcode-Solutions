from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from collections import deque
        heap=[] # 使用小根堆 存储负数 数值越小 代表距离越短 距离原点越近
        for i,(x,y) in enumerate(points):
            heapq.heappush(heap,(-(x**2+y**2),i)) # 同时存储索引 代表答案位置
            if len(heap)>k:
                heapq.heappop(heap)
        dq=deque()
        ans=[]
        for _,idx in heap:
            ans.append(points[idx])
        return ans
