"""
881. Boats to Save People
Medium
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 
Constraints:
1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""

def numRescueBoats(people, limit):
    """
    Time complexity: O(nlogn)
    Space complexity: O(1)
    """
    people.sort()
    l, r = 0, len(people) - 1
    boats = 0
    while l <= r:
        # If the sum of the weights of the lightest and heaviest person is less than or equal to the limit
        if people[l] + people[r] <= limit:
            # Move the left pointer
            l += 1
        # Move the right pointer in any case as the heaviest person will be on the boat
        r -= 1
        # Increment the number of boats
        boats += 1
    return boats
    
if __name__ == '__main__':
    print(numRescueBoats([1,2], 3))  # 1
    print(numRescueBoats([3,2,2,1], 3))  # 3
    print(numRescueBoats([3,5,3,4], 5))  # 4