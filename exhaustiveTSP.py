import math
import time

start = time.time()

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def tsp(graph):
    # get the number of nodes in the graph
    n = len(graph)
    # calculate the number of possible permutations
    # (n! / (n-k)!) where k is the number of edges
    num_permutations = math.factorial(n) // (math.factorial(n - 2) * 2)
    # create a list to store the best permutation and its cost
    best_permutation = []
    best_cost = float("inf")
    # loop through all possible permutations
    for i in range(num_permutations):
        # convert the integer i to a permutation of 0, 1, 2, ..., n-1
        permutation = list(permutations(range(n)))[i]
        # calculate the cost of the current permutation
        cost = 0
        for j in range(n - 1):
            # get the indices of the adjacent nodes
            u = permutation[j]
            v = permutation[j + 1]
            # calculate the distance between the nodes
            cost += graph[u][v]
        # check if the current permutation is the best one so far
        if cost < best_cost:
            best_permutation = permutation
            best_cost = cost
    # return the best permutation and its cost
    return best_permutation, best_cost

# Example graph represented as an adjacency matrix
# graph = [
#     [0, 6, 8, 3, 5, 7, 2, 4, 9, 5], 
#     [6, 0, 4, 7, 9, 2, 1, 3, 8, 7], 
#     [8, 4, 0, 2, 6, 1, 9, 7, 5, 3], 
#     [3, 7, 2, 0, 4, 8, 5, 6, 1, 9], 
#     [5, 9, 6, 4, 0, 3, 7, 2, 6, 4], 
#     [7, 2, 1, 8, 3, 0, 6, 5, 3, 2], 
#     [2, 1, 9, 5, 7, 6, 0, 8, 2, 1], 
#     [4, 3, 7, 6, 2, 5, 8, 0, 4, 6], 
#     [9, 8, 5, 1, 6, 3, 2, 4, 0, 5], 
#     [5, 7, 3, 9, 4, 2, 1, 6, 5, 0]
# ]

# graph = [
#     [0, 6, 8, 3, 5, 7, 2, 4, 9],
#     [6, 0, 4, 7, 9, 2, 1, 3, 8],
#     [8, 4, 0, 2, 6, 1, 9, 7, 5],
#     [3, 7, 2, 0, 4, 8, 5, 6, 1],
#     [5, 9, 6, 4, 0, 3, 7, 2, 6],
#     [7, 2, 1, 8, 3, 0, 6, 5, 3],
#     [2, 1, 9, 5, 7, 6, 0, 8, 2],
#     [4, 3, 7, 6, 2, 5, 8, 0, 4],
#     [9, 8, 5, 1, 6, 3, 2, 4, 0]
# ]

# graph = [
#     [0, 6, 8, 3, 5, 7, 2, 4], 
#     [6, 0, 4, 7, 9, 2, 1, 3], 
#     [8, 4, 0, 2, 6, 1, 9, 7], 
#     [3, 7, 2, 0, 4, 8, 5, 6], 
#     [5, 9, 6, 4, 0, 3, 7, 2], 
#     [7, 2, 1, 8, 3, 0, 6, 5], 
#     [2, 1, 9, 5, 7, 6, 0, 8], 
#     [4, 3, 7, 6, 2, 5, 8, 0] 
# ]

# graph = [
#     [0, 6, 8, 3, 5, 7, 2], 
#     [6, 0, 4, 7, 9, 2, 1], 
#     [8, 4, 0, 2, 6, 1, 9], 
#     [3, 7, 2, 0, 4, 8, 5], 
#     [5, 9, 6, 4, 0, 3, 7], 
#     [7, 2, 1, 8, 3, 0, 6], 
#     [2, 1, 9, 5, 7, 6, 0] 
# ]

# graph = [
#     [0, 6, 8, 3, 5, 7], 
#     [6, 0, 4, 7, 9, 2], 
#     [8, 4, 0, 2, 6, 1], 
#     [3, 7, 2, 0, 4, 8], 
#     [5, 9, 6, 4, 0, 3], 
#     [7, 2, 1, 8, 3, 0]
# ]

# graph = [
#     [0, 6, 8, 3, 5], 
#     [6, 0, 4, 7, 9], 
#     [8, 4, 0, 2, 6], 
#     [3, 7, 2, 0, 4], 
#     [5, 9, 6, 4, 0] 
# ]

# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# graph = [
#     [0, 6, 8], 
#     [6, 0, 4], 
#     [8, 4, 0] 
# ]

graph = [
    [0, 15],
    [20, 0]
]

# Solve the TSP using the provided graph
final_permutation, total_cost = tsp(graph)

# Print the results
print("Final Permutation:", final_permutation)
print("Total Cost:", total_cost)

end = time.time()
print("Running time : ")
print(end - start)