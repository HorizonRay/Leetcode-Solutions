class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 核心:栈
        stack=[]
        for c in s:
            if stack and stack[-1]==c:
                stack.pop() # 遇到相邻重复项就弹出删除
            else:
                stack.append(c) # 否则就添加
        return ''.join(stack)
