def maxValue(root): 
    current = root 
      
    #loop down to find the rightmost leaf 
    while(current.right): 
        current = current.right 
    return current.data 
