# Problem: https://leetcode.com/problems/search-a-2d-matrix/
# Time Complexity: O(log(m * n)) – binary search on a virtual 1D array
# Space Complexity: O(1) – constant space used

def searchMatrix(matrix, target):
    """
    Approach:
        - Treat the 2D matrix as a 1D sorted array by flattening the indices.
        - Use binary search to search within the virtual 1D array.
        - Map 1D index back to 2D using:
            - row = index // number of columns
            - col = index % number of columns
        - Return True if element matches target, else adjust search range.
    """

    n = len(matrix)      # Number of rows
    m = len(matrix[0])   # Number of columns

    start = 0
    end = n * m - 1      # Total number of elements - 1

    while start <= end:
        mid = (start + end) // 2
        i = mid // m     # Row index
        j = mid % m      # Column index

        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


def main():
    # Test - 1
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    print(f"output-1: {searchMatrix(matrix1, target1)}")

    # Test - 2
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    print(f"output-2: {searchMatrix(matrix2, target2)}")

if __name__ == "__main__":
    main()
