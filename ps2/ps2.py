# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
# The graph's nodes represent buildings. The edges represent ways to get from one building to another.
# To display the graph, i will go through each individual building and print out all of the places you can go from that building, with
# the weights displayed next to the dest in parentheses.
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    # TODO
    print("Loading map from file...")

    g = Digraph()

    with open(map_filename) as file:
        for line in file:
            line = line.split()
            src = Node(line[0])
            dest = Node(line[1])
            if not g.has_node(src):
                g.add_node(src)
            if not g.has_node(dest):
                g.add_node(dest)
            edge = WeightedEdge(src, dest, int(line[2]), int(line[3]))
            g.add_edge(edge)

    return g

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out

# map = load_map("test_load_map.txt")
# print(map)

#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: The objective is the total distance traveled. We want to find the shortest route possible between two points. The constraint
#         is the amount of time spent outdoors - there is a maximum amount of time that we are willing to spend outdoors.
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # TODO

    path[0] = path[0] + [start]                                                     # add to the path
    if((not digraph.has_node(Node(start))) or (not digraph.has_node(Node(end)))):   # check if the nodes exist in the graph
        raise ValueError('node is not defined')                                     
    elif start == end:                                                              # check if we've reached the end
        return path                                                                 # if we have, return path
    else:
        for edge in digraph.get_edges_for_node(Node(start)):                        # beginning at the first node, iterate through each edge (each next possible node)
            pathLength = path[1]                                                    # initialize path length
            outdoorsDistance = path[2]                                              # and distance outdoors
            newStart = edge.dest.get_name()                                         # alias for next possible node
            if newStart not in path[0]:                                             # check if we have not already visited the next possible node; if we have, go to the next edge
                outdoorsDistance += edge.get_outdoor_distance()                     # if it's a new node, accumulate distance outdoors
                if(outdoorsDistance <= max_dist_outdoors):                          # check that this path meets the constraint; if it doesn't, go to the next edge
                    pathLength += edge.get_total_distance()                         # if we meet the constraint, accumulate path length
                    if(pathLength < best_dist):                                     # check that the path is less than the current best path
                        newPath = get_best_path(digraph, newStart, end, [path[0],   # if it is, find the best path to the end from this potential next node
                            pathLength, outdoorsDistance],
                            max_dist_outdoors, best_dist, best_path)
                        if newPath:                                                 # check if a path from this potential next node to the end exists
                            best_path = newPath                                     # if it does, update best path
                            best_dist = newPath[1]
    return best_path                                                                # return best path
        



# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    best_dist = 99999           # set an arbitrarily large initial best distances
    best_path = None
    best_path = get_best_path(digraph, start, end, [[], 0, 0], max_dist_outdoors, best_dist, best_path)     # find the shortest path within the max dist outdoors
    if best_path:                               # if a path exists....
        if(best_path[1] < max_total_dist):      # if the path's distance is within the max total distance,
            return best_path[0]                 # return the path
    raise ValueError("no existing path")        # otherwise, raise an error


# map = load_map("test_load_map.txt")
# print(directed_dfs(map, 'a', 'c', 99999, 0))

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
