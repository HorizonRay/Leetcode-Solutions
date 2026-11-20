class Solution:
    def reverse(self, x: int) -> int:
        str_x=str(abs(x))[::-1]
        if x>=0: # 注意正负号
            result=int(str_x)
        else:
            result=int(str_x)*(-1)
        if result<(-2)**31 or result>2**31-1:
            return 0
        return result
