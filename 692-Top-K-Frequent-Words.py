from typing import List
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        from collections import Counter
        import heapq
        freq=Counter(words)
        heap=[]
        for word,cnt in freq.items():
            heapq.heappush(heap,(-cnt,word)) # 频率用负数模仿大根堆 之后弹出来的时候就是最大频率的元素
        ans=[]
        while heap and k>0:
            ans.append(heapq.heappop(heap)[1]) # 核心:题目要求单词排序按照频率从高到低排序 符合堆的性质 如果频率相同 堆也根据字典序从小到大排序了
            k-=1
        return ans
