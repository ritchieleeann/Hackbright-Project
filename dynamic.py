import math
import analysis_2
import numpy as np
import os



# seqx = analysis_2.master(os.path.abspath("audios/Alohamora_3.wav"))
# seqy = analysis_2.master(os.path.abspath("audios/Alohamora_3.wav"))
 

def dynamicTimeWarp(seqA, seqB, d = lambda x,y: abs(x-y)):
    # create the cost matrix
    numRows, numCols = len(seqA), len(seqB)
    cost = [[0 for _ in range(numCols)] for _ in range(numRows)]
 
    # initialize the first row and column
    cost[0][0] = d(seqA[0], seqB[0])
    for i in xrange(1, numRows):
        cost[i][0] = cost[i-1][0] + d(seqA[i], seqB[0])
 
    for j in xrange(1, numCols):
        cost[0][j] = cost[0][j-1] + d(seqA[0], seqB[j])
 
    # fill in the rest of the matrix
    for i in xrange(1, numRows):
        for j in xrange(1, numCols):
            choices = cost[i-1][j], cost[i][j-1], cost[i-1][j-1]
            cost[i][j] = min(choices) + d(seqA[i], seqB[j])
 
    # for row in cost:
       # for entry in row:
       #    print "%03d" % entry,
       # print ""
    test_cost = cost[-1][-1]

    return test_cost

def match_test(test_cost):
    if test_cost <= 300:
        return True
    else:
        return False


# print dynamicTimeWarp(seqx,seqy)
# print match_test(test_cost)
# print test_cost 












# def DTW(seqx, seqy, d = lambda x,y: abs(x.all()-y.all())):
#     # create the cost matrix
#     numRows, numCols = 13 * len(seqx), 13 * len(seqy)
#     print numRows, numCols
#     cost = [[0 for _ in range(numCols)] for _ in range(numRows)]
 
#     # initialize the first row and column
#     cost[0][0] = d(seqx[0], seqy[0])
#     for i in xrange(1, numRows):
#         cost[i][0] = cost[i-1][0] + d(seqx[i], seqy[0])
 
#     for j in xrange(1, numCols):
#         cost[0][j] = cost[0][j-1] + d(seqx[0], seqy[j])
 
#     # fill in the rest of the matrix
#     for i in xrange(1, numRows):
#         for j in xrange(1, numCols):
#             choices = cost[i-1][j], cost[i][j-1], cost[i-1][j-1]
#             cost[i][j] = min(choices) + d(seqx[i], seqy[j])
 
#     # for row in cost:
#     #    for entry in row:
#     #       print "%03d" % entry,
#     #    print ""
#     return cost[-1][-1]

# print DTW(seqx, seqy, d = lambda x,y: abs(x.all()-y.all()))


# def alternateDTW(seqA, seqB, distance=lambda x,y: abs(x.all()-y.all())):
#     row = []
#     current_seqA = seqA[0]
#     for val_seqB in seqB:
#         row.append(distance(current_seqA, val_seqB))

#     for val_seqA in range(1, 13 *len(seqA)):
#         current_seqA = seqB[val_seqA]

#         temp = row[0]
#         row[0] = distance(current_seqA, seqB[0]) + row[0]

#         for i in range (1, 13 * len(seqB)):
#             temp_2 = row[i]

#             row[i] = distance(current_seqA, seqB[i]) + min(row[i-1], temp, temp_2)

#             temp = temp_2

#     return row[-1]        



# print alternateDTW(seqx, seqy, distance=lambda x,y: abs(x.all()-y.all()))
