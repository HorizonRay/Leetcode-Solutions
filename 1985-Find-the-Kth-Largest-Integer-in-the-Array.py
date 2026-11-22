from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # 核心:堆
        import heapq
        heap=[]
        for num in nums:
            num=int(num) # 不能直接添加字符串 因为堆会比较字典序 但是字符串长度可能不一样 会比较错误
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return str(heap[0])
