class Solution:
    def numSub(self, s: str) -> int:
        # 核心:字符都为1的子字符串的数目本质是(首项+末项)*项数/2
        MOD=10**9+7
        ans=count=0
        n=len(s)
        for i in range(n):
            if s[i]=='1':
                count+=1
            else:
                ans+=(1+count)*count//2
                count=0
        return (ans+(1+count)*count//2)%MOD # 最后还要计算剩余的count
