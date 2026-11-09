def solution(A):
    while len(A) > 1:
        for i, x in enumerate(A):
            if A.count(x) % 2 == 1:
                return A[i]
    return A[0]
