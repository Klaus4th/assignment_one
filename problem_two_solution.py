def solution(A):
    while len(A) > 1:
        for i, x in enumerate(A):
            if A.count(x) % 2 == 1:
                #if an element in the list has an odd number of occurences in the list, we return it
                return A[i]
    return A[0]
