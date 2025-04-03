# Problem Link: https://leetcode.com/problems/solving-questions-with-brainpower

# Time Complexity: O(N) (where N is the number of questions, since we iterate once)
# Space Complexity: O(N) (for storing dp values)

def mostPoints(questions):
    """
    Approach:
        - We use Dynamic Programming (DP) to solve this problem efficiently.
        - We maintain a dp array where `dp[i]` stores the maximum points we can earn starting from question `i`.
        - We iterate backwards from the last question to the first:
        - If we solve question `i`, we gain its points and skip the next `brainpower` questions.
        - If we skip question `i`, we move to the next question as normal.
        - We store the maximum of these two choices in `dp[i]`.
        - The answer is stored in `dp[0]`, representing the maximum points we can earn starting from question `0`.
    """
    # Recursive approach with caching (Top-down memoization)
    # Uncomment the following lines if you want to use recursion instead of DP.

    # cache = [0] * len(questions)
    # def backtrack(i):
    #     if i >= len(questions):   # Base case: If out of bounds, return 0 points
    #         return 0
    #     if cache[i]:
    #         return cache[i]
    #     points, brainpower = questions[i]
    #     cache[i] = max(
    #         backtrack(i + 1),                         # Skip the question and move to the next one
    #         points + backtrack(i + 1 + brainpower)    # Solve the question and skip 'brainpower' questions
    #     )

    #     return cache[i]

    # return backtrack(0)

    # Bottom-Up Approach
    dp = [0] * len(questions)

    for i in range(len(questions) - 1, -1, -1):
        points, brainpower = questions[i]

        # Solve the current question
        choose = points + (dp[i + 1 + brainpower] if i + 1 + brainpower < len(questions) else 0)

        # Skip the current question
        skip = dp[i + 1] if i + 1 < len(questions) else 0

        # Store the maximum points we can earn starting from question `i`
        dp[i] = max(choose, skip)

    # The answer is stored at dp[0], which represents max points from the first question onward
    return dp[0]


def main():
    # Test - 1
    questions1 = [[3,2],[4,3],[4,4],[2,5]]
    print(f"output-1: {mostPoints(questions1)}")

    # Test - 2
    questions2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    print(f"output-2: {mostPoints(questions2)}")

if __name__ == "__main__":
    main()
