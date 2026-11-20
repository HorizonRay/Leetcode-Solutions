from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left,right=0,len(height)-1
        left_max=right_max=0
        water=0
        while left<right: #每一步都进行增加(使得每一步的水都能够进入计算)或者更新
            if height[left]<height[right]: #左边较小 先处理左边 因为右边更高 可以保证左边的水不会因为右边的高度更低而流出去
                if height[left]>=left_max: #当前最大值(包括相等)更新
                    left_max=height[left]
                else: # 只有降低的时候才能盛水
                    water+=(left_max-height[left])
                left+=1
            else: # 同上
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    water+=(right_max-height[right])
                right-=1
        return water
