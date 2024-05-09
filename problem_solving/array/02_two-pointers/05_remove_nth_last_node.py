"""
19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # n = 2
    # 1 2 3 4 5
    #     l   r
    # two pointers
    fast = slow = head
    # offset fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
        
    # if only one item in list
    if not fast:
        return head.next
    
    # move fast and slow pointers
    while fast.next:
        fast = fast.next # move fast only one step
        slow = slow.next
    
    # delete
    slow.next = slow.next.next   
    
    return head
    
    
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    result = removeNthFromEnd(l1, 2)
    while result:
        print(result.val, end=" ")
        result = result.next
    


