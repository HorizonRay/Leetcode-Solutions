from typing import List
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 核心:动态规划
        n=len(nums)
        ans=[1]*n
        left_product=right_product=1
        for left in range(n): # 从左往右遍历 现将当前位置的答案乘以它左边元素的乘积
            ans[left]=left_product # 因为初始为1 所以直接用等号也行
            left_product*=nums[left] # 注意累乘
        for right in range(n-1,-1,-1): # 同上
            ans[right]*=right_product # 注意要写乘号
            right_product*=nums[right] # 注意累乘
        return ans
