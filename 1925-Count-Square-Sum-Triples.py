class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        squares = {num ** 2 for num in range(1, n + 1)} # 记录所有范围内的平方和
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a ** 2 + b ** 2 in squares: # 只要在squares中 说明符合勾股定理
                    ans += 1
        return ans
