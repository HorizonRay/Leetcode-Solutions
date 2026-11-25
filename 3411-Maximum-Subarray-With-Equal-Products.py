from typing import List
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # 滑动窗口
        import math
        ans=2
        product=1
        left=0
        for right,num in enumerate(nums):
            # 核心:当最大公约数为1的时候 乘积和当前元素两两互质 所以最小公倍数就是指针范围内的全部元素的乘积 所以prod == gcd × lcm
            while math.gcd(product,num)>1:
                product//=nums[left]
                left+=1
            product*=num
            ans=max(ans,right-left+1)
        return ans
