# Problem: https://leetcode.com/problems/car-fleet
# Time Complexity: O(n log n) – due to sorting by position
# Space Complexity: O(n) – for storing times on the stack

def carFleet(target, position, speed):
    """
    Approach:
        - Pair up each car's position and speed, then sort them in descending order of position.
        - This ensures we evaluate cars from closest to the target backwards.
        - Compute the time each car takes to reach the target.
        - Use a stack to track the fleets:
            - If a car takes more time than the car ahead (i.e., stack top), it becomes a new fleet.
            - If it takes less or equal time, it will merge into the fleet ahead (no new fleet formed).
        - The stack size at the end represents the number of distinct car fleets.
    """

    # Pair and sort cars by position descending
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)

    stack = []  # Stack to track arrival times of fleets

    for p, s in pair:
        time = (target - p) / s  # Time to reach the target
        stack.append(time)

        # If current car catches up to fleet ahead, they merge
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()  # No new fleet formed

    return len(stack)


def main():
    # Test - 1
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    print(f"output-1: {carFleet(target1, position1, speed1)}")

    # Test - 2
    target2 = 10
    position2 = [3]
    speed2 = [3]
    print(f"output-2: {carFleet(target2, position2, speed2)}")

    # Test - 3
    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    print(f"output-3: {carFleet(target3, position3, speed3)}")

if __name__ == "__main__":
    main()
