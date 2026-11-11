from typing import List
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # 通过将数组升序排序 利用索引找到当前对应的最大值和最小值 然后将平均值添加到答案数组中 最后返回最小值
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n//2):
            ans.append((nums[i]+nums[n-1-i])/2)
        return min(ans)
