# Problem: https://leetcode.com/problems/minimum-genetic-mutation

# Time Complexity: O(n * m)         # n = len(bank), m = gene length (always 8)
# Space Complexity: O(n)            # For visited set and BFS queue

from collections import deque

def minMutation(startGene, endGene, bank):
    """
    Approach:
        - Use BFS to find the shortest sequence of valid gene mutations from startGene to endGene.
        - At each step, generate all possible 1-character mutations using 'A', 'C', 'G', 'T'.
        - Only enqueue mutations that exist in the bank and are not visited.
        - Return the mutation count when endGene is reached.
        - If not reachable, return -1.
    """

    if endGene not in bank:
        return -1

    bank = set(bank)
    visited = set([startGene])
    queue = deque([[startGene, 0]])     # (Mutuation string, moves)

    while queue:
        gene, mutation = queue.popleft()

        if gene == endGene:
            return mutation

        # Try all one-letter mutations
        for i in range(8):
            for c in 'ACGT':
                mutated = gene[:i] + c + gene[i+1:]

                # If mutuation in bank and not visited yet add into the queue.
                if mutated in bank and mutated not in visited:
                    visited.add(mutated)
                    queue.append([mutated, mutation + 1])

    return -1


def main():
    # Test - 1
    start1 = "AACCGGTT"
    end1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    print(f"output-1: {minMutation(start1, end1, bank1)}")

    # Test - 2
    start2 = "AACCGGTT"
    end2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(f"output-2: {minMutation(start2, end2, bank2)}")

if __name__ == "__main__":
    main()
