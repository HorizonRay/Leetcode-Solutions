class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freqs=Counter(s) # 统计每种字符的频率
        idx={c:i for i,c in enumerate(s)} # 记录每种字符最后出现的索引
        n=len(s)
        ans=n
        for c,freq in freqs.items():
            if freq==1: # 当频率为1时 更新最小答案
                ans=min(ans,idx[c])
        return ans if ans<n else -1
