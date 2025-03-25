"""
2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
9 -> 2 -> 3
1 -> 2 -> None
0 -> 5 -> 3
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val + l2.val
        s, remain = s % 10, s // 10
        result_head = ListNode(s)
        result_cur = ListNode(0)
        result_head.next = result_cur
        l1 = l1.next
        l2 = l2.next 
        while l1 or l2:
            s = 0 + remain
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            remain = s // 10
            s = s % 10
            result_cur.val = s
            result_cur.next = ListNode(0)
            if (not l1) and (not l2):
                if remain == 1:
                    result_cur.next = ListNode(1)
                    return result_head
                else:
                    result_cur.next = None
                    return result_head
            result_cur = result_cur.next
    
        if remain == 1:
            result_head.next = ListNode(1)
        else:
            result_head.next = None
        return result_head
        