# Problem: https://leetcode.com/problems/gas-station

# Time Complexity: O(n)
# Space Complexity: O(1)

def canCompleteCircuit(gas, cost):
    """
    Approach:
        - If total gas is less than total cost, it's impossible to complete the circuit. Return -1.
        - Traverse the gas stations while maintaining a running `total` of gas - cost.
        - If at any point this total becomes negative, reset the total and start the journey from the next station.
        - The idea is that the segment we skipped can never be the start of a successful journey.
        - The index `out` will eventually point to the correct start station if a solution exists.
    """
    # Total gas available is less than required cost — circuit not possible
    if sum(gas) < sum(cost):
        return -1

    total = 0     # Running total of net gas (gas - cost)
    out = 0       # Potential starting index

    for i in range(len(gas)):
        total += gas[i] - cost[i]  # Net gas at station i

        # If we can't reach next station from current segment
        if total < 0:
            total = 0             # Reset the net gas
            out = i + 1           # Try next station as starting point

    return out


def main():
    # Test case 1
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(f"output-1: {canCompleteCircuit(gas1, cost1)}")

    # Test case 2
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    print(f"output-2: {canCompleteCircuit(gas2, cost2)}")


if __name__ == "__main__":
    main()
