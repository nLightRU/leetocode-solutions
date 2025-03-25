# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        cur = self
        s = ''
        while cur:
            s += f'{cur.val} -> '
            cur = cur.next
        s += 'None'
        return s

# в конце может быть 1
# в конце не может быть 0 (надо будет удалить последний элемент)
def create_list(l: list) -> ListNode:
    head = ListNode(l[0])
    head.next = ListNode()
    cur = head
    for val in l[1:]:
        cur.next = ListNode(val)
        cur.next.next = ListNode()
        cur = cur.next
    cur.next = None
    return head

def print_list(l: ListNode):
    cur = l 
    print('[', end='')
    while cur:
        print(str(cur.val) + ', ', end='')
        cur = cur.next
    print(']')

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s = (l1.val + l2.val) % 10
    remain = (l1.val + l2.val) // 10
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
        result_cur = result_cur.next
        if (not l1) and (not l2):
            if remain == 1:
                result_cur.val = 1
                result_cur.next = None
            else:
                result_cur = None
    
    return result_head

if __name__ == '__main__':
    l1 = create_list([9,9,9,9,9,9,9])
    l2 = create_list([9,9,9,9])
    res = addTwoNumbers(l1, l2)
    print_list(res)