###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

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

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

class Cattle(object):
    def __init__(self, n, w):
        self.name = n
        self.weight = w
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.name + ", " + str(self.weight)

def buildCows(dict):
    cow_list = []
    for i, j in dict.items():
        cow_list.append(Cattle(n = i, w = j))
    return cow_list

cow_set = buildCows(cows)

# Problem 1
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
def greedy_cow_transport(cows,limit=10):
    # TODO: Your code here

    """
    ---- First Try Code ----
        items_sort = sorted(cow_set, reverse = True, key = Cattle.getWeight)
        result = []
        total_weight = 0
        for i in range(len(items_sort)):
            if (total_weight + items_sort[i].getWeight()) <= limit:
                result.append(items_sort[i].getName())
                total_weight += items_sort[i].getWeight()
        return (result, total_weight)
    """

    items_sort = sorted(cow_set, reverse = True, key = Cattle.getWeight)
    result = []
    while items_sort != []:
        trip_list = []
        trip_weight = 0
        for i in range(len(items_sort)):
            if (trip_weight + items_sort[i].getWeight()) <= limit:
                trip_list.append(items_sort[i].getName())
                trip_weight += items_sort[i].getWeight()
                items_sort.remove(items_sort[i])
            result.append((trip_list, trip_weight))
    return result
    pass

"""
This manipulates the original dictionary, converting it into a class of cows. I can't figure out how to run through iterations of a dictionary
"""


"""
---- Me trying different ways to search through a dictionary, but without finding a solution ----
def greedy_cow_transport2(cows, limit = 10):
    cow_dict = sorted(cows.items(), key = lambda x: x[1], reverse = True)
    result = []
    while cow_dict != {}:
        trip_weight = 0
        trip_list = []
        for i in cow_dict:
            if ((trip_weight + cow_dict[i].values()) <= limit):
                trip_weight += cow_dict[i].values()
                trip_list.append(cow_dict[i].keys())
                cow_dict.pop(cow_dict[i].key())
        result.append((trip_list, trip_weight))
    return result

def greedy_cow_transport3(cows, limit = 10):
    result = []
    while cow_dict != {}:
        trip_weight = 0
        trip_list = []
        while ()
"""


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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

    pass


# Problem 3
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
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


