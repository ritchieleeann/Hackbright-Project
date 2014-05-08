import math
import analysis_2
import numpy as np
import os



# seqx = analysis_2.master(os.path.abspath("audios/Alohamora_3.wav"))
# seqy = analysis_2.master(os.path.abspath("audios/Alohamora_3.wav"))
 
#compare two audios with dynamic time warping
def dynamicTimeWarp(seqA, seqB, d = lambda x,y: math.pow(abs(x-y),2)):
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
 

    test_cost = cost[-1][-1]

    return test_cost

#define threshhold and return match results
def match_test(test_cost):
    if test_cost <= 1000:
        return True
    else:
        return False


# print dynamicTimeWarp(seqx,seqy)
# print match_test(test_cost)
# print test_cost 













