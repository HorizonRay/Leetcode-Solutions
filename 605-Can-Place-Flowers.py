from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0] # 左右两边也是没有花的
        length=len(flowerbed)
        for i in range(1,length-1):
            if n==0: # 先判断是否能够弹出 防止出现n=0还继续循环的情况
                break
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        return n==0
