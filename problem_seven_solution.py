def solution(X, A):
    n = len(A)
    # getting the length of the list
    if X > n+1:
        return -1
        # there is not enough time to get all the leaves for our frog
    
    H = [0]*X
    #creating a list for the numbers we have
    for i in range(X):
        H[i] = i+1
    for i, j in enumerate(A):
        if H.count(j) == 1 and len(H) == 1:
            return i
        if H.count(j) == 1:
            H.pop((H.index(j)))
        
    return -1
