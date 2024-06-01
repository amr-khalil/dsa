"""
207. Course Schedule
Solved
Medium

Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Time complexity: O(V + E), because we visit each node once and each edge once
    Space complexity: O(V + E), because we store the graph as an adjacency list
    """
    # Step 1: Build the graph using adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prerequisit in prerequisites:
        graph[course].append(prerequisit)

    # Step 2: Initialize visited and recStack arrays
    visited = [False] * numCourses # is the course visited
    recStack = [False] * numCourses # is the course in the recursion stack

    # Step 3: Define the DFS function
    def isCyclic(node: int) -> bool:
        # If the course is already in the recursion stack, then there is a cycle
        visited[node] = True
        recStack[node] = True
        # Check all the neighbors of the course
        for neighbor in graph[node]:
            # If the neighbor is not visited, then visit it
            if not visited[neighbor]:
                # If the neighbor has a cycle, then return True
                if isCyclic(neighbor):
                    return True
            # If the neighbor is in the recursion stack, then there is a cycle
            elif recStack[neighbor]:
                return True
        # Remove the course from the recursion stack
        recStack[node] = False
        return False

    # Step 4: Check each course for cycles
    for course in range(numCourses):
        # If the course is not visited, then check for cycles
        if not visited[course]:
            # If there is a cycle, then return False
            if isCyclic(course):
                return False

    return True

if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(canFinish(numCourses, prerequisites))  # True

    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print(canFinish(numCourses, prerequisites))  # False