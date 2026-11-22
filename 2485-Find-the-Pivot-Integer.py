class Solution:
    def pivotInteger(self, n: int) -> int:
        mid_num=n//2
        sum_first=(1+mid_num)*mid_num//2
        sum_latter=(mid_num+n)*(n-mid_num+1)//2 # 注意:左右两个和都包括中枢整数
        for num in range(mid_num+1,n+1):
            sum_first+=num # 左边和添加当前数字
            sum_latter-=(num-1) # 右边和减去前一个数字
            if sum_first==sum_latter:
                return num
        return -1
