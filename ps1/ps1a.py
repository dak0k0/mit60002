###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here

    cowDict = {}
    with open(filename) as cowFile:
        for line in cowFile:
            cow = line.split(",")
            cowDict[cow[0]] = int(cow[1])
    
    return cowDict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    trips = []                  # initialize a list of all tirps
    cowsCopy = cows.copy()      # create a copy of the dictionary that we can mutate
    numCows = len(cowsCopy)     # helper variables
    cowsMoved = 0
    numTrips = 0;

    cowsCopy = sorted(cowsCopy.items(), key = lambda x : x[1], reverse = True)      # sort the cows by weight in descending order
                                                                                    # use lambda function to sort by value
    cowsCopy = dict(cowsCopy)                                                       # cast the sorted list to a dictionary
    while(cowsMoved < numCows):                                                     # while not all cows have been moved....
        tripWeight = 0                                                              # initialize a trip
        trips.append([])
        for k, v in cowsCopy.items():                                               # iterate through all cows
            if v + tripWeight <= limit:                                             # add cow to trip if it's able to fit
                trips[numTrips].append(k)
                tripWeight += v
                cowsMoved += 1

        for cow in trips[numTrips]:                                                 # remove all cows that have been added from the dictionary
            del cowsCopy[cow]

        numTrips += 1
            
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    # pseudocode
    # try all iterations of 1 trip
    # then try all iterations of 2 trips
    # etc.

    minPartition = ([], len(cows))

    for partition in get_partitions(cows):
        numSuccessfulTrips = 0
        for trip in partition:
            tripWeight = 0
            for cow in trip:
                tripWeight += cows[cow]
            if tripWeight <= limit:
                numSuccessfulTrips += 1
            else:
                break
        if (numSuccessfulTrips == len(partition)) & (len(partition) < minPartition[1]):
            minPartition = (partition, len(partition))
    
    return minPartition[0]

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here

    cows = load_cows("ps1_cow_data.txt")

    start = time.time()
    brute = brute_force_cow_transport(cows)
    end = time.time()
    bruteTime = end - start

    start = time.time()
    greedy = greedy_cow_transport(cows)
    end = time.time()
    greedyTime = end - start

    print("Brute algo: ", len(brute), " trips in ", bruteTime, " seconds.")
    print("Greedy algo: ", len(greedy), " trips in ", greedyTime, " seconds.")

compare_cow_transport_algorithms()


"""

Writeup:
1. What were your results from compare_cow_transport_algorithms? Which
algorithm runs faster? Why?
    Brute force gave an option with 5 trips in 0.27 seconds. Greedy gave an option with 6 trips in 0.0 seconds. Greedy is faster.

2. Does the greedy algorithm return the optimal solution? Why/why not?
    No. Brute force gave an arrangement with only 5 trips as opposed to Greey's 6. It is able to give a better solution because it
    iterates through all possible options, while Greedy just returns the first option the works.

3. Does the brute force algorithm return the optimal solution? Why/why not?
    Brute returns the optimal solution.

"""