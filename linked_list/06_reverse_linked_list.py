"""
206. Reverse Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # add prev and current nodes
    prev, current = None, head
    while current:
        # select the next node
        next_, current.next = current.next, prev
        # move
        prev, current = current, next_
        
    return prev

def reverseListRecursive(head):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not head or not head.next:
        return head
    reversed_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    reversed_head = reverseList(head)
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next # 5 4 3 2 1