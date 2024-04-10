"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Hint 1
How about using a data structure such as deque (double-ended queue)?

Hint 2
The queue size need not be the same as the window’s size.

Hint 3
Remove redundant elements and the queue should store only elements that need to be considered.
"""
import random

def maxSlidingWindowNaive(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    Time complexity: O(n)
    Space complexity: O(n)
    """
    ans = []
    for i in range(len(nums)-k+1):
        subarray = nums[i:i+k]
        ans.append(max(subarray))
    return ans

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    use deque to store the index of the elements in the window
    """
    from collections import deque
    ans = []
    q = deque()
    for i in range(len(nums)):
        # remove the first element from the deque if it is out of the window
        if q and q[0] == i - k:
            q.popleft()
        # remove the elements from the deque that are smaller than the current element
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        # add the maximum element to the result
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans

if __name__ == '__main__':
    # Test case 1
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums, k)) # Output: [3,3,5,5,6,7]

    # Test case 2
    nums = [1]
    k = 1
    print(maxSlidingWindow(nums, k)) # Output: [1]
    
    # Test case 3
    nums = range(1, 10**5)
    k = 50000
    # print(maxSlidingWindow(nums, k))