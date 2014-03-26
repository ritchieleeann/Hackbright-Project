import math
import analysis_2

rate1, data1 = analysis_2.read_file("Alohamora_1.wav")
data1 = analysis_2.normalize(data1)
bins1 = analysis_2.split(data1)

power_spectrum1 = analysis_2.power_spectrum(bins1)

filter_matrix1 = analysis_2.mel_filterbank(power_spectrum1)


dct_spectrum1 = analysis_2.MFCC(power_spectrum1, filter_matrix1)


rate2, data2 = analysis_2.read_file("Alohamora_3.wav")
data2 = analysis_2.normalize(data2)
bins2 = analysis_2.split(data2)

power_spectrum2 = analysis_2.power_spectrum(bins2)

filter_matrix2 = analysis_2.mel_filterbank(power_spectrum2)


dct_spectrum2 = analysis_2.MFCC(power_spectrum2, filter_matrix2)


seqx = dct_spectrum1[100]
seqy = dct_spectrum2[100]
 
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
 
    for row in cost:
       for entry in row:
          print "%03d" % entry,
       print ""
    return cost[-1][-1]

print dynamicTimeWarp(seqx,seqy)
