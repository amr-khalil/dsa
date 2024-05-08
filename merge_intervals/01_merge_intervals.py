"""
56. Merge Intervals
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

def merge(intervals):
    """
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    intervals.sort(key=lambda x:x[0])
    ans = [intervals[0]]
    for interval in intervals:
        a1, a2 = ans[-1]
        b1, b2 = interval
        if a2 < b1:
            ans.append(interval)
        else:
            ans[-1][1] = max(a2, b2)
    return ans
    
if __name__ == '__main__':
    intervals = [[1,4],[4,5]]
    print(merge(intervals)) # [[1,5]]
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals)) # [[1,6],[8,10],[15,18]]
     