# Problem: https://leetcode.com/problems/word-ladder

# Time Complexity: O(n * m^2)       # n = number of words, m = word length
# Space Complexity: O(n * m)        # For graph (patterns), visited set, and queue

from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    """
    Approach:
        - Use BFS to find the shortest transformation sequence from beginWord to endWord.
        - Preprocess the word list to build a pattern-to-word map using wildcard '*'.
        - Each pattern groups words that differ by one letter.
        - Traverse using BFS, transforming one letter at a time, and stop once endWord is reached.
    """
    # Early exit if endWord is not in the word list
    if endWord not in wordList:
        return 0

    # Dictionary to map wildcard patterns to corresponding words
    neighbors = defaultdict(list)
    wordList.append(beginWord)  # Include beginWord in wordList for graph construction

    # Build the graph: for each word, create intermediate wildcard patterns
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]   # Replace one character with '*'
            neighbors[pattern].append(word)           # Add to pattern group

    # BFS initialization
    visited = set([beginWord])      # Track visited words to avoid cycles
    q = deque([beginWord])          # Start BFS from beginWord
    out = 1                       # Represents number of transformations

    # Perform BFS
    while q:
        for _ in range(len(q)):
            word = q.popleft()

            # If endWord is reached, return the out (transformation count)
            if word == endWord:
                return out

            # Generate all patterns from the current word
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]

                # For each pattern, explore all possible transformations
                for nei in neighbors[pattern]:
                    if nei not in visited:
                        visited.add(nei)   # Mark as visited
                        q.append(nei)      # Add to queue for next level

        out += 1  # Increment out after processing current level

    return 0  # No valid transformation found


def main():
    # Test - 1
    begin1 = "hit"
    end1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(f"output-1: {ladderLength(begin1, end1, wordList1)}")

    # Test - 2
    begin2 = "hit"
    end2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print(f"output-2: {ladderLength(begin2, end2, wordList2)}")

if __name__ == "__main__":
    main()
