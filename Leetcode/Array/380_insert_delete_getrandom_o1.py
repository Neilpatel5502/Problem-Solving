# Problem: https://leetcode.com/problems/insert-delete-getrandom-o1

# Time Complexity:
#   - insert(): O(1)
#   - remove(): O(1)
#   - getRandom(): O(1)
# Space Complexity: O(n)

import random

class RandomizedSet:
    """
    Approach:
        - Use a dictionary `randomized_set` to store the value as key and its index in the list.
        - Use a list to maintain insertion order for O(1) random access.
        - insert(val): Add the element to the list and dictionary if not already present.
        - remove(val): Swap the element with the last one, remove it from the list and update dictionary.
        - getRandom(): Return a random element using random.choice from the list.
    """

    def __init__(self):
        self.randomized_set = dict()  # Maps value to its index in list
        self.list = []                # Stores the values for O(1) access

    def insert(self, val):
        # Only insert if not present
        if val not in self.randomized_set:
            self.randomized_set[val] = len(self.list)
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val):
        # Only remove if present
        if val in self.randomized_set:
            pos = self.randomized_set[val]       # Get index of element to remove
            last_element = self.list[-1]         # Get last element in list
            self.list[pos] = last_element        # Overwrite position with last element
            self.randomized_set[last_element] = pos  # Update index of last element
            self.list.pop()                      # Remove last element
            del self.randomized_set[val]         # Delete from dictionary
            return True
        else:
            return False

    def getRandom(self):
        # Return a random element from the list
        return random.choice(self.list)

def main():
    # Test - 1
    obj = RandomizedSet()
    output1 = [
        obj.insert(1),
        obj.remove(2),
        obj.insert(2),
        obj.getRandom(),
        obj.remove(1),
        obj.insert(2),
        obj.getRandom()
    ]

    print(f"outputs: {output1}")



if __name__ == "__main__":
    main()
