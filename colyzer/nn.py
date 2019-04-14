import numpy as np
import copy

'''
                        NEAREST NEIGHBOUR ALGORITHM
                        ---------------------------


The algorithm takes two arguments. The first one is an array, with elements
being lists/column-vectors from the given complete incidensmatrix. The second
argument is an integer which represents the startingnode where 1 is the
smallest. The program will only make sense, if the triangle inequality is satisfied.
Furthermore, diagonal elements needs to be inf. The pseudocode is listed below:


1. - stand on an arbitrary vertex as current vertex.
2. - find out the shortest edge connecting current vertex and an unvisited vertex V.
3. - set current vertex to V.
4. - mark V as visited.
5. - if all the vertices in domain are visited, then terminate.
6. - Go to step 2.

The sequence of the visited vertices is the output of the algorithm

Remark - infinity is entered as np.inf
'''

def NN(A, start):

    start = start-1 #To compensate for the python index starting at 0.
    n = len(A)
    path = [start]
    costList = []
    tmp = copy.deepcopy(start)
    B = copy.deepcopy(A)

    #This block eliminates the startingnode, by setting it equal to inf.
    for h in range(n):
        B[h][start] = np.inf

    for i in range(n):

        # This block appends the visited nodes to the path, and appends
        # the cost of the path.
        for j in range(n):
            if B[tmp][j] == min(B[tmp]):
                costList.append(B[tmp][j])
                path.append(j)
                tmp = j
                break

        # This block sets the current node to inf, so it can't be visited
        # again.
        for k in range(n):
            B[k][tmp] = np.inf

    # The last term adds the weight of the edge connecting the start - and
    # endnote.
    cost = sum([i for i in costList if i < np.inf]) + A[path[len(path)-2]][start]

    # The last element needs to be popped, because it is equal to inf.
    path.pop(n)

    # Because we want to return to start, we append this node as the last
    # element.
    path.insert(n, start)

    # Prints the path with original indicies.
    path = [i+1 for i in path]

    return path, cost

'''
If the desired result is to know the path and cost from every startnode,
then initialize the following method:
'''
def every_node(A):
    for i in range(1, len(A)):
        print(NN(A, i))
    return ""
