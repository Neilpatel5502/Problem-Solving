# Problem Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies

# Time Complexity: O(N + M)         N = Len of supplies, M = Len of recipes
# Space Complexity: O(N + M)

def findAllRecipes(recipes, ingredients, supplies):
    """
    Approach:
        - Dict `cook` to keep track of ingredients it already have or can prepare.
        - Use another dict `recipe_index` to map each recipe name to its index in the `recipes` list.
        - Perform a DFS for each recipe to check if it can be made using available ingredients.
        - If all ingredients of a recipe are either in `supplies` or can be prepared recursively,
        mark the recipe as cookable.
        - Avoid cycles by temporarily marking a recipe as `False` in `cook` before checking its ingredients.
    """
    cook = {s:True for s in supplies}
    recipe_index = {r:i for i, r in enumerate(recipes)}

    def dfs(r):
        if r in cook:
            return cook[r]          # Return if we already determined its status
        if r not in recipe_index:
            return False            # If it's not a recipe, return False

        cook[r] = False             # Temporarily mark as False to avoid cycles

        # Check if all ingredients of the recipe can be prepared
        for i in ingredients[recipe_index[r]]:
            if not dfs(i):
                return False

        cook[r] = True              # Mark recipe as cookable
        return cook[r]

    # Return all recipes that can be prepared
    return [r for r in recipes if dfs(r)]


def main():
    # Test - 1
    recipes1 = ["bread"]
    ingredients1 = [["yeast","flour"]]
    supplies1 = ["yeast","flour","corn"]
    print(f"output-1: {findAllRecipes(recipes1, ingredients1, supplies1)}")

    # Test - 2
    recipes2 = ["bread","sandwich"]
    ingredients2 = [["yeast","flour"],["bread","meat"]]
    supplies2 = ["yeast","flour","meat"]
    print(f"output-2: {findAllRecipes(recipes2, ingredients2, supplies2)}")

    # Test - 3
    recipes3 = ["bread","sandwich","burger"]
    ingredients3 = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies3 = ["yeast","flour","meat"]
    print(f"output-3: {findAllRecipes(recipes3, ingredients3, supplies3)}")


if __name__ == "__main__":
    main()
