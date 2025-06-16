# Problem: https://leetcode.com/problems/course-schedule-ii

# Time Complexity: O(V + E)           # V = numCourses, E = prerequisites
# Space Complexity: O(V + E)          # Graph, visited, cycle, output

def findOrder(numCourses, prerequisites):
    """
    Approach:
        - Build a graph where each edge a → b means "to take course a, you need course b first".
        - Use DFS with cycle detection to check if it's possible to finish all courses.
        - If a cycle is detected, return an empty list.
        - Use post-order DFS traversal to generate the topological sort.
        - Append nodes after visiting all dependencies, then reverse the result.
    """
    graph = {i: [] for i in range(numCourses)}

    # Construct the adjacency list
    for a, b in prerequisites:
        graph[a].append(b)

    cycle = set()      # Tracks current recursion stack for cycle detection
    visited = set()    # Memoization of safe nodes
    out = []           # Stores post-order nodes for topological sort

    def dfs(course):
        if course in cycle:
            return False         # Cycle detected
        if course in visited:
            return True          # Already processed safely

        cycle.add(course)
        for dep in graph[course]:
            if not dfs(dep):
                return False

        cycle.remove(course)
        visited.add(course)
        out.append(course)       # Post-order addition

        return True

    for course in range(numCourses):
        if not dfs(course):
            return []            # Return empty list on cycle detection

    return out


def main():
    # Test - 1:
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"output-1: {findOrder(numCourses1, prerequisites1)}")

    # Test - 3:
    numCourses2 = 4
    prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"output-3: {findOrder(numCourses2, prerequisites2)}")

    # Test - 3:
    numCourses3 = 1
    prerequisites3 = []
    print(f"output-2: {findOrder(numCourses3, prerequisites3)}")

if __name__ == "__main__":
    main()
