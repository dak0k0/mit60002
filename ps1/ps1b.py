###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here

    if target_weight in memo.keys():                                            # first, check if the target weight is in the memo or not
        result = memo[target_weight]                                            # if it is, pull result from the memo
    elif target_weight == 0:                                                    # base case: 0 eggs needed for 0 lbs
        result = 0
    else:                                                                       # all other cases
        new_targets = []                                                        # initialize a list for potential new targets based on egg weights
        for weight in egg_weights:                                              # iterate through all egg weights, testing against target weight
            if target_weight - weight >= 0:                                     # if the weight is <= target weight, add the potential new target to the list
                new_targets.append(target_weight - weight)
            result = dp_make_weight(egg_weights, min(new_targets), memo) + 1    # recurse on whichever new target weight is smallest and add 1 to
                                                                                # the total number eggs, indicating an egg having been put towards the final weight
        memo[target_weight] = result                                            # assign the new result to the memo for future use
    
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()