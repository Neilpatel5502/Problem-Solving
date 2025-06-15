# Problem: https://leetcode.com/problems/simplify-path

# Time Complexity: O(n), where n = length of the path string
# Space Complexity: O(n), for the stack

def simplifyPath(path):
    """
    Approach:
        - Split the input path by '/' to get path components.
        - Use a stack to simulate directory traversal.
            - '..' means go up one directory: pop from stack if not empty.
            - '.' or empty strings are ignored.
            - All other names are valid directories to be pushed onto the stack.
        - Join the stack with '/' to form the simplified absolute path.
    """
    stack = []
    path_list = path.split("/")

    for di in path_list:
        if di != "":
            if di == "..":
                stack.pop() if stack else None  # Go up one directory
            elif di == ".":
                continue  # Stay in the current directory
            else:
                stack.append(di)  # Valid directory, go deeper

    return "/" + "/".join(stack)  # Construct simplified path

def main():
    # Test - 1
    path1 = "/home/"
    print(f"output-1: {simplifyPath(path1)}")

    # Test - 2
    path2 = "/home//foo/"
    print(f"output-2: {simplifyPath(path2)}")

    # Test - 3
    path3 = "/home/user/Documents/../Pictures"
    print(f"output-3: {simplifyPath(path3)}")

    # Test - 4
    path4 = "/../"
    print(f"output-4: {simplifyPath(path4)}")

    # Test - 5
    path5 = "/.../a/../b/c/../d/./"
    print(f"output-5: {simplifyPath(path5)}")

if __name__ == "__main__":
    main()
