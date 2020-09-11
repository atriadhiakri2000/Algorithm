import atexit
import io
import sys
from collections import defaultdict 

def findLongestConseqSubseq(arr, N):
    arr.sort()
    len=1
    for i in arr:
        if i-1 not in arr:
            j=1
            while(i+j in arr):
                j=j+1
            len=max(len,j)
    return(len)
