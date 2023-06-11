import time

start = time.time()

def tsp(graph):
    # get the number of nodes in the graph
    n = len(graph)
    # create a list to store the current permutation and its cost
    permutasi = list(range(n))
    cost = 0
    # loop through all nodes in the graph
    for i in range(n - 1):
        # get the indices of the adjacent nodes
        u = permutasi[i]
        v = permutasi[i + 1]
        # calculate the distance between the nodes
        distance = graph[u][v]
        # add the distance to the total cost
        cost += distance
        # update the permutation to move to the next node
        permutasi[i + 1:] = permutasi[i + 2:] + [permutasi[i + 1]]
    # return the final permutation and its cost
    return permutasi, cost

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

graph = [
    [0, 6, 8, 3, 5], 
    [6, 0, 4, 7, 9], 
    [8, 4, 0, 2, 6], 
    [3, 7, 2, 0, 4], 
    [5, 9, 6, 4, 0] 
]

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

# graph = [
#     [0, 15],
#     [20, 0]
# ]

# Solve the TSP using the provided graph
final_permutation, total_cost = tsp(graph)

# Print the results
print("Final Permutation:", final_permutation)
print("Total Cost:", total_cost)


end = time.time()
print("Running time : ")
print(end - start)