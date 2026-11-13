from typing import List
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=1
        subs=word
        n=len(subs)
        while n*k<=len(sequence):
            # 因为k设定为1 所以每次循环开始最先检查当前的子串是否在sequence中 如果在就复制延长子串 否则说明当前子串不存在当中 所以不能算之前的最后一次延长 所以break后k要减1
            if sequence.find(subs)!=-1:
                subs+=word
                k+=1
            else:
                break
        return k-1
