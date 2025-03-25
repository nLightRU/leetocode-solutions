"""
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

tests
[1, 2, 4], [1, 3, 4]
[], [0]
[], []
[-10,-9,-6,-4,1,9,9], [-5,-3,0,7,8,8]

"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        if not list1 and not list2:
            return None

        while True:
            first_val = list1.val if list1 else None
            second_val = list2.val if list2 else None

            if (first_val is None) and (second_val is None):
                break
            
            if not (first_val is None) and not (second_val is None):
                if first_val == second_val:
                    node = ListNode(first_val, ListNode(second_val))
                    cur.next = node
                    cur = cur.next.next
                    list1, list2 = list1.next, list2.next
                elif first_val < second_val:
                    node = ListNode(first_val)
                    cur.next = node
                    cur, list1 = cur.next, list1.next
                else:
                    node = ListNode(second_val)
                    cur.next = node
                    cur, list2 = cur.next, list2.next         
            elif second_val is None:
                node = ListNode(first_val)
                cur.next = node
                cur, list1 = cur.next, list1.next
                while list1:
                    node = ListNode(list1.val)
                    cur.next = node
                    cur, list1 = cur.next, list1.next
            elif first_val is None:
                node = ListNode(second_val)
                cur.next = node
                cur, list2 = cur.next, list2.next
                while list2:
                    node = ListNode(list2.val)
                    cur.next = node
                    cur, list2 = cur.next, list2.next
            


        return res.next