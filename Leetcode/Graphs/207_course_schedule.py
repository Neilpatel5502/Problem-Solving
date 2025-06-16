# Problem: https://leetcode.com/problems/course-schedule

# Time Complexity: O(V + E)           # V = numCourses, E = len(prerequisites)
# Space Complexity: O(V + E)          # For graph, visited and cycle set

def canFinish(numCourses, prerequisites):
    """
    Approach:
        - Build a directed graph where each node represents a course.
        - Perform DFS to check for cycles.
        - Use a `cycle` set to track nodes in the current DFS path.
        - If a node is revisited while still in the DFS path, a cycle is detected.
        - Use a `visited` set to memoize nodes that are already confirmed to be acyclic.
        - If all nodes are checked without detecting a cycle, return True.
    """
    graph = {i: [] for i in range(numCourses)}   # Adjacency list

    # Build graph: edge a → b means "to take a, you must take b first"
    for a, b in prerequisites:
        graph[a].append(b)

    visited = set()  # Courses confirmed as acyclic
    cycle = set()    # Courses in the current DFS path

    def dfs(course):
        if course in cycle:
            return False  # Cycle detected
        if course in visited:
            return True   # Already processed and safe

        cycle.add(course)
        for dep in graph[course]:
            if not dfs(dep):
                return False

        cycle.remove(course)
        visited.add(course)  # Mark as visited (safe)
        return True

    # Check all courses
    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


def main():
    # Test - 1:
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"output-1: {canFinish(numCourses1, prerequisites1)}")

    # Test - 2:
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"output-2: {canFinish(numCourses2, prerequisites2)}")

if __name__ == "__main__":
    main()
