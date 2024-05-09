"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""


class MinStack:
    def __init__(self) -> None:
        self.stack = [] # blue - stack[-1] will always have the top element
        self.min_stack = [] # green - min_stack[-1] will always have the minimum value
        
    def push(self, val) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
    
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1
        
    
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(-3)
    minStack.push(0) # -2, -3, 0
    print("min", minStack.getMin())
    minStack.pop() # -2, -3
    print("top", minStack.top())
    minStack.push(10) # -2, -3, 10
    print("min", minStack.getMin())
    print("top", minStack.top())