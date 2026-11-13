from typing import List
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n=len(arr)
        if n<3:
            return 0
        ans=0
        # 思路:从第二个元素遍历到倒数第二个元素 当当前元素大于左右相邻的两个元素的时候 分别检查左右两个元素分别向两边符合条件地扩展能到达的边界 即此次循环左右指针的边界 然后计算长度 更新答案
        for i in range(1,n-1):
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                left,right=i-1,i+1
                while left>0 and arr[left]>arr[left-1]:
                    left-=1
                while right<n-1 and arr[right]>arr[right+1]:
                    right+=1
                ans=max(ans,right-left+1)
        return ans
