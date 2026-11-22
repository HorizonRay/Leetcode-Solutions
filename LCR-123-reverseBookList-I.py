# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        # 核心:使用链表
        ans=[]
        current=head
        while current:
            ans.append(current.val)
            current=current.next # 让current这个指针/引用指向下一个节点
        return list(reversed(ans))
