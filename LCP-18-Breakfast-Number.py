from typing import List
class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        # 核心:双指针
        staple.sort()
        drinks.sort()
        left,right=0,len(drinks)-1 # 左指针对应staple递增 右指针对应drinks递减
        ans=0
        while left<len(staple) and right>=0:
            if staple[left]+drinks[right]<=x:
                ans+=(right+1) # 当符合条件的时候 小于等于右指针的组合都是答案
                left+=1
            else:
                right-=1 # 不符合条件的时候 说明右指针对应的价格过大 要减小 右指针左移
        return ans%(10**9+7)
