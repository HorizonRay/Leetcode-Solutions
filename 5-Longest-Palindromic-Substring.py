class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 核心:遍历每个值 并且以每个值为中心向两边遍历寻找答案
        def compare(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        if len(s)<=1:
            return s
        longest=''
        for i in range(len(s)):
            odd=compare(i,i)
            even=compare(i,i+1)
            if len(odd)>=len(longest):
                longest=odd
            if len(even)>=len(longest):
                longest=even
        return longest
