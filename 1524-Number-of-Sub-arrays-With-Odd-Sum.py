from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        #通过每次前缀和计数来记录出现了多少次奇数和偶数的前缀和
        #奇数=偶数－奇数=奇数－偶数
        prefix_sum=ans=0
        odd_count=0
        even_count=1 # 空前缀和为0 为偶数
        for num in arr:
            prefix_sum+=num
            if prefix_sum%2==1:
                # 前缀和为奇数的时候 检查之前有几个偶数前缀和 然后奇数-偶数=奇数 所以直接加偶数前缀和数量
                ans+=even_count
                odd_count+=1 # 算上本次前缀和
            else:
                # 前缀和为偶数的时候 检查之前有几个奇数前缀和 然后偶数-奇数=奇数 所以直接加奇数前缀和数量
                ans+=odd_count
                even_count+=1 # 算上本次前缀和
        return ans%(10**9+7)
