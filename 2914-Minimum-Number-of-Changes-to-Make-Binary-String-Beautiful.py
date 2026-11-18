class Solution:
    def minChanges(self, s: str) -> int:
        # 因为要获得尽可能多的偶数个子字符串 所以两两配对
        ans=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                ans+=1
        return ans
