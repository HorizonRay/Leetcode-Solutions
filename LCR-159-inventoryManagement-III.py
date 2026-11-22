from typing import List
class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        # 核心:堆
        import heapq
        heapq.heapify(stock) # 堆化stock 堆顶都是目前最小的元素
        ans=[]
        while cnt>0: # 找到cnt个最小的元素
            ans.append(heapq.heappop(stock)) # 弹出当前最小元素 添加到答案中
            cnt-=1
        return ans
