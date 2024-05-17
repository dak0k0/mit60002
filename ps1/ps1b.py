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
        options = []                                                            # initialize a list for potential ways to make it to that weight
        for weight in egg_weights:                                              # iterate through all egg weights, testing against target weight
            if target_weight - weight >= 0:                                     
                options.append(dp_make_weight(egg_weights, target_weight - weight, memo))   # the least number of coins necessary to reach the target weight
                                                                                            # is 1 coin more than the least number of coins necessary to reach 
                                                                                            # the target weight minus any of the weight options.....i understand
                                                                                            # now why this was so difficult to understand

            result = min(options) + 1                                                       # add 1 egg to indicate contributing an egg towards the weight goal 
            memo[target_weight] = result                                                    # update memo
    
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

"""

Writeup:
1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there
were 30 different egg weights. You do not need to implement a brute force algorithm in order to
answer this.
    With 30 different egg weights, a brute force algorithm would have to explore an extremely
    large number of combinations of egg weights, which would take too long to do.

2. If you were to implement a greedy algorithm for finding the minimum number of eggs
needed, what would the objective function be? What would the constraints be? What strategy
would your greedy algorithm follow to pick which coins to take? You do not need to implement a
greedy algorithm in order to answer this.
    For a greedy algorithm, the objective function would be the smallest number of eggs needed to reach 99 lbs. The constraint would be the total
    weight must be exactly 99 lbs. The strategy would be as follows: add 25s until the different between 99 and the total weight is less than 25; then,
    add 10s, and so on

3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is
optimal or give an example of when it will not return the optimal solution. Again, you do not need
to implement a greedy algorithm in order to answer this.
    Greedy will not always return the optimal solution. For example, in the case of target weight 6 with options 1, 3, and 4, greedy will do
    4, 1, 1 (3 coins), when the correct solution is 3, 3 (2 coins).

"""