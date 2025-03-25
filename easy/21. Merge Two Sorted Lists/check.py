# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    cur = res
    if not list1 and not list2:
        return None

    while True:
        show_list(res.next)

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
            while list1:
                node = ListNode(list1.val)
                cur.next = node
                cur, list1 = cur.next, list1.next
        elif first_val is None:
            while list2:
                node = ListNode(list2.val)
                cur.next = node
                cur, list2 = cur.next, list2.next
        else:
            break
    
    

    return res.next

def create_list(l):
    res = ListNode()
    cur = res
    for a in l:
        cur.next = ListNode(a)
        cur = cur.next
    return res.next

def show_list(l: ListNode):
    cur = l
    print('[', end='')
    while cur:
        if not cur.next:
            print(cur.val, end='')
            break
        else:
            print(cur.val, end=', ')
        cur = cur.next
    print(']')


if __name__ == '__main__':

    check_1 = [1, 2, 4], [1, 2, 3]
    check_2 = [], [0]
    check = [-10,-9,-6,-4,1,9,9], [-5,-3,0,7,8,8]

    list1 = create_list(check[0])
    list2 = create_list(check[1])


    show_list(list1)
    show_list(list2)
    
    res = mergeTwoLists(list1, list2)

    show_list(res)

