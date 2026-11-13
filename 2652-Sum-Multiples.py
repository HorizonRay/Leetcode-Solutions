from typing import List
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # 求 1 ~ n 中所有 k 的倍数之和
        def choose(k):
            count=n//k
            # 计算公式:(首项+末项)*项数//2 首项为k 末项为count*k 项数为count
            return (count+1)*k*count//2
        # 利用容斥原理:A∪B∪C=A+B+C-A∩B-A∩C-B∩C+A∩B∩C
        return choose(3)+choose(5)+choose(7)-choose(15)-choose(21)-choose(35)+choose(105)
