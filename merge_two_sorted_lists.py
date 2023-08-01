# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2;
        if not list2:
            return list1
        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val > ptr2.val:
                temp = ptr2.next
                temp1 = ptr1.next
                ptr1.val, ptr2.val = ptr2.val, ptr1.val
                ptr1.next = ptr2
                ptr2.next = temp1
                ptr1 = ptr2
                ptr2 = temp

            elif ptr1.next == None:
                break
            else:
                ptr1 = ptr1.next

        if ptr2:
            ptr1.next = ptr2

        return list1

