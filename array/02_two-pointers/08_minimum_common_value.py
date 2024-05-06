"""
2540. Minimum Common Value
Solved
Easy
Topics
Companies
Hint
Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
"""
def mostCommon(nums1, nums2):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    common = nums1.intersection(nums2)
    if common:
        return min(common)
    return -1


def mostCommonTwoPointers(nums1, nums2):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1

## binary search
def mostCommonBinarySearch(nums1, nums2):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def binarySearch(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    for num in nums1:
        if binarySearch(nums2, num):
            return num
    return -1


if __name__ == '__main__':
    print(mostCommon([1,2,3], [2,4])) # 2
    print(mostCommon([1,2,3,6], [2,3,4,5])) # 2
    print(mostCommon([1,2,3,6], [4,5])) # -1