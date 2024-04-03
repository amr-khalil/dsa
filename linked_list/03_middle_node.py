"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode1(head):
    node = head
    length = 0

    while node:
        length += 1
        node = node.next

    mid = length // 2

    node = head
    for _ in range(mid):
        node = node.next
    return node.val
    
def middleNode2(head):
    """
    :type head: Node
    :rtype: int
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(middleNode1(head))
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(7)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(middleNode2(head))
    
    



