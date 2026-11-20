from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 即兴发挥
        if not nums:
            return 0
        tran=[[],[],[]]
        for i in nums:
            if i%3==0:
                tran[0].append(i)
            elif i%3==1:
                tran[1].append(i)
            else:
                tran[2].append(i)
        total=sum(nums)
        tran[1].sort(reverse=True)
        tran[2].sort(reverse=True)
        if total%3==0:
            return total
        elif len(nums)==1:
            return 0
        if not tran[0] and not tran[1]:
            if total%3==1:
                total-=(tran[2].pop()+tran[2].pop())
            else:
                total-=tran[2].pop()
            return total
        elif not tran[0] and not tran[2]:
            if total%3==1:
                total-=tran[1].pop()
            else:
                total-=(tran[1].pop()+tran[1].pop())
            return total
        if not tran[1]:
            if total%3==1:
                total-=(tran[2].pop()+tran[2].pop())
            else:
                total-=tran[2].pop()
            return total
        elif not tran[2]:
            if total%3==1:
                total-=tran[1].pop()
            else:
                total-=(tran[1].pop()+tran[1].pop())
            return total
        elif not tran[0]:
            if len(tran[1])==1:
                if total%3==1:
                    if tran[1][-1]<tran[2][-1] or (tran[1][-1]>tran[2][-1] and tran[1][-1]<tran[2][-2]):
                        total-=tran[1][-1]
                    else:
                        total-=(tran[2].pop()+tran[2].pop())
                    return total
                elif total%3==2:
                    total-=tran[2].pop()
                    return total
            elif len(tran[2])==1:
                if total%3==2:
                    if (tran[2][-1]<tran[1][-1]) or (tran[2][-1]<tran[1][-2] and tran[2][-1]>tran[1][-1]):
                        total-=tran[2][-1]
                    else:
                        total-=(tran[1].pop()+tran[1].pop())
                    return total
                elif total%3==1:
                    total-=tran[1].pop()
                    return total
            else:
                if total%3==1:
                    if tran[1][-1]<=tran[2][-1]+tran[2][-2]:
                        total-=tran[1].pop()
                    else:
                        total-=(tran[2].pop()+tran[2].pop())
                    return total
                elif total%3==2:
                    if tran[2][-1]<=tran[1][-1]+tran[1][-2]:
                        total-=tran[2].pop()
                    else:
                        total-=(tran[1].pop()+tran[1].pop())
                    return total

        if len(tran[1])==1:
            if total%3==1:
                if tran[1][-1]<tran[2][-1] or (tran[1][-1]>tran[2][-1] and tran[1][-1]<tran[2][-2]):
                    total-=tran[1][-1]
                else:
                    total-=(tran[2].pop()+tran[2].pop())
                return total
            elif total%3==2:
                total-=tran[2].pop()
                return total
        elif len(tran[2])==1:
            if total%3==2:
                if (tran[2][-1]<tran[1][-1]) or (tran[2][-1]<tran[1][-2] and tran[2][-1]>tran[1][-1]):
                    total-=tran[2][-1]
                else:
                    total-=(tran[1].pop()+tran[1].pop())
                return total
            elif total%3==1:
                total-=tran[1].pop()
                return total

        if total%3==1:
            if tran[1][-1]<=tran[2][-1]+tran[2][-2]:
                total-=tran[1].pop()
            else:
                total-=(tran[2].pop()+tran[2].pop())
            return total
        elif total%3==2:
            if tran[2][-1]<=tran[1][-1]+tran[1][-2]:
                total-=tran[2].pop()
            else:
                total-=(tran[1].pop()+tran[1].pop())
            return total
        return 0
