from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 核心:遇到1前缀和加1 遇到0前缀和减1 当当前前缀和存在于idx中的时候 说明中间这一段的前缀和为0 说明这一
        ans=prefix_sum=0
        # 当不确定位置的时候 可以通过记录索引来进行计算
        idx={0:-1} # 记录值相同的前缀和首次出现的时候的索引(前缀和一开始为0的时候记录-1作为哨兵方便计算)
        for i,num in enumerate(nums):
            if num==1:
                prefix_sum+=1
            else:
                prefix_sum-=1
            if prefix_sum in idx:
                ans=max(ans,i-idx[prefix_sum])
            if prefix_sum not in idx: # 之后不更新是因为索引越小 计算答案的差值越大 答案越大
                idx[prefix_sum]=i
        return ans
