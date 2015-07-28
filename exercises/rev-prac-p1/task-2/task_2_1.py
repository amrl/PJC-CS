# initialise array
X = ['' for i in range(20)]
X[0] = 999
X[1] = 850
X[2] = 812
X[3] = 770
X[4] = 733
X[5] = 634
X[6] = 511
X[7] = 508
X[8] = 500
X[9] = 497
X[10] = 413
X[11] = 406
X[12] = 389
X[13] = 310
X[14] = 292
X[15] = 251
X[16] = 107
X[17] = 88
X[18] = 53
X[19] = 13


# note that this bsearch is for arrays in descending order
def rec_binarysearch(array, target, Low, High):
    if Low > High:
        return -1  # not found
    else:
        mid = (Low + High) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return rec_binarysearch(array, target, mid+1, High)
        else:
            return rec_binarysearch(array, target, Low, mid-1)


# print(rec_binarysearch(X, 500, 0, len(X)-1))
